"""Tests for check write/output of mongo."""
from aiohttp import web


async def test_insert(init_app):
    """
    Test: insert some data in mongodb to request to route /write.

    Args:
        init_app: fixture for test
    """
    response = await init_app.post('/write')
    assert response.status == web.HTTPCreated.status_code
    assert await response.text() == 'Thanks. Now Eduard in database'


async def test_output(init_app):
    """
    Test: get some data from mongodb to request to route /output.

    Args:
        init_app: fixture for test.
    """
    response = await init_app.get('/output')
    assert response.status == web.HTTPOk.status_code
    assert await response.text() == 'Eduard'
