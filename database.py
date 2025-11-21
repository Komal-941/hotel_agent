
from dotenv import load_dotenv 
from pymongo import MongoClient

import os


load_dotenv()


MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")


client = MongoClient(MONGO_URI)
db = client[DB_NAME]


menu_collection = db["menu"]
history_collection = db["history"]