from flask import Flask,Blueprint
from flask_restful import Api

from instance.config import app_config
from connection import DbBase


my_db = DbBase()
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])

    # register the apps Blueprint created in api/v1/views folder
    from .api.v2.views import app_v2
    app.register_blueprint(app_v2)

    my_db.createTables()
    my_db.create_store_owner()



    return app
