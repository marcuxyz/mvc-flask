from collections import Counter


def test_when_blueprints_have_been_registered(client):
    assert "messages" in client.application.blueprints


def test_when_not_exists_registered_blueprints(client):
    assert Counter(client.application.blueprints.keys()) == {
        "messages": 1,
        "health": 1,
        "posts": 1,
    }


def test_when_messages_routes_have_been_registered(client):
    endpoints = ["/messages", "/messages/new", "/messages/<id>", "/messages/<id>/edit"]
    routes = [route.rule for route in client.application.url_map.iter_rules()]

    for endpoint in endpoints:
        assert endpoint in routes


def test_when_messages_endpoint_have_been_registered(client):
    endpoints = [route.endpoint for route in client.application.url_map.iter_rules()]

    assert f"messages.index" in endpoints
    assert f"messages.show" in endpoints
    assert f"messages.new" in endpoints
    assert f"messages.create" in endpoints
    assert f"messages.edit" in endpoints
    assert f"messages.update" in endpoints
    assert f"messages.delete" in endpoints
