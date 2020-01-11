from aiohttp import web

from routes import init_routes


def init_app() -> web.Application:
    app = web.Application()
    init_routes(app)
    return app


if __name__ == '__main__':
    web.run_app(init_app())
