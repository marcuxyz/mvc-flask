from flask import render_template


class HomeController:
    def index(self):
        return render_template("index.html")

    def aftermoon(self):
        print("good aftermoon!")
