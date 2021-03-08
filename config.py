import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "hey"


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False


class StagingConfig(Config):
    ENV = "staging"
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql:///wordcount_dev"


class TestingConfig(Config):
    ENV = "testing"
    TESTING = True
