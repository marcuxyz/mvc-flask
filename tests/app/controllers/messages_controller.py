from flask import render_template, redirect, url_for

from tests.app.db.storage import data


class MessagesController:
    def index(self):
        return "Hello, FLASK MVC!"

    def show(self, id):
        return render_template("messages/show.html")

    def new(self):
        return {}, 200

    def create(self):
        return {}, 201

    def edit(self, id):
        return render_template("messages/edit.html")

    def update(self, id):
        return redirect(url_for(".index"))

    def delete(self, id):
        data.pop()
        return redirect(url_for(".index"))
