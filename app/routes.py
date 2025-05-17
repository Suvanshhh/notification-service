from fastapi import APIRouter
from pydantic import BaseModel
from app.queue.producer import publish_notification

router = APIRouter()

class Notification(BaseModel):
    user_id: str
    type: str
    subject: str
    message: str

@router.post("/notifications")
async def send_notification(notification: Notification):
    await publish_notification(notification.dict())
    return {"status": "queued"}
