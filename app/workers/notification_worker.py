import aio_pika
import json
import os
from app.services.email import send_email
from app.services.sms import send_sms_notification
from app.database import notifications_collection
import asyncio

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq/")

async def handle_notification(data):
    try:
        notif_type = data["type"]
        if notif_type == "email":
            await send_email(data)
        elif notif_type == "sms":
            await send_sms_notification(data)
        elif notif_type == "in-app":
            # Placeholder for in-app logic
            print(f"In-App: {data['message']}")
        await notifications_collection.update_one(
            {"_id": data["_id"]}, {"$set": {"status": "sent"}}
        )
    except Exception as e:
        print("Retrying failed notification:", e)
        await asyncio.sleep(2)
        await handle_notification(data)

async def connect_with_retry(url, retries=10, delay=5):
    for attempt in range(1, retries + 1):
        try:
            print(f"[Attempt {attempt}] Connecting to RabbitMQ...")
            return await aio_pika.connect_robust(url)
        except Exception as e:
            print(f"Connection failed: {e}")
            await asyncio.sleep(delay)
    raise ConnectionError("Could not connect to RabbitMQ after multiple attempts.")

async def main():
    connection = await connect_with_retry(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("notifications", durable=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    data = json.loads(message.body)
                    await handle_notification(data)

if __name__ == "__main__":
    asyncio.run(main())
