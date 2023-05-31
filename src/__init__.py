from flask import Flask 
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

api = Api()
db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        api.init_app(app)
        db.init_app(app)

        @app.route("/create_db")
        def create_db():
            import src.models
            db.create_all()
            return "DataBase created!"

    return app

import src.routes