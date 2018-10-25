import os

class Config(object):
    "parent configuration class"
    DEBUG= False



class DevelopmentConfig(Config):
    "Configurations for Development"
    DEBUG = True
    connectionVariables="dbname='store-manager' user='postgres' password='mwoboko10@' host='localhost' port='5432'"
    os.environ['ENV']='testing'

class TestingConfig(Config):
    """Configurations for Testing,"""
    TESTING = True
    DEBUG = True
    connectionVariables="dbname='store-manager-test' user='postgres' host='localhost' port='5432'"
    os.environ['ENV']='development'

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    os.environ['ENV']='staging'


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    os.environ['ENV']='production'


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}