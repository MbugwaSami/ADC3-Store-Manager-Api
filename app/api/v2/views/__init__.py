from flask import Blueprint
from flask_restful import Api, Resource

# import the endpoint classes
from .users_endpoint import UsersApi

# create the app Blueprint
app_v2 = Blueprint('app_v1',__name__, url_prefix="/api/v2")
api_v2 = Api(app_v2)

api_v2.add_resource(UsersApi,'/users')
