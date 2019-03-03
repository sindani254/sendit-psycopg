from flask_restful import Resource
from flask import jsonify, make_response, request

from .models import V2_OrdersModel


class V2_Orders(Resource):
    """docstring for Orders"""

    def __init__(self):
        self.db = V2_OrdersModel()

    def post(self):
        data = request.get_json()
        item_name = data['item name']
        sender = data['sender']
        price = data['price']

        resp = self.db.save(item_name, sender, price)

        return make_response(
            jsonify(
                {
                    'Status': "Ok",
                    'Message': "order posted successfully",
                    'posted order': resp
                }
            ), 201
        )

    def get(self):
        orders = self.db.fetch_all_orders()
        if orders:
            return make_response(
                jsonify(
                    {
                        'Status': "ok",
                        'Message': "all orders fetched successfully",
                        'orders list': orders
                    }
                ), 200
            )
