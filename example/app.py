from flask import Flask
from mvc_flask import FlaskMVC

mvc = FlaskMVC()


def create_app():
    app = Flask(__name__)
    app.config["FLASK_MVC_DIR"] = "example"
    mvc.init_app(app)

    return app
