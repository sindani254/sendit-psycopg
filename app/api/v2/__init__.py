from flask import Blueprint
from flask_restful import Api
from .views import V2_Orders


version2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version2)

api.add_resource(V2_Orders, '/v2_orders')
