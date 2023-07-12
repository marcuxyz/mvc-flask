from tests.app import create_app
from ward import fixture
from splinter import Browser
from tests.app import db


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
        db.create_all()

        yield client

        db.session.remove()
        db.drop_all()


@fixture
def browser(app_context=app_context):
    with app_context.test_client():
        db.create_all()

        yield Browser("flask", app=app_context)

        db.session.remove()
        db.drop_all()
