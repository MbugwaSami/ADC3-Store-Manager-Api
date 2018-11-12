from flask import Flask,Blueprint
from flask_restful import Api
from functools import wraps
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from instance.config import app_config
from connection import DbBase
from .api.v2.models.users import Users


my_db = DbBase()
def create_app(config_name):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'mysecretkey code'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
    jwt = JWTManager(app)



    @jwt.user_identity_loader
    def user_identity_lookup(logged_user):
        '''set token identity for logged_user'''
        return logged_user["email"]

    @jwt.user_claims_loader
    def add_claims_to_access_token(logged_user):
        '''This methods adds claims from logged_user'''
        return {'role': logged_user['role'],'user':logged_user['user_id']}

    @jwt.token_in_blacklist_loader
    def check_blacklist(decrypted_token):
        '''check if token is in black list'''
        json_token = decrypted_token['jti']
        revoked_tokens = Users()
        return revoked_tokens.check_blacklist(json_token)






    # register the apps Blueprint created in api/v1/views folder
    from .api.v2.views import app_v2
    app.register_blueprint(app_v2)

    my_db.createTables()
    my_db.create_store_owner()



    return app
