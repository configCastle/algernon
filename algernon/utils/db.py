"""Module for database settings."""
from motor.motor_asyncio import AsyncIOMotorClient

from algernon.constants import mongo_port


async def init_db():
    """
    Initialize db and client of monngodb.

    Returns:
        AsyncIOMotorClient().editor: database for application
    """
    return AsyncIOMotorClient('mongo_algernon', mongo_port).editor


async def return_all(db):
    """
    Return all object in collection.

    Args:
        db: object of database

    Returns:
        all object in collections
    """
    cursor = db.service.find()
    services = []

    async for document in cursor:
        services.append(document)

    return services
