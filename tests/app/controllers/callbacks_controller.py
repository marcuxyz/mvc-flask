class CallbacksController:
    before_request = ["before"]

    def index(self):
        return self.page

    def before(self):
        self.page = "index"
