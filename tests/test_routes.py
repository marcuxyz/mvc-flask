from ward import test, expect
from tests.fixtures import test_app, test_client


@test("contains routes")
def _(app=test_app):
    routes = [route.rule for route in app.url_map.iter_rules()]

    expect.assert_in("/contact", routes, None)
    expect.assert_in("/", routes, None)


@test("contains endpoints")
def _(app=test_app):
    endpoints = [route.endpoint for route in app.url_map.iter_rules()]

    expect.assert_in("home.index", endpoints, None)
    expect.assert_in("contact.index", endpoints, None)


@test("contains methods")
def _(app=test_app):
    methods = [
        route
        for routes in app.url_map.iter_rules()
        for route in routes.methods
    ]

    expect.assert_equal(methods.count("GET"), 3, None)


@test("must contains text")
def _(client=test_client):
    res = client.get("/")

    expect.assert_equal(res.status_code, 200, None)
    expect.assert_in("Hello, World!", res.get_data(as_text=True), None)


@test("must contains text")
def _(client=test_client):
    res = client.get("/contact")

    expect.assert_equal(res.status_code, 200, None)
    expect.assert_in("Contact page", res.get_data(as_text=True), None)
