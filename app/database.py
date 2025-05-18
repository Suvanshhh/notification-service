# app/database.py

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

# Get Mongo URI from environment (provided by Railway plugin or .env)
MONGO_URI = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

# Initialize client and DB
client = AsyncIOMotorClient(MONGO_URI)
db = client["notifications"]

# Define collections
notifications_collection = db["notifications"]
users_collection = db["users"]

# Optional: Create indexes
async def init_db():
    await notifications_collection.create_index([("user_id", ASCENDING)])
    await users_collection.create_index([("id", ASCENDING)], unique=True)
