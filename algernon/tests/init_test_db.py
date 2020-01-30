"""Module for settings mongodb for tests."""
from motor.motor_asyncio import AsyncIOMotorClient


async def init_test_mongo():
    """
    Initialize of test db.

    Returns:
        AsyncIOMotorClient client of database test
    """
    return AsyncIOMotorClient().test
