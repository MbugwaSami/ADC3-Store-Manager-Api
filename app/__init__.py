from flask import Flask,Blueprint
from flask_restful import Api

from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])


    return app
