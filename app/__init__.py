from flask import Flask,Blueprint
from flask_restful import Api
from functools import wraps
from flask_jwt_extended import JWTManager

from instance.config import app_config
from connection import DbBase


my_db = DbBase()
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'mysecretkey code'
    jwt = JWTManager(app)

    
    def admin_required(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            if claims['roles'] != 'admin':
                return jsonify(message='Only Admin is allowed!'), 403
            else:
                return fn(*args, **kwargs)
        return wrapper

    @jwt.user_identity_loader
    def user_identity_lookup(logged_user):
        '''set token identity for logged_user'''
        return logged_user["email"]

    @jwt.user_claims_loader
    def add_claims_to_access_token(logged_user):
        '''This methods adds claims from logged_user'''
        return {'role': logged_user['role']}





    # register the apps Blueprint created in api/v1/views folder
    from .api.v2.views import app_v2
    app.register_blueprint(app_v2)

    my_db.createTables()
    my_db.create_store_owner()



    return app
