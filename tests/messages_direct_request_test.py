import json

from flask import url_for

from tests.app import db
from tests.app.models.message import Message


def test_create_a_message(client):
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"title": "hello"})

    res = client.post(url_for("messages.create"), data=data, headers=headers)

    assert res.status_code == 201
    assert res.json["title"] == "hello"


def test_update_a_message(client):
    message = Message.query.filter_by(title="Message One").first()

    res = client.put(
        url_for("messages.update", id=message.id),
        data=json.dumps({"title": "hello updated"}),
        headers={"Content-Type": "application/json"},
    )

    assert res.json["title"] == "hello updated"
    assert message.title == "hello updated"
