from aiohttp import web

from app.core.constants.app import APP_LOGGER, APP_DATABASE_CLIENT
from .routes import setup_routes


def setup(app: web.Application) -> None:
    subapp = web.Application()

    # subapp[APP_DATABASE_CLIENT] = app[APP_DATABASE_CLIENT]
    # subapp[APP_LOGGER] = app[APP_LOGGER]

    setup_routes(subapp)

    app.add_subapp('/api/v1/', subapp)
