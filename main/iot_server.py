import secrets
import asyncio
from aiohttp import web
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from common import web, app, sio
from request_handlers import mainHandle, buttonHandle  # request_handlers.py에서 mainHandle과 buttonHandle 함수를 가져옵니다.
import socket_events
from simple_conversation import create_chatbot

async def chatgptHandle(request):
    bot = create_chatbot()
    try:
        data = await request.json()
        user_input = data.get('userInput')
        if user_input == "HOWAREYOU":
            user_input = "HOW ARE YOU"
        if not user_input:
            return web.json_response({'error': 'No input provided'}, status=400)
        return web.json_response({'outputText': bot.respond(user_input)})
    except Exception as e:
        return web.json_response({'error': str(e)}, status=500)
# 암호화 키 설정
SETTING = {
    'SECRET_KEY': secrets.token_bytes(32),
    'COOKIE_NAME': 'session_cookie'
}
# 세션 미들웨어 설정
setup(app, EncryptedCookieStorage(SETTING['SECRET_KEY'], cookie_name=SETTING['COOKIE_NAME']))

async def web_server():
    app.router.add_static('/static/', path='static/', name='static')  # 리소스 위치
    app.router.add_get('/button', buttonHandle)  # http://본인아이피:5000/button

    app.router.add_get('/', mainHandle)  # http://본인아이피:5000
    app.router.add_post('/chatgpt', chatgptHandle)  # Add the new route for chatgpt

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 5000)  # http://본인아이피:5000
    await site.start()

async def main():
    try:
        await web_server()  # 웹 서버 시작
        # 무한 루프로 서버가 계속 실행되도록 유지
        while True:
            await asyncio.sleep(3600)  # 예시로, 1시간마다 대기를 풀고 다시 대기함
    except KeyboardInterrupt:
        print("프로그램이 사용자에 의해 종료됨.")
    except Exception as e:
        print(f"예외 발생: {e}")

if __name__ == '__main__':
    asyncio.run(main())
