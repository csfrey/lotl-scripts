from pymongo import MongoClient
from dotenv import load_dotenv

from random import randrange
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
db = client['lotl']

collections = [
    'adventures',
    'backgrounds',
    'classes',
    'feats',
    'magicItems',
    'monsters',
    'races',
    'retainers',
    'spells',
    'subclasses'
]

for name in collections:
    collection = db[name]
    collection.delete_many({"tag": "fake"})
    
client.close()