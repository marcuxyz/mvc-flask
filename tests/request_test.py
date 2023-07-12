import json

from flask import url_for
from ward import each, test

from tests.app.models.message import Message
from tests.fixtures import client, browser
from tests.app import db


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


@test(
    "should return status 201 for POST (CREATE)",
    tags=["request", "create", "user", "posts"],
)
def _(client=client, resource=each("user", "posts")):
    message = Message(title="Message One")
    db.session.add(message)
    db.session.commit()

    resp = client.post(url_for(f"{resource}.create"))

    assert resp.status_code == 201


@test(
    "should create a message sending json",
    tags=["request", "messages", "create", "json"],
)
def _(client=client):
    message = Message(title="Message One")
    db.session.add(message)
    db.session.commit()

    data = {"title": "hello, andrews"}
    res = client.post(
        url_for("messages.create"),
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )

    assert res.status_code == 201
    assert res.json["title"] == "hello, andrews"


@test(
    "should update message from form", tags=["request", "messages", "update"]
)
def _(browser=browser):
    message = Message(title="Message One")
    db.session.add(message)
    db.session.commit()

    browser.visit(url_for("messages.edit", id=message.id))
    browser.fill("title", "Message updated")
    browser.find_by_value("send").click()

    assert browser.url == "/messages"
    assert browser.is_text_present("Message updated")


@test(
    "should delete message from form", tags=["request", "messages", "delete"]
)
def _(browser=browser):
    message = Message(title="Message One")
    db.session.add(message)
    db.session.commit()

    browser.visit(url_for("messages.show", id=message.id))
    browser.find_by_value("delete").click()

    assert browser.url == "/messages"
    assert browser.is_text_not_present("Message updated")
