"""Module for database settings."""
from motor.motor_asyncio import AsyncIOMotorClient


async def init_db():
    """
    Initialize db and client of monngodb.

    Returns:
        AsyncIOMotorClient().editor: database for application
    """
    return AsyncIOMotorClient().editor
