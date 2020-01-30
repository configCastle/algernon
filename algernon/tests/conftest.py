"""Fixture for pytests."""
import pytest
from aiohttp import web

from algernon.tests.init_test_db import init_test_mongo
from algernon.tests.views import view_test_mongo_input, view_test_mongo_output


@pytest.fixture
def init_app(loop, aiohttp_client):
    """
    Fixture of that tests.

    Args:
        loop: event_loop for fixture.
        aiohttp_client: simple client for fixture.

    Returns:
        loop for every test.
    """
    app = web.Application()

    db = loop.run_until_complete(init_test_mongo())
    app['db'] = db

    app.router.add_get('/output', view_test_mongo_output)
    app.router.add_post('/write', view_test_mongo_input)

    return loop.run_until_complete(aiohttp_client(app))
