from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING
import os

MONGO_URI = os.getenv("MONGODB_URI")

client = AsyncIOMotorClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=3000,
    retryWrites=True
)
db = client["notifications"]


notifications_collection = db["notifications"]
users_collection = db["users"]

async def init_db():
    await notifications_collection.create_index([("user_id", ASCENDING)])
    await users_collection.create_index([("id", ASCENDING)], unique=True)
