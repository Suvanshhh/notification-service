from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
client = AsyncIOMotorClient(MONGO_URI)
db = client["notifications"]

notifications_collection = db["notifications"]
users_collection = db["users"]  # Added users collection

# Optional: Create indexes
async def init_db():
    await notifications_collection.create_index([("user_id", ASCENDING)])
    await users_collection.create_index([("id", ASCENDING)], unique=True)  # unique user id index
