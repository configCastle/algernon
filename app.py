"""Main module."""
import asyncio
import os
import sys

import aiohttp_cors
from aiohttp import web
from tartiflette_aiohttp import register_graphql_handlers

from algernon.constants import standart_port
from algernon.routes import init_routes
from algernon.utils.db import init_db
from algernon.utils.strings import str_to_bool


def init_app() -> web.Application:
    """
    Initialize application, db for application and other.

    Returns:
        app: instance of application.
    """
    loop = asyncio.get_event_loop()
    db = loop.run_until_complete(init_db())
    app = web.Application()
    cors = aiohttp_cors.setup(app)
    app['db'] = db
    init_routes(app, cors)
    return app


def initialize_sdl():
    """
    Init sdl path.

    Returns:
        sdl path
    """
    return os.path.dirname(os.path.abspath(__file__)) + '/algernon/sdl'


def run() -> None:
    """Entry point for graphql server."""
    port = os.getenv('PORT', standart_port)
    graphiql = str_to_bool(os.getenv('GRAPHIQL', 'True'))

    web.run_app(
        register_graphql_handlers(
            app=init_app(),
            engine_sdl=initialize_sdl(),
            engine_modules=[
                'algernon.api.query_resolvers',
                'algernon.api.mutation_resolvers',
            ],
            executor_http_endpoint='/graphql',
            executor_http_methods=['POST'],
            graphiql_enabled=graphiql,
        ),
        port=port,
    )


if __name__ == '__main__':
    sys.exit(run())
