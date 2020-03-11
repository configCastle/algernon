"""Test for app.py."""
from aiohttp import web

from app import init_app


async def test_app():
    """Test init_app return web.Application instance."""
    isinstance(init_app, web.Application)
