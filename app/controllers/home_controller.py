class HomeController:
    before_request = ["hi"]

    def index(self, view, request):
        return "home"

    def hello(self, view, request):
        return "hello"

    def hi(self):
        print("hi")
