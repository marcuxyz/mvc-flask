import json

from flask import url_for

from tests.app.models.message import Message
from tests.app import db


def test_create_a_message(client):
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"title": "hello"})
    expected = "hello"

    res = client.post(url_for("messages.create"), data=data, headers=headers)

    assert res.status_code == 201
    assert res.json["title"] == expected
    assert Message.query.first().title == expected


def test_update_a_message(client):
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"title": "hello updated"})
    message = Message(title="Message One")

    db.session.add(message)
    db.session.commit()
    res = client.put(
        url_for("messages.update", id=message.id), data=data, headers=headers
    )

    assert res.json["title"] == "hello updated"
    assert Message.query.first().title == "hello updated"
