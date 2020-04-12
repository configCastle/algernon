"""Module for database settings."""
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
    return AsyncIOMotorClient().editor


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
