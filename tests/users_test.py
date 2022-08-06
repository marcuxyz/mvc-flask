from flask import url_for
from ward import test

from tests.fixtures import test_client


@test("GET /users")
def _(client=test_client):
    resp = client.get(url_for("users.index", id=1))

    assert resp.status_code == 200
    assert "users" in resp.get_data(as_text=True)


@test("GET /users/1")
def _(client=test_client):
    resp = client.get(url_for("users.show", id=1))

    assert resp.status_code == 200
    assert "user 1" in resp.get_data(as_text=True)


@test("GET /users/new")
def _(client=test_client):
    resp = client.get(url_for("users.new"))

    assert resp.status_code == 200
    assert "form" in resp.get_data(as_text=True)


@test("POST /users")
def _(client=test_client):
    resp = client.post(url_for("users.create"))

    assert resp.status_code == 201
    assert "user created" in resp.get_data(as_text=True)


@test("GET /users/1/edit")
def _(client=test_client):
    resp = client.get(url_for("users.edit", id=1))

    assert resp.status_code == 200
    assert "form" in resp.get_data(as_text=True)


@test("PUT /users/1")
def _(client=test_client):
    resp = client.put(url_for("users.update", id=1))

    assert resp.status_code == 200
    assert "updated user: 1" in resp.get_data(as_text=True)


@test("PATCH /users/1")
def _(client=test_client):
    resp = client.patch(url_for("users.update", id=1))

    assert resp.status_code == 200
    assert "updated user: 1" in resp.get_data(as_text=True)


@test("DELETE /users/1")
def _(client=test_client):
    resp = client.delete(url_for("users.delete", id=1))

    assert resp.status_code == 200
    assert "delete user: 1" in resp.get_data(as_text=True)
