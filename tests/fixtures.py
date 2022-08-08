from tests.app import create_app
from ward import fixture


@fixture
def client():
    app = create_app()
    app.testing = True
    app_contenxt = app.test_request_context()
    app_contenxt.push()

    with app.test_client() as client:
        yield client
