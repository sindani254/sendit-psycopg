import os

from flask import Flask
from app.api.v1 import version_one as v1
from app.api.v2 import version2 as v2
from flask_restful import Api

from flask_jwt import JWT
from app.api.v1.auth.security import authenticate, identity

from app.api.v1.views import OrdersList, SpecificOrder, ManageOrders, UpdateOrder
from app.api.v2.views import V2_Orders


app = Flask(__name__)
app.register_blueprint(v1)
app.register_blueprint(v2)

app.config.from_object(os.environ['APP_SETTINGS'])
app.secret_key = "@nonymous"
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

db = os.getenv('DB_URL')


api.add_resource(OrdersList, '/orders')
api.add_resource(SpecificOrder, '/orders/<int:id>')
api.add_resource(ManageOrders, '/orders/<int:id>/delete')
api.add_resource(UpdateOrder, '/orders/<int:id>/update')
api.add_resource(V2_Orders, '/v2_orders')
