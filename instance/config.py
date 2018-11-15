import os

class Config(object):
    "parent configuration class"
    DEBUG= True
    SECRET_KEY = "Just write nothing that is not easy for not guessing"



class DevelopmentConfig(Config):
    "Configurations for Development"
    DEBUG = True
    connectionVariables="dbname='Database_store' user='postgres' password='Mwoboko10@' host='localhost' port='5432'"
    os.environ['ENVIRONMENT']='development'

class TestingConfig(Config):
    """Configurations for Testing,"""
    TESTING = True
    DEBUG = True
    connectionVariables="dbname='store_manager_test' password='Mwoboko10@' user='postgres' host='localhost' port='5432'"
    os.environ['ENVIRONMENT']='testing'


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
