import os
import psycopg2
from werkzeug.security import generate_password_hash

from instance.config import app_config


enviroment = os.environ['ENVIRONMENT']
class Models(object):
    """This class has shared methods and attributes in all model class"""
    def __init__(self):
        self.conn = psycopg2.connect(app_config[enviroment].connectionVariables)
        self.cur = self.conn.cursor()
