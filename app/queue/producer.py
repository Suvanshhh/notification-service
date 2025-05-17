import os
import json
import aio_pika
from dotenv import load_dotenv

load_dotenv()

async def publish_notification(message: dict):
    connection = await aio_pika.connect_robust(os.getenv("RABBITMQ_URL"))
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("notifications", durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(message).encode()),
            routing_key=queue.name,
        )
