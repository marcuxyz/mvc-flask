from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_mvc import FlaskMVC

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"

    FlaskMVC(app, path="tests.app")
    db.init_app(app)

    return app
