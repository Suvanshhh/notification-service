from pydantic import BaseModel, Field, EmailStr
from typing import Literal

class Notification(BaseModel):
    user_id: str = Field(..., example="user123")
    type: Literal["email", "sms", "in-app"]
    subject: str
    message: str

class NotificationInDB(Notification):
    status: str = "queued"

class User(BaseModel):
    id: str = Field(..., example="user123")
    name: str = Field(..., example="John Doe")
    email: EmailStr = Field(..., example="john.doe@example.com")
    phone: str = Field(..., example="+1234567890")
