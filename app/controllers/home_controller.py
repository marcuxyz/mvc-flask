class HomeController:
    before_request = ["hi"]

    def index(self):
        return "home"

    def hello(self):
        return "hello"

    def hi(self):
        print("hi")
