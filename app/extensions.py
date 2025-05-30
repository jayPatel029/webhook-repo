# app/extensions.py

from pymongo import MongoClient
from config import MONGO_URI

# Mongo URI (adjust as needed)
client = MongoClient(MONGO_URI)
db = client.github_events
events_collection = db.events
