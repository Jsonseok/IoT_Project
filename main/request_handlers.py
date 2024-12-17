from common import response_html
async def mainHandle(request):
    return response_html('index.html')
#추가 내용
async def temperatureHandle(request):
    return response_html('temperature.html')

async def buttonHandle(request):
    return response_html('button.html')

async def loginHandle(request):
    return response_html('login.html')