from faker import Faker
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from datetime import datetime

from random import randrange
import os

num_items = 30

load_dotenv()
fake = Faker()
client = MongoClient(os.getenv('MONGO_URI'))
db = client['lotl']

collection = db['adventures']
data = []
for _ in range(num_items):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
        
        'avgHoursToComplete': randrange(2, 7),
        'avgCharacters': randrange(3, 8),
        'avgLevel': randrange(1, 20)
    })
collection.insert_many(data)

collection = db['backgrounds']
data = []
for _ in range(num_items):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
    })
collection.insert_many(data)

collection = db['classes']
data = []
for _ in range(num_items):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
        
        'subclasses': ', '.join(fake.words(4)),
    })
collection.insert_many(data)

collection = db['feats']
data = []
for _ in range(num_items):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
    })
collection.insert_many(data)

collection = db['magicItems']
data = []
for _ in range(num_items):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
        
        'rarity': fake.word()
    })
collection.insert_many(data)

collection = db['monsters']
data = []
for _ in range(num_items):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
        
        'challenge': randrange(1, 10)
    })
collection.insert_many(data)

collection = db['races']
data = []
for _ in range(30):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
    })
collection.insert_many(data)

collection = db['retainers']
data = []
for _ in range(30):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
    })
collection.insert_many(data)

collection = db['spells']
data = []
for _ in range(30):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
        
        'level': randrange(1, 9),
        'schoolOfMagic': "evocation"
    })
collection.insert_many(data)

collection = db['subclasses']
data = []
for _ in range(30):
    data.append({
        'tag': 'fake',
        'name': fake.word(),
        'page': randrange(1, 300),
        'source': fake.word(),
        'summary': ' '.join(fake.sentences(4)),
        'createdBy': ObjectId('66cdd1acbbda499574c3577c'),
        'updatedBy': ObjectId('66cdd1acbbda499574c3577c'),
        'createdAt': datetime.now(),
        'updatedAt': datetime.now(),
        
        'parentClass': fake.word()
    })
collection.insert_many(data)

client.close()