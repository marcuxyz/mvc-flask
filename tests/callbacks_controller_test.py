from flask import url_for


def test_before_request(client):
    response = client.get(url_for("callbacks.index"))

    assert response.text == "before request message"


def test_after_request(client):
    response = client.get(url_for("callbacks.show", id=1))

    assert response.headers["from_after_request"] == "yes"
    assert response.text == "hello"
