from aiohttp import web

from app.api.http.handlers import test


def setup_routes(app):
    app.add_routes([
        web.get('/test', test.test),
    ])
