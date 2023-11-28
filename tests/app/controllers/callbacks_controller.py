class CallbacksController:
    before_request = dict(callback="before_set_page", actions="index")
    after_request = dict(callback="after_set_page", actions="show")

    def index(self):
        return self.page

    def show(self, id):
        return "hello"

    def before_set_page(self):
        self.page = "before request message"

    def after_set_page(self, response):
        response.headers["from_after_request"] = "yes"
        return response
