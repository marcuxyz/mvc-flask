from flask import url_for
from ward import test

from tests.fixtures import client


@test("should return status 200 for GET (/messages)", tags=["request"])
def _(client=client):
    resp = client.get(url_for("messages.index"))

    assert resp.status_code == 200


@test("should return status 200 for GET (/messages/show/1)", tags=["request"])
def _(client=client):
    resp = client.get(url_for("messages.show", id=1))

    assert resp.status_code == 200


@test("should return status 200 for GET (/messages/new)", tags=["request"])
def _(client=client):
    resp = client.get(url_for("messages.new"))

    assert resp.status_code == 200


@test("should return status 201 for POST (/messages)", tags=["request"])
def _(client=client):
    resp = client.post(url_for("messages.create"))

    assert resp.status_code == 201


@test("should return status 200 for GET (/messages/1/edit)", tags=["request"])
def _(client=client):
    resp = client.get(url_for("messages.edit", id=1))

    assert resp.status_code == 200


@test(
    "should return status 200 for GET (/messages/update/1)", tags=["request"]
)
def _(client=client):
    resp = client.put(url_for("messages.update", id=1))

    assert resp.status_code == 202


@test(
    "should return status 200 for GET (/messages/delete/1)", tags=["request"]
)
def _(client=client):
    resp = client.delete(url_for("messages.delete", id=1))

    assert resp.status_code == 202
