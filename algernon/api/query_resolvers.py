"""Query resolovers for API."""
from tartiflette import Resolver

from algernon.utils.db import return_all


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
        all objects in collections
    """
    db = ctx['req'].app['db']

    return await return_all(db, 'file')


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
    db = ctx['req'].app['db']

    for document in await return_all(db, 'file'):
        if document['id'] == args.get('id', None):
            return document

    return None
