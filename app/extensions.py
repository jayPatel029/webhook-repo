# app/extensions.py

from pymongo import MongoClient
from config import MONGO_URI

#! Mongo configs (create a config.py and add a str MONGO_URI to run locally!!)
client = MongoClient(MONGO_URI)
# mongo: db & collection name
db = client.github_events
events_collection = db.events
