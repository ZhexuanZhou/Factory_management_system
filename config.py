import os


class Config(object):
    SECRET_KEY = "test"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:test@localhost/plant_management_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
