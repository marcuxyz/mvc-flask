from collections import Counter

from ward import test

from tests.fixtures import test_client


@test("confirm if blueprints was registered")
def _(client=test_client):
    assert "home" in client.application.blueprints


@test("verify if exists duplicate blueprints")
def _(client=test_client):
    assert Counter(client.application.blueprints.keys()) == {
        "home": 1,
        "messages": 1,
        "users": 1,
    }


@test("view path")
def _(client=test_client):
    routes = [route.rule for route in client.application.url_map.iter_rules()]

    assert "/" in routes
    assert "/hello" in routes


@test("view endpoints")
def _(client=test_client):
    endpoints = [
        route.endpoint for route in client.application.url_map.iter_rules()
    ]

    assert "home.index" in endpoints
    assert "home.hello" in endpoints


@test("count GET")
def _(client=test_client):
    methods = [
        route
        for routes in client.application.url_map.iter_rules()
        for route in routes.methods
    ]

    assert methods.count("GET") == 10


@test("count POST")
def _(client=test_client):
    methods = [
        route
        for routes in client.application.url_map.iter_rules()
        for route in routes.methods
    ]

    assert methods.count("POST") == 2


@test("count PUT")
def _(client=test_client):
    methods = [
        route
        for routes in client.application.url_map.iter_rules()
        for route in routes.methods
    ]

    assert methods.count("PUT") == 1


@test("count DELETE")
def _(client=test_client):
    methods = [
        route
        for routes in client.application.url_map.iter_rules()
        for route in routes.methods
    ]

    assert methods.count("DELETE") == 1
