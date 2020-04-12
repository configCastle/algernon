"""Write test file to mongodb."""

from pymongo import MongoClient

db = MongoClient().editor

db.file.insert_one(
    {
        'id': 0,
        'name': 'test_file',
        'data': ("{id: 0,type: 1,name: 'some name',data: [{"
                 "id: '_0',key: 'version',value: 3,required: true},"
                 "{id: '_1',key: 'services',value: [{id: '_1_0',key: 'redis',"
                 "value: [{id: '_1_0_0',key: 'build',value: '.'},{id: '_1_0_1',"
                 "key: 'port',value: 8080}]},{id: '_1_1',key: 'mongo',"
                 "value: [{id: '_1_1_0',key: 'user',value: ["
                 "{ id: '_1_1_0_0', value: 'l' },{ id: '_1_0_0_1', value: 'o' },"
                 "{ id: '_1_0_0_2', value: 'l' },]},{id: '_1_1_1',key: 'pass',"
                 "value: 'kek'}]}]}]}"),
        'configType': 'DOCKER_COMPOSE',
    },
)
