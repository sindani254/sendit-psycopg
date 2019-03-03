import os
import psycopg2
import psycopg2.extras


class V2_OrdersModel():
    """docstring for OrdersOperations"""

    def __init__(self):
        self.db = os.getenv('DB_URL')

    def save(self, item_name, sender, price):
        data = {
            'item name': item_name,
            'sender': sender,
            'price': price
        }

        connection = psycopg2.connect(self.db)
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        query = "INSERT INTO orders (item_name, sender, price) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['item name'], data['sender'], data['price']))

        connection.commit()
        connection.close()

        return {'msg': "data inserted"}

    def fetch_all_orders(self):
        connection = psycopg2.connect(self.db)
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        query = "SELECT * FROM orders ORDER BY id ASC"
        cursor.execute(query)
        all_orders = cursor.fetchall()
        connection.close()
        return all_orders
