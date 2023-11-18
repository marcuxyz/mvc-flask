from flask import render_template, redirect, url_for, request
from tests.app.models.message import Message
from tests.app import db


class MessagesController:
    def index(self):
        message = Message.query.first()

        return render_template("messages/index.html", message=message)

    def show(self, id):
        message = Message.query.first()

        return render_template("messages/show.html", message=message)

    def new(self):
        return {}, 200

    def create(self):
        message = Message(title=request.json["title"])
        db.session.add(message)
        db.session.commit()

        return {"title": message.title}, 201

    def edit(self, id):
        return render_template("messages/edit.html")

    def update(self, id):
        message = Message.query.filter_by(id=id).first()

        if request.headers["Content-Type"] == "application/json":
            message.title = request.json["title"]
            db.session.add(message)
            db.session.commit()

            return {"title": message.title}
        else:
            message.title = request.form.get("title")
            db.session.add(message)
            db.session.commit()

            return render_template("messages/show.html", message=message)

    def delete(self, id):
        message = Message.query.filter_by(id=id).first()
        db.session.delete(message)
        db.session.commit()

        return redirect(url_for(".index"))
