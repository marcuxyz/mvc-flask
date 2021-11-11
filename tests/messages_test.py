from flask import url_for
from ward import test

from tests.fixtures import test_client


@test("GET /messages")
def _(client=test_client):
    resp = client.get(url_for("messages.index", id=1))

    assert resp.status_code == 200
    assert "messages" in resp.get_data(as_text=True)


@test("GET /messages/1")
def _(client=test_client):
    resp = client.get(url_for("messages.show", id=1))

    assert resp.status_code == 200
    assert "message 1" in resp.get_data(as_text=True)


@test("GET /messages/new")
def _(client=test_client):
    resp = client.get(url_for("messages.new"))

    assert resp.status_code == 200
    assert "form" in resp.get_data(as_text=True)


@test("POST /messages")
def _(client=test_client):
    resp = client.post(url_for("messages.create"))

    assert resp.status_code == 201
    assert "message created" in resp.get_data(as_text=True)
