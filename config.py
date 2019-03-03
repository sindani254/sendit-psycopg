import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '@nonymous'
    DATABASE_URL = os.environ['DB_URL']


class DevConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
