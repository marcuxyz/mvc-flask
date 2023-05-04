from flask import url_for
from ward import each, test

from tests.fixtures import client, browser
from tests.app.db.storage import data


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


@test("must update data from form", tags=["request"])
def _(browser=browser):
    browser.visit(url_for("messages.edit", id=1))
    browser.fill("message", "the message of flask mvc")
    browser.find_by_value("send").click()

    assert browser.url == "/messages"
    assert browser.is_text_present("Hello, FLASK MVC")


@test("must delete data from form", tags=["request"])
def _(browser=browser):
    browser.visit(url_for("messages.show", id=1))

    assert len(data) == 3
    assert 1 in data
    assert 2 in data
    assert 3 in data

    browser.find_by_value("delete").click()

    assert browser.url == "/messages"
    assert len(data) == 2
    assert 1 in data
    assert 2 in data
    assert 3 not in data
