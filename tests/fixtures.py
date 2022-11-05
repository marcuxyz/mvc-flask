from tests.app import create_app
from ward import fixture
from splinter import Browser


@fixture
def app_context():
    app = create_app()
    app.testing = True
    app_contenxt = app.test_request_context()
    app_contenxt.push()
    return app


@fixture
def client(app_context=app_context):
    with app_context.test_client() as client:
        yield client


@fixture
def browser(app_context=app_context):
    with app_context.test_client():
        yield Browser("flask", app=app_context)
