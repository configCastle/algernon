"""Module for algernon routes."""
import aiohttp_cors

from algernon.api.hello import HelloAPI


def init_routes(app, cors):
    """
    Initialize view and it route.

    Args:
        app: instance of application
        cors: instalce of cors setting application
    """
    app.router.add_view('/hello', HelloAPI)

    cors.add(app.router.add_resource('/graphql'), {
        '*': aiohttp_cors.ResourceOptions(
            expose_headers='*',
            allow_headers='*',
            allow_credentials=True,
            allow_methods=['POST', 'GET'],
        ),
    })
