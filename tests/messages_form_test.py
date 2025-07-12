from flask import url_for

from tests.app import db
from tests.app.models.message import Message


def test_must_have_put_input_hidden(browser):
    message = Message.query.filter_by(title="Message One").first()

    browser.visit(url_for("messages.edit", id=message.id))

    assert browser.is_element_present_by_name("_method")
    assert browser.is_element_present_by_value("PUT")


def test_must_have_delete_input_hidden(browser):
    message = Message.query.filter_by(title="Message One").first()

    browser.visit(url_for("messages.show", id=message.id))

    assert browser.is_element_present_by_name("_method")
    assert browser.is_element_present_by_value("DELETE")


def test_update_message_using_put_http_method(browser):
    message = Message.query.filter_by(title="Message One").first()

    browser.visit(url_for("messages.edit", id=message.id))
    browser.fill("title", "Message updated")
    browser.find_by_value("send").click()

    assert Message.query.first().title == "Message updated"


def test_delete_message_using_put_http_method(browser):
    message = Message.query.filter_by(title="Message One").first()

    browser.visit(url_for("messages.show", id=message.id))
    browser.find_by_value("delete").click()

    assert browser.url == "/messages"
    assert browser.is_text_not_present("Message updated")
    assert Message.query.count() == 0
