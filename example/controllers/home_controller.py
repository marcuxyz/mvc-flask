from flask import render_template, redirect, url_for, request


class HomeController:
    def index(self):
        return render_template("index.html")

    def new(self):
        return render_template("post/new.html")

    def create(self):
        return redirect(url_for(".index"))
