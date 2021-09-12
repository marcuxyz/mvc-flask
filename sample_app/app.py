from flask import Flask
from mvc_flask import FlaskMVC


def create_app():
    app = Flask(__name__)
    return app


if __name__ == "__main__":
    app = create_app()
    app.template_folder = "views"
    FlaskMVC(app, ".")
    app.run()
