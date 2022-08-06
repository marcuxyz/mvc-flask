from flask import Flask
from mvc_flask import FlaskMVC


def create_app():
    app = Flask(__name__)
    FlaskMVC(app, path="tests.app")
    return app
