"""Module for mutation."""
from tartiflette import Resolver

from algernon.utils.db import return_all, return_last_id


@Resolver('Mutation.createFile')
async def resolve_mutation_create_file(parent, args, ctx, system):
    """
    Resolve mutation createFile in GraphqQL API.

    Args:
        parent: initial field in 'execute' method
        args: argument for query
        ctx: context field
        system: information related to the execution

    Returns:
        return created document
    """
    db = ctx['req'].app['db']

    file_id = await return_last_id(db, 'file') + 1

    db['file'].insert_one(
        {
            'id': file_id,
            'name': args['input']['name'],
            'data': args['input']['data'],
            'configType': args['input']['configType'],
        },
    )

    for document in await return_all(db, 'file'):
        if document['id'] == file_id:
            return document
