from fastapi import APIRouter, HTTPException
from app.models import Notification, NotificationInDB, User
from app.queue.producer import publish_notification
from app.database import notifications_collection, users_collection  # users_collection added
from bson import ObjectId

router = APIRouter()

# --- Notification routes ---

@router.post("/notifications")
async def send_notification(notification: Notification):
    notif_dict = notification.dict()
    notif_dict["status"] = "queued"
    result = await notifications_collection.insert_one(notif_dict)
    notif_dict["_id"] = str(result.inserted_id)
    await publish_notification(notif_dict)
    return {"status": "queued", "notification_id": notif_dict["_id"]}

@router.get("/users/{user_id}/notifications")
async def get_user_notifications(user_id: str):
    cursor = notifications_collection.find({"user_id": user_id})
    notifications = []
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        notifications.append(doc)
    if not notifications:
        raise HTTPException(status_code=404, detail="No notifications found.")
    return notifications

# --- User routes with MongoDB ---

@router.post("/users")
async def create_user(user: User):
    existing_user = await users_collection.find_one({"id": user.id})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    user_dict = user.dict()
    await users_collection.insert_one(user_dict)
    return {"message": "User created successfully", "user": user}

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    user_doc = await users_collection.find_one({"id": user_id})
    if not user_doc:
        raise HTTPException(status_code=404, detail="User not found")
    # Remove _id ObjectId before returning
    user_doc.pop("_id", None)
    return user_doc
