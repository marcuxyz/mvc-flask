from flask import Request

class CustomRequestMiddleware(Request):
    @property
    def form(self):
        if "wsgi._post_form" in self.environ:
            return self.environ["wsgi._post_form"]
        return super().form

    @property
    def files(self):
        if "wsgi._post_files" in self.environ:
            return self.environ["wsgi._post_files"]
        return super().files
