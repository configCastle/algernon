"""Write test file to mongodb."""

from pymongo import MongoClient

db = MongoClient().editor

db.file.insert_one(
    {
        'id': 0,
        'name': 'test_file',
        'data': '[]',
        'configType': 'DOCKER_COMPOSE',
    },
)
