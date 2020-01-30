"""Main module."""
import asyncio

from aiohttp import web

from algernon.routes import init_routes
from algernon.utils.db import init_db


def init_app() -> web.Application:
    """
    Initialize application, db for application and other.

    Returns:
        app: instance of application.
    """
    loop = asyncio.get_event_loop()
    db = loop.run_until_complete(init_db())
    app = web.Application()
    app['db'] = db
    init_routes(app)
    return app


if __name__ == '__main__':
    web.run_app(init_app())
