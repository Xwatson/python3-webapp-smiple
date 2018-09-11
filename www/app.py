import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
routes = web.RouteTableDef()

"""
过时写法 
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
 """
@routes.get('/')
async def index(req):
  text = b'<h1>Smiple Python3 WebApp</h1>'
  return web.Response(body=text, charset='utf-8', content_type='text/html')

def init():
  app = web.Application()
  app.add_routes(routes)
  web.run_app(app, host='127.0.0.1', port='8080')

init()