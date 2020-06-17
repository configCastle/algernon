"""Module for mutation."""
from bson.objectid import ObjectId
from tartiflette import Resolver

from algernon.utils.db import returl_all_id, return_last_id
from algernon.utils.token import check_token


@Resolver('Mutation.createFile')
async def resolve_mutation_create_file(parent, args, ctx, system):
    """
    Resolve mutation createFile in GraphqQL API.

    Args:
        parent: initial field in 'execute' method
        args: argument for query
        ctx: context field
        system: information related to the execution

    Raises:
        Exception: raise if id user does not exist

    Returns:
        return created document
    """
    access_token = ctx['req'].headers.get('Authorization', None)
    await check_token(access_token)

    db = ctx['req'].app['db']

    file_id = await return_last_id(db, 'file') + 1
    user_id = args['input']['user']

    if user_id not in await returl_all_id(db, 'user'):
        raise Exception('User does not exist.')

    document = await db['file'].insert_one(
        {
            'id': file_id,
            'name': args['input']['name'],
            'data': args['input']['data'],
            'user': user_id,
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
    access_token = ctx['req'].headers.get('Authorization', None)
    await check_token(access_token)

    db = ctx['req'].app['db']

    document = await db.file.find_one({'id': args['id']})

    if document is None:
        raise Exception('File does not exist.')

    db.file.delete_one({'id': args['id']})

    return document


@Resolver('Mutation.updateFile')
async def resolve_mutation_update_file(parent, args, ctx, system):
    """
    Resolve mutation updateFile in GraphqQL API.

    Args:
        parent: initial field in 'execute' method
        args: argument for query
        ctx: context field
        system: information related to the execution

    Raises:
        Exception: If 'id' of document not found
        Exception: If new data not input

    Returns:
        Updated document
    """
    await check_token(ctx['req'].headers.get('Authorization', None))

    db = ctx['req'].app['db']

    args_input = args['input']

    doc_base = {
        'name': None,
        'configType': None,
        'data': None,
    }

    doc_base['name'] = args_input.get('name')
    doc_base['configType'] = args_input.get('configType')
    doc_base['data'] = args_input.get('data')

    if all(file_value is None for file_value in doc_base.values()):
        raise Exception(
            "You should provide at least one value: 'name'" +
            "'type' or 'data'",
        )

    doc_base = {
        key: input_value for key, input_value in doc_base.items()
        if input_value is not None
    }

    if await db.file.find_one({'id': args_input['id']}) is None:
        raise Exception('File does not exist.')

    await db.file.update_one(
        {'id': args_input['id']},
        {'$set': doc_base},
    )

    return await db.file.find_one({'id': args_input['id']})
