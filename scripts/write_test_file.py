"""Write test file to mongodb."""

from pymongo import MongoClient

db = MongoClient().editor

db.file.insert_one(
    {
        'id': 0,
        'name': 'test_file',
        'data': ('[{"key":"version","value":3,"required":true},{"key":'
                 '"services","value":[{"key":"redis","value":[{"key":"build",'
                 '"value":"."},{"key":"port","value":8080}]},{"key":"mongo",'
                 '"value":[{"key":"user","value":[{"value":"l"},{"value":"o"},'
                 '{"value":"l"}]},{"key":"pass","value":"kek"}]}]}]"'),
        'configType': 'DOCKER_COMPOSE',
    },
)
