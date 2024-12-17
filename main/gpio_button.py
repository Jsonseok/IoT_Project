import RPi.GPIO as GPIO
import asyncio
import threading
import time
from morse_translator import translator
# GPIO 설정
BUTTON_PIN = 18  # 버튼이 연결된 GPIO 핀 번호
BUTTON_PIN_2 = 17  # 버튼이 연결된 GPIO 핀 번호
LED_PIN  = 23
LONG_PRESS_TIME = 2.0
led_button_press_start = None

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 스레드 중지를 위한 플래그
is_button_monitoring = False
button_thread = None
button_lock = threading.Lock()
sequence = ""
word = []
led_button_press_start = None
async def send_button_data(sio, data, sid):
    # 클라이언트에게 수신 (비동기)
    await sio.emit('update_textbox', data, room=sid)


    
def cycle_button(sio, sid):
    global is_button_monitoring
    global word
    global sequence
    previous_state = GPIO.input(BUTTON_PIN)
    previous_state_2 = GPIO.input(BUTTON_PIN_2)
    led_previous_state = GPIO.input(LED_PIN)

    while is_button_monitoring:
        current_state = GPIO.input(BUTTON_PIN)
        current_state_2 = GPIO.input(BUTTON_PIN_2)
        led_currnet_state = GPIO.input(LED_PIN)

        if current_state != previous_state:
            previous_state = current_state
            if current_state == GPIO.LOW:
                sequence += "•"
                print('. 저장 완료')
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
        if current_state_2 != previous_state_2:
            previous_state_2 = current_state_2
            if current_state_2 == GPIO.LOW:
                sequence += "‒"
                print('- 저장 완료')
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                
        if led_currnet_state != led_previous_state:
            global led_button_press_start
            global sentence
            led_previous_state = led_currnet_state
            if led_currnet_state == GPIO.LOW:
                led_button_press_start = time.time()
            else:
                if led_button_press_start:
                    press_duration = time.time() - led_button_press_start
                    if press_duration < LONG_PRESS_TIME:
                        word.append(sequence)
                        sequence = ""
                        print("단어 저장")
                    else:
                        print(word)
                        trans_word = [translator(i) for i in word]
                        print(trans_word)
                        transed_word = ''.join(trans_word)
                        data = {'message': f'{transed_word}'}
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        asyncio.run(send_button_data(sio, data, sid))
                        word = []
                        print("단어 출력")

        time.sleep(0.1)

async def start_button_monitoring(sio, sid):
    global is_button_monitoring, button_thread
    with button_lock:
        if button_thread is None or not button_thread.is_alive():
            is_button_monitoring = True
            button_thread = threading.Thread(target=cycle_button, args=(sio, sid))
            button_thread.start()

async def stop_button_monitoring():
    global is_button_monitoring, button_thread
    with button_lock:
        is_button_monitoring = False
        if button_thread is not None:
            button_thread.join()
            button_thread = None

# 클린업 함수
def cleanup():
    GPIO.cleanup()
