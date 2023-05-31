import pathlib

BASEDIR = pathlib.Path(__file__).parent

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    SECRET_KEY = "super secret key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASEDIR / "data" / "dev.db")


class DevelopmentConfig(Config):
    TESTING = False
    SECRET_KEY = "super secret key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + str(BASEDIR / "data" / "dev.db")
    DEBUG = True


class ProductionConfig(Config):
    pass

class TestingConfig(Config):
    TESTING = True


configs = {
    "dev": DevelopmentConfig,
    "product": ProductionConfig,
    "test": TestingConfig,
}
    