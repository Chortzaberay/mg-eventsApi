import pathlib
import os

BASEDIR = pathlib.Path(__file__).parent

DB_PASS = os.environ.get("DB_PASS")
DB_USER = os.environ.get("DB_USER")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = "localhost"
DB_PORT = "5432"

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
    SECRET_KEY = "09a097bb73f1d6d0320c13191147f97fbdffd17aa6a20ca41c155ee6a3370cbc"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

configs = {
    "dev": DevelopmentConfig,
    "product": ProductionConfig,
    "test": TestingConfig,
}
    