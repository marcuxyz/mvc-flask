from collections import Counter

from ward import each, test

from tests.fixtures import client


@test("confirm if blueprints was registered", tags=["routes"])
def _(client=client, resource=each("messages", "health", "user", "posts")):
    assert resource in client.application.blueprints


@test("verify if exists duplicate blueprints registered", tags=["routes"])
def _(client=client):
    assert Counter(client.application.blueprints.keys()) == {
        "messages": 1, "health": 1, "user": 1, "posts": 1
    }


@test("and view registered path", tags=["routes"])
def _(
    client=client,
    endpoint=each(
        "/messages",
        "/messages/new",
        "/messages/<id>",
        "/messages/<id>/edit",
        "/api/v1/health",
        "/api/v1/posts",
        "/api/v1/posts/<id>",
        "/api/v1/user",
        "/api/v1/user/new",
        "/api/v1/user/<id>",
        "/api/v1/user/<id>/edit",

    ),
):
    routes = [route.rule for route in client.application.url_map.iter_rules()]

    assert endpoint in routes


@test("and view registered endpoints", tags=["routes"])
def _(client=client, resource=each("messages", "user")):
    endpoints = [
        route.endpoint for route in client.application.url_map.iter_rules()
    ]

    assert f"{resource}.index" in endpoints
    assert f"{resource}.show" in endpoints
    assert f"{resource}.new" in endpoints
    assert f"{resource}.create" in endpoints
    assert f"{resource}.edit" in endpoints
    assert f"{resource}.update" in endpoints
    assert f"{resource}.delete" in endpoints


@test("and count verbs registered for HTTP", tags=["routes"])
def _(client=client):
    methods = [
        route
        for routes in client.application.url_map.iter_rules()
        for route in routes.methods
    ]

    assert methods.count("GET") == 13
    assert methods.count("POST") == 3
    assert methods.count("PUT") == 3
    assert methods.count("PATCH") == 3
    assert methods.count("DELETE") == 2
