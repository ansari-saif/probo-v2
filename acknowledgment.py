import json
import os

import pika

# RabbitMQ connection details
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_QUEUE = "orderbook_queue_acknowledgment"
RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT = 5672
USER_MAP = {}
EVENT_MAP = {}
STOCK_BALANCE_MAP = {}
DEBUG = 0
from websocket import create_connection


def consumer(body):
    ws = create_connection("ws://localhost:8080")
    data_to_send = {
        "event":"message",
        "room":"test",
        "message":body
    }
    ws.send(json.dumps(data_to_send))
    ws.close()


input_data = {}


def main():

    if DEBUG:
        consumer(input_data)
    else:
        RABBITMQ_CONNECTION = pika.BlockingConnection(
            pika.ConnectionParameters(RABBITMQ_HOST, int(RABBITMQ_PORT),
                                      RABBITMQ_USERNAME,
                                      pika.PlainCredentials(RABBITMQ_USERNAME,
                                                            RABBITMQ_PASSWORD)))
        RABBITMQ_CHANNEL = RABBITMQ_CONNECTION.channel()

        def callback(ch, method, properties, body):
            try:
                requested_data = json.loads(body.decode("utf-8"))
                consumer(requested_data)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as E:
                ch.basic_ack(delivery_tag=method.delivery_tag)
                error_text = str(E)
                print(error_text)

        RABBITMQ_CHANNEL.basic_consume(
            queue=RABBITMQ_QUEUE, on_message_callback=callback)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        RABBITMQ_CHANNEL.start_consuming()


if __name__ == '__main__':
    main()
