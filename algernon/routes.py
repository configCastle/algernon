"""Module for algernon routes."""
from algernon.api.hello import HelloAPI


def init_routes(app):
    """
    Initialize view and it route.

    Args:
        app: instance of application.
    """
    app.router.add_view('/hello', HelloAPI)
