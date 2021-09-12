from sample_app.app import create_app
from ward import fixture
from mvc_flask import FlaskMVC


@fixture
def test_app():
    app = create_app()
    app.testing = True
    app.template_folder = "views"
    FlaskMVC(app, directory="sample_app")
    return app


@fixture
def test_client(app=test_app):
    app_contenxt = app.test_request_context()
    app_contenxt.push()

    return app.test_client()
