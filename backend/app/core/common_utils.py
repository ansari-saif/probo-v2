import asyncio
import json
import pika
from app.core.constraints import RABBITMQ_HOST, RABBITMQ_PASSWORD, RABBITMQ_USERNAME, RABBITMQ_PORT


def publish_queue(data, queue_name):
    RABBITMQ_CONNECTION = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_HOST, int(RABBITMQ_PORT),
                                  RABBITMQ_USERNAME,
                                  pika.PlainCredentials(RABBITMQ_USERNAME,
                                                        RABBITMQ_PASSWORD)))
    RABBITMQ_CHANNEL = RABBITMQ_CONNECTION.channel()
    RABBITMQ_CHANNEL.basic_publish(exchange='', routing_key=queue_name,
                                   body=json.dumps(data, default=str).encode('utf-8'))
    RABBITMQ_CONNECTION.close()



async def subscribe_queue(user_id):
    RABBITMQ_CONNECTION = pika.BlockingConnection(
        pika.ConnectionParameters(
            RABBITMQ_HOST, int(RABBITMQ_PORT),
            RABBITMQ_USERNAME,
            pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        )
    )
    RABBITMQ_CHANNEL = RABBITMQ_CONNECTION.channel()
    
    # Create an asyncio queue to hold messages received by the callback
    message_queue = asyncio.Queue()
    loop = asyncio.get_event_loop()

    def callback(ch, method, properties, body):
        try:
            requested_data = json.loads(body.decode("utf-8"))
            # Use loop.call_soon_threadsafe to put the data into the async queue from the pika thread
            loop.call_soon_threadsafe(message_queue.put_nowait, requested_data)
        except Exception as e:
            print(f"Error: {e}")

    RABBITMQ_CHANNEL.basic_consume(queue="orderbook_queue_acknowledgment", on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    
    # Start consuming in a separate thread since pika's start_consuming is blocking
    asyncio.get_event_loop().run_in_executor(None, RABBITMQ_CHANNEL.start_consuming)

    # Wait and retrieve the message from the queue
    requested_data = await message_queue.get()
    return requested_data