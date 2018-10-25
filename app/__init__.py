from flask import Flask,Blueprint
from flask_restful import Api

from instance.config import app_config
from connection import DbBase


my_db = DbBase()
def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])

    my_db.createTables()


    return app
