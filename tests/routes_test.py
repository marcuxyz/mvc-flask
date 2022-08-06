from collections import Counter

from ward import test

from tests.fixtures import client


@test("confirm if messages blueprint was registered", tags=["routes"])
def _(client=client):
    assert "messages" in client.application.blueprints


@test("verify if exists duplicate blueprints registered", tags=["routes"])
def _(client=client):
    assert Counter(client.application.blueprints.keys()) == {
        "messages": 1,
    }


@test("and view registered path", tags=["routes"])
def _(client=client):
    routes = [route.rule for route in client.application.url_map.iter_rules()]

    assert "/messages" in routes


@test("and view registered endpoints", tags=["routes"])
def _(client=client):
    endpoints = [route.endpoint for route in client.application.url_map.iter_rules()]

    assert "messages.index" in endpoints
    assert "messages.show" in endpoints
    assert "messages.new" in endpoints
    assert "messages.create" in endpoints
    assert "messages.edit" in endpoints
    assert "messages.update" in endpoints
    assert "messages.delete" in endpoints


@test("and count verbs registered for HTTP", tags=["routes"])
def _(client=client):
    methods = [
        route
        for routes in client.application.url_map.iter_rules()
        for route in routes.methods
    ]

    assert methods.count("GET") == 5
    assert methods.count("POST") == 1
    assert methods.count("PUT") == 1
    assert methods.count("PATCH") == 1
    assert methods.count("DELETE") == 1
