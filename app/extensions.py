# app/extensions.py

from pymongo import MongoClient
# from config import MONGO_URI
from dotenv import load_dotenv
import os

load_dotenv()

#! Mongo configs (create a .env and add a str MONGO_URI to run locally!!)
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
# mongo: db & collection name
db = client.github_events
events_collection = db.events
