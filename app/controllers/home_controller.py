from flask import redirect, url_for, request


class HomeController:
    before_request = ["redirect_to_hi"]

    def index(self, view, request):
        return "home"

    def hello(self, view, request):
        return "hello"

    def redirect_to_hi(self):
        if request.endpoint == "home.index":
            return redirect(url_for(".hello"))
