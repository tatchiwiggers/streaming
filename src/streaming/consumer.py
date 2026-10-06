from datetime import datetime
from uuid import UUID

import pika
from clickhouse_driver import Client

client = Client('localhost')


def callback(ch, method, properties, body):
    sale_id, amount = body.decode().split(':')
    client.execute(
        'INSERT INTO salesDB.sales (sale_id, amount, timestamp) VALUES',
        [(UUID(sale_id), float(amount), datetime.now())]
    )
    print(f"Inserted {sale_id}: {amount}")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='sales', durable=True)

    channel.basic_consume(queue='sales', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
