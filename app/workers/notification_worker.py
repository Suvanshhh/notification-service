import os
from dotenv import load_dotenv
load_dotenv()

import asyncio, json
from app.models import Notification
from app.database import engine, AsyncSessionLocal
from app.utils.notifier import send_email, send_sms, send_inapp
from sqlalchemy import update
import aio_pika

MAX_RETRIES = 3
RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@127.0.0.1:5672/")

print("RABBITMQ_URL:", RABBITMQ_URL)  # DEBUG LINE

async def consume():
    conn = await aio_pika.connect_robust(RABBITMQ_URL)
    channel = await conn.channel()
    queue = await channel.declare_queue("notifications", durable=True)

    async with engine.begin() as conn:
        await conn.run_sync(Notification.metadata.create_all)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process():
                data = json.loads(message.body.decode())
                await process_notification(data)

async def process_notification(data):
    session = AsyncSessionLocal()
    try:
        notification = Notification(
            user_id=data["user_id"],
            type=data["type"],
            subject=data.get("subject", ""),
            message=data["message"],
        )
        session.add(notification)
        await session.commit()

        if data["type"] == "email":
            await send_email(data["subject"], data["message"], data["user_id"])
        elif data["type"] == "sms":
            await send_sms(data["message"], data["user_id"])
        elif data["type"] == "inapp":
            await send_inapp(data["user_id"], data["message"])

        await session.execute(
            update(Notification).where(Notification.id == notification.id).values(status="sent")
        )
        await session.commit()

    except Exception as e:
        print("Failed:", e)
        await session.execute(
            update(Notification).where(Notification.id == notification.id).values(status="failed", retry_count=1)
        )
        await session.commit()
    finally:
        await session.close()

if __name__ == "__main__":
    asyncio.run(consume())
