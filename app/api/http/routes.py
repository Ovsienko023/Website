from aiohttp import web

from app.api.http.handlers import send_email, index


def setup_routes(app):
    app.add_routes([
        web.get('/test', send_email.test),
        web.get('/index', index.index)
    ])
