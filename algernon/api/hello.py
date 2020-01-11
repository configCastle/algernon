from aiohttp import web


class HelloAPI(web.View):
    async def hello(self, request):
        return web.Response(text='Hello, Client. Pay me with a minted coin.')

    async def get(self):
        return await self.hello(self.request)
