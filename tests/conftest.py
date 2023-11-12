import pytest
from splinter import Browser

from tests.app import create_app
from tests.app import db


def test_client():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()
    return app


@pytest.fixture
def client():
    app = test_client()

    with app.test_client() as client:
        db.create_all()

        yield client

        db.session.remove()
        db.drop_all()


@pytest.fixture
def browser():
    app = test_client()

    with app.test_client():
        db.create_all()

        yield Browser("flask", app=app)

        db.session.remove()
        db.drop_all()
