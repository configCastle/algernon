"""Module for hello view."""
from aiohttp import web


class HelloAPI(web.View):
    """Class-based view for test main application."""

    async def hello(self, request):
        """
        Return text to client.

        Args:
            request: instance of request from client.

        Returns:
            web.Response: response for client.
        """
        return web.Response(text='Hello, Client. Pay me with a minted coin.')

    async def get(self):
        """
        Handle get-request from client.

        Returns:
            self.hello: view in this class.
        """
        return await self.hello(self.request)
