from flask import url_for


def test_create_a_message(client):
    response = client.get(url_for("callbacks.index"))

    assert response.text == "index"
