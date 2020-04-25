"""Module for mutation."""
from bson.objectid import ObjectId
from tartiflette import Resolver

from algernon.utils.db import return_last_id


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

    document = await db['file'].insert_one(
        {
            'id': file_id,
            'name': args['input']['name'],
            'data': args['input']['data'],
            'configType': args['input']['configType'],
        },
    )

    return await db['file'].find_one({'_id': ObjectId(document.inserted_id)})


@Resolver('Mutation.deleteFile')
async def resolve_mutation_delete_file(parent, args, ctx, system):
    """
    Resolve mutation deleteFile in GraphqQL API.

    Args:
        parent: initial field in 'execute' method
        args: argument for query
        ctx: context field
        system: information related to the execution

    Raises:
        Exception: If 'id' of document not found

    Returns:
        Removed document
    """
    db = ctx['req'].app['db']

    document = await db.file.find_one({'id': args['id']})

    if document is None:
        raise Exception('File does not exist.')

    db.file.delete_one({'id': args['id']})

    return document
