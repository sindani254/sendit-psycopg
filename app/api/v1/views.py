from flask_restful import Resource
from flask import jsonify, make_response, request
from .models import OrdersModel
from flask_jwt import jwt_required


class SpecificOrder(Resource):
    """docstring for Orders"""

    def __init__(self):
        self.db = OrdersModel()

    @jwt_required()
    def get(self, id):
        return self.db.get_order_by_id(id)


class OrdersList(Resource):

    def __init__(self):
        self.db = OrdersModel()

    def post(self):
        data = request.get_json(force=True)
        item_name = data['item name']
        sender = data['sender']
        price = data['price']
        status = data['current status']

        search_item = self.db.get_order_by_name(data['item name'])
        if search_item:
            return make_response(
                jsonify(
                    {
                        'msg': "entry already exists"
                    }
                )
            )
        else:
            resp = self.db.save(item_name, sender, price, status)

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
        orders = self.db.get_all_orders()
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
        else:
            return make_response(
                jsonify(
                    {
                        'Status': "ok",
                        'Message': "0 orders found"
                    }
                )
            )


class ManageOrders(Resource):
    """docstring for ManageOrders"""

    def __init__(self):
        self.db = OrdersModel()

    def delete(self, id):
        item_to_delete = self.db.get_order_by_id(id)
        if item_to_delete is None:
            return make_response(
                jsonify(
                    {
                        'Message': "order NOT found"
                    }
                )
            )
        return self.db.delete_item(id)


class UpdateOrder(Resource):
    """docstring for UpdateOrder"""

    def __init__(self):
        self.db = OrdersModel()

    def put(self, id):
        order_status = self.db.get_order_by_id(id)
        return order_status
