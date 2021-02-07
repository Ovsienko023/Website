import aiohttp_jinja2

from aiohttp import web


@aiohttp_jinja2.template('index.html')
async def index(request: web.Request) -> web.Response:
    return {}
