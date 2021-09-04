from example.app import create_app
from mvc_flask import FlaskMVC
from ward import fixture


@fixture
def test_client():
    app = create_app()
    app.testing = True
    app_contenxt = app.test_request_context()
    app_contenxt.push()

    return app.test_client()


@fixture
def test_app():
    app = create_app()
    app.testing = True

    return app
