orders = []


class OrdersModel():
    """docstring for OrdersModel"""

    def __init__(self):
        self.db = orders

    def get_all_orders(self):
        return self.db

    def get_order_status(self):
        for order in self.db:
            if order:
                order['current status'] = "cancelled"
                return order, 200 if order else 400
            else:
                return {'error': "order NOT found!"}

    def get_order_by_name(self, name):
        for item in self.db:
            if item['item name'] == name:
                return item, 200 if item else 400

    def get_order_by_id(self, id):
        item = next(filter(lambda x: x['id'] == id, self.db), None)
        if item:
            return {'order details': item}, 200
        else:
            return {'msg': "item NOT found!"}, 404

    def save(self, item_name, sender, price, status):
        data = {
            'id': len(self.db) + 1,
            'item name': item_name,
            'sender': sender,
            'item price': price,
            'current status': status
        }

        self.db.append(data)

        return self.db

    def delete_item(self, id):
        global orders
        order_to_delete = next(filter(lambda x: x['id'] == id, self.db), None)
        if order_to_delete:
            orders = list(filter(lambda x: x['id'] != id, self.db))
            return {'msg': "order with id '{}' deleted successfull".format(id)}, 400
        return {'error': 'order NOT found'}
