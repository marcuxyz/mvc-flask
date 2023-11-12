from flask import url_for

from tests.app.models.message import Message
from tests.app import db


def test_update_message_using_put_http_method(browser):
    message = Message(title="Message One")
    db.session.add(message)
    db.session.commit()

    browser.visit(url_for("messages.edit", id=message.id))
    browser.fill("title", "Message updated")
    browser.find_by_value("send").click()

    assert Message.query.first().title == "Message updated"


def test_delete_message_using_put_http_method(browser):
    message = Message(title="Message One")
    db.session.add(message)
    db.session.commit()

    browser.visit(url_for("messages.show", id=message.id))
    browser.find_by_value("delete").click()

    assert browser.url == "/messages"
    assert browser.is_text_not_present("Message updated")
    assert Message.query.count() == 0
