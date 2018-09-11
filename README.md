# python3-webapp-smiple
一个基于python3的webapp

### 过时写法
``` python
import asyncio
from aiohttp import web
def index():
  return web.Response(body=b'<h1>a Smiple Python3 WebApp</h1>')

async def init(loop):
  app = web.Application(loop=loop)
  app.router.add_route('GET', '/', index)
  srv = await loop.create_server(app.make_handler(), 'localhost', 8080)
  logging.info('server started at http://localhost:8080...')
  return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
```
>运行时错误：DeprecationWarning: Application.make_handler(...) is deprecated, use AppRunner API instead
### 新写法
``` python
from aiohttp import web
routes = web.RouteTableDef()

@routes.get('/')
async def index(req):
  text = b'<h1>Smiple Python3 WebApp</h1>'
  return web.Response(body=text, charset='utf-8', content_type='text/html')

def init():
  app = web.Application()
  app.add_routes(routes)
  web.run_app(app, host='127.0.0.1', port='8080')

init()
```