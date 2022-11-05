from flask import render_template_string, render_template, redirect, url_for


class MessagesController:
    def index(self):
        return render_template_string(
            "<h1>Hello, {{ name }}", name="FLASK MVC"
        )

    def show(self, id):
        return {}, 200

    def new(self):
        return {}, 200

    def create(self):
        return {}, 201

    def edit(self, id):
        return render_template("messages/edit.html")

    def update(self, id):
        return redirect(url_for(".index"))

    def delete(self, id):
        return {}, 200
