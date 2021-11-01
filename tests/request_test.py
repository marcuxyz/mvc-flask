from collections import Counter

from flask import url_for
from ward import test

from tests.fixtures import test_client


@test("request GET (/)")
def _(client=test_client):
    resp = client.get(url_for("home.index"))

    assert resp.status_code == 200
    assert b"home" in resp.data


@test("request POST (/messages)")
def _(client=test_client):
    resp = client.post(url_for("messages.create"))

    assert resp.status_code == 201
    assert b"message has been created" in resp.data


@test("request PUT (/users/1)")
def _(client=test_client):
    resp = client.put(url_for("users.update", id=1))

    assert resp.status_code == 200
    assert b"user 1 updated successfully" in resp.data


@test("request PUT (/users/1)")
def _(client=test_client):
    resp = client.delete(url_for("users.delete", id=1))

    assert resp.status_code == 200
    assert b"user 1 has been destroyed" in resp.data
