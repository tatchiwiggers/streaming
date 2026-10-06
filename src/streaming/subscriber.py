import pika
from clickhouse_driver import Client
import uuid
import pytz
from datetime import datetime

def callback(ch, method, properties, body):
    client = Client('localhost')
    client.execute('USE salesDB')

    data = body.decode('utf-8').split(":")
    sale_id = uuid.UUID(data[0])
    amount = float(data[1])
    print(f"Received sale {sale_id} for ${amount}")
    utc_now = datetime.now(pytz.utc)
    query = 'INSERT INTO sales (sale_id, amount, timestamp) VALUES'
    values = [(sale_id, amount, utc_now)]
    client.execute(query, values)
