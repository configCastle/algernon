"""Module for database settings."""
import os

from motor.motor_asyncio import AsyncIOMotorClient

from algernon.constants import mongo_port
from algernon.utils.docker_runtime import in_docker


async def init_db():
    """
    Initialize db and client of monngodb.

    Returns:
        AsyncIOMotorClient().editor: database for application
    """
    if in_docker():
        return AsyncIOMotorClient('mongo_algernon', mongo_port).editor

    mongo_uri = os.getenv('MONGO_URI')

    if mongo_uri is None:
        return AsyncIOMotorClient().editor

    return AsyncIOMotorClient(mongo_uri).editor


async def return_all(db, collection):
    """
    Return all object in collection.

    Args:
        db: object of database
        collection: name of collection

    Returns:
        all object in collections
    """
    cursor = db[collection].find()
    documents = []

    async for document in cursor:
        documents.append(document)

    return documents


async def return_last_id(db, collection):
    """
    Return last id in collection.

    Args:
        db: instance of database
        collection: name of collection

    Returns:
        last id in collection
    """
    documents = await return_all(db, collection)
    document_ids = [document_id['id'] for document_id in documents]

    return max(document_ids, default=-1)
