"""Common views fot pytests."""
from aiohttp import web


async def view_test_mongo_input(request):
    """
    View of write some data in mongodb collection.

    Args:
        request: object of request in view.

    Returns:
        web.Response: response for client.
    """
    db = request.app['db']
    await db.pages.insert_one({'_id': '1', 'body': 'Eduard'})
    return web.Response(
        text='Thanks. Now Eduard in database',
        status=web.HTTPCreated.status_code,
    )


async def view_test_mongo_output(request):
    """
    View of get data from mongodb.

    Args:
        request: object of request in view.

    Returns:
        web.Response: response for client.
    """
    db = request.app['db']
    response = await db.pages.find_one({'_id': '1'})

    # after getting document - delete collection
    # if you know the best way - please, create pull request
    await db.pages.drop()

    return web.Response(text=response['body'], status=web.HTTPOk.status_code)
