
from flask import Blueprint
from flask_restful import Api
from .views import OrdersList, SpecificOrder, ManageOrders, UpdateOrder

version_one = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api = Api(version_one)


api.add_resource(OrdersList, '/orders')
api.add_resource(ManageOrders, '/orders/<int:id>/delete')
api.add_resource(UpdateOrder, '/orders/<int:id>/update')
api.add_resource(SpecificOrder, '/orders/<int:id>')
