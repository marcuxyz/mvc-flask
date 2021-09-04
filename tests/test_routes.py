from ward import test, expect, skip
from fixtures import test_app


@test("contains routes")
def _(app=test_app):
    routes = [route.rule for route in app.url_map.iter_rules()]

    expect.assert_in("/contact", routes, None)
    expect.assert_in("/", routes, None)
    expect.assert_in("/new", routes, None)
    expect.assert_in("/create", routes, None)


@test("contains endpoints")
def _(app=test_app):
    endpoints = [route.endpoint for route in app.url_map.iter_rules()]

    expect.assert_in("home.index", endpoints, None)
    expect.assert_in("home.new", endpoints, None)
    expect.assert_in("home.create", endpoints, None)
    expect.assert_in("contact.index", endpoints, None)


@test("contains methods")
def _(app=test_app):
    methods = [
        route
        for routes in app.url_map.iter_rules()
        for route in routes.methods
    ]

    expect.assert_equal(methods.count("GET"), 4, None)
    expect.assert_equal(methods.count("POST"), 1, None)
