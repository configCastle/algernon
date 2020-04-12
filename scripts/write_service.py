"""Write service data to mongodb."""

from pymongo import MongoClient

db = MongoClient().editor

db.service.insert_one(
    {
        'id': 0,
        'name': 'redis',
        'data': ("{id: '_1_0',key: 'redis',value: [{id: '_1_0_0',"
                 "key: 'build',value: '.'},{id: '_1_0_1',key: 'port',"
                 "value: 8080}]}"),
    },
)

db.service.insert_one(
    {
        'id': 1,
        'name': 'mongo',
        'data': ("{id: '_1_0',key: 'mongo',value: [{id: '_1_0_0',"
                 "key: 'build',value: '.'},{id: '_1_0_1',key: 'port',"
                 "value: 8080}]}"),
    },
)
