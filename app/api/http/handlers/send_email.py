from aiohttp import web


async def test(request: web.Request) -> web.Response:
    return web.json_response({"status": "hello"})

