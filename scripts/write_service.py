"""Write service data to mongodb."""

from pymongo import MongoClient

db = MongoClient().editor

db.service.insert_one(
    {
        'id': 0,
        'name': 'redis',
        'data': ('{"key":"redis","value":[{"key":"build","value":"."},'
                 '{"key":"port","value":8080}]}'),
    },
)

db.service.insert_one(
    {
        'id': 1,
        'name': 'mongo',
        'data': ('{"key":"mongo","value":[{"key":"build","value":"."},'
                 '{"key":"port","value":8080}]}'),
    },
)
