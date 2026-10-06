import pika
import random
import uuid
import time
import random

def publish_random_sales():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='sales', durable=True)
    try:
        while True:
            sale_id = uuid.uuid4()
            amount = round(random.uniform(10.0, 200.0), 2)
            message = f"{sale_id}:{amount}"
            channel.basic_publish(exchange='', routing_key='sales', body=message)
            time.sleep(random.random())
    finally:
        connection.close()

if __name__ == '__main__':
    publish_random_sales()
