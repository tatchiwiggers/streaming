from clickhouse_driver import Client

def setup_db():
    client = Client('localhost')

    client.execute('CREATE DATABASE IF NOT EXISTS salesDB')
    client.execute('USE salesDB')
    client.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id UUID,
        amount Float64,
        timestamp DateTime
    ) ENGINE = MergeTree()
    ORDER BY timestamp
    ''')

if __name__ == '__main__':
    setup_db()
