from flask import url_for
from ward import each, test

from tests.fixtures import client, browser


@test("should return status 200 for GET (INDEX)", tags=["request"])
def _(client=client, resource=each("messages", "user", "posts", "health")):
    resp = client.get(url_for(f"{resource}.index"))

    assert resp.status_code == 200


@test("should return status 200 for GET (SHOW)", tags=["request"])
def _(client=client, resource=each("messages", "user", "posts")):
    resp = client.get(url_for(f"{resource}.show", id=1))

    assert resp.status_code == 200


@test("should return status 200 for GET (/messages/new)", tags=["request"])
def _(client=client):
    resp = client.get(url_for("messages.new"))

    assert resp.status_code == 200


@test("should return status 201 for POST (CREATE)", tags=["request"])
def _(client=client, resource=each("messages", "user", "posts")):
    resp = client.post(url_for(f"{resource}.create"))

    assert resp.status_code == 201


@test("sent form data via put must be redirected", tags=["request"])
def _(browser=browser):
    browser.visit(url_for("messages.edit", id=1))
    browser.fill("message", "the message of flask mvc")
    browser.find_by_value("send").click()

    assert browser.url == "http://localhost/messages"
    assert browser.is_text_present("Hello, FLASK MVC")


@test("should return status 200 for GET (UPDATE)", tags=["request", "update"])
def _(client=client, resource=each("messages", "user", "posts")):
    resp = client.put(
        url_for(f"{resource}.update", id=1), follow_redirects=True
    )

    assert resp.status_code == 200


@test("should return status 200 for GET (DELETE)", tags=["request"])
def _(client=client, resource=each("messages", "user", "posts")):
    resp = client.delete(url_for("messages.delete", id=1))

    assert resp.status_code == 200
