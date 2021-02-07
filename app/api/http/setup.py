import jinja2
import aiohttp_jinja2
from aiohttp import web

# from app.core.constants.app import APP_LOGGER, APP_DATABASE_CLIENT
from .routes import setup_routes


def setup(app: web.Application) -> None:
    subapp = web.Application()

    # subapp[APP_DATABASE_CLIENT] = app[APP_DATABASE_CLIENT]
    # subapp[APP_LOGGER] = app[APP_LOGGER]
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(r'D:\home\projects\Website\app\templates'))
    setup_routes(subapp)

    app.add_subapp('/api/v1/', subapp)
