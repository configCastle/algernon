"""Write service data to mongodb."""

from pymongo import MongoClient

db = MongoClient().editor

db.service.insert_one(
    {
        '_id': '0',
        'name': 'redis',
        'data': 'some_data',
    },
)

db.service.insert_one(
    {
        '_id': '1',
        'name': 'postgres',
        'data': 'some_data',
    },
)

db.service.insert_one(
    {
        '_id': '2',
        'name': 'node',
        'data': 'some_data',
    },
)
