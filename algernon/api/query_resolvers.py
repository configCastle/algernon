"""Query resolovers for API."""
from tartiflette import Resolver

from algernon.utils.db import return_all, return_files_by_user
from algernon.utils.token import check_token


@Resolver('Query.services')
async def resolve_query_services(parent, args, ctx, system):
    """
    Resolve all services.

    Args:
        parent: initial field in 'execute' method
        args: argument for query
        ctx: context field
        system: information related to the execution

    Returns:
        all objects in collections
    """
    db = ctx['req'].app['db']

    return await return_all(db, 'service')


@Resolver('Query.service')
async def resolve_query_service(parent, args, ctx, system):
    """
    Resolve one service.

    Args:
        parent: initial field in 'execute' method
        args: argument for query
        ctx: context field
        system: information related to the execution

    Returns:
        one service
    """
    db = ctx['req'].app['db']

    for document in await return_all(db, 'service'):
        if document['id'] == args['id']:
            return document
    return None


@Resolver('Query.files')
async def resolve_query_files(parent, args, ctx, system):
    """
    Resolve all files in system.

    Args:
        parent: initial field in 'execute' method
        args: argument for query
        ctx: context field
        system: information related to the execution

    Returns:
        all objects in collections by user
    """
    access_token = ctx['req'].headers.get('Authorization', None)
    await check_token(access_token)

    db = ctx['req'].app['db']
    user_id = args.get('user')

    return await return_files_by_user(db, user_id)


@Resolver('Query.file')
async def resolve_query_file(parent, args, ctx, system):
    """
    Resolve one file.

    Args:
        parent: initial field in 'execute' method
        args: argument for query
        ctx: context field
        system: information related to the execution

    Returns:
        one file
    """
    access_token = ctx['req'].headers.get('Authorization', None)
    await check_token(access_token)
    db = ctx['req'].app['db']

    for document in await return_all(db, 'file'):
        if document['id'] == args.get('id', None):
            return document

    return None
