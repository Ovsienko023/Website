import asyncio

from aiohttp import web
from app.api.http.setup import setup as setup_api_v1
from app.core.constants.container import C_CONFIG, C_LOGGER, C_DATABASE_CLIENT
from app.core.constants.app import APP_LOGGER, APP_DATABASE_CLIENT
from app.core.tools import get_config
from app.core import logger


async def init_app(container) -> web.Application:
    app = web.Application()
    app.on_cleanup.append(close_database)

    app[APP_LOGGER] = container[C_LOGGER]
    # app[APP_DATABASE_CLIENT] = container[C_DATABASE_CLIENT]

    setup_api_v1(app)

    return app


def main() -> None:
    # lgr = logger.get_logger()
    # licenses.set_first_license_upd(True)
    # installtools.set_installing(False)
    config = get_config()
    lgr = logger.get_logger()

    container = {
        C_CONFIG: config,
        C_LOGGER: lgr,
        # DI_DATABASE_CLIENT: MCUDatabaseManager(
        #     host=config['db']['host'],
        #     port=config['db']['port'],
        #     user=config['db']['username'],
        #     password=config['db']['password'],
        #     database=config['db']['dbname']
        # )
    }

    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app(container))

    web.run_app(app, host='127.0.0.1', port=config["webapi"]["port"], access_log=lgr)


async def close_database(app: web.Application):
    # pool: MCUDatabaseManager = app[APP_DATABASE_CLIENT]
    # await pool.close()
    pass
