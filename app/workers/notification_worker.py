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
            await send_sms(data)
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

async def main():
    connection = await aio_pika.connect_robust(RABBITMQ_URL)
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
