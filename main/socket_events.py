from common import get_system_info, sio

from gpio_button import start_button_monitoring, stop_button_monitoring

@sio.event
async def connect(sid, environ):
    print('클라이언트 연결', sid)
    await start_button_monitoring(sio, sid)

@sio.event
async def disconnect(sid):
    print('클라이언트 종료', sid)
    await stop_button_monitoring()

@sio.on('get_system_info')
async def on_get_system_info(sid, data):
    systemInfo = get_system_info()
    await sio.emit('ret_system_info', systemInfo, room=sid)


@sio.on('start_button_monitoring')
async def on_start_button_monitoring(sid, data):
    await start_button_monitoring(sio, sid)

@sio.on('stop_button_monitoring')
async def on_stop_button_monitoring(sid):
    await stop_button_monitoring()
