from werkzeug.formparser import parse_form_data


class MethodOverrideMiddleware:
    allowed_methods = frozenset(
        [
            "GET",
            "POST",
            "DELETE",
            "PUT",
            "PATCH",
        ]
    )
    bodyless_methods = frozenset(
        [
            "GET",
            "HEAD",
            "OPTIONS",
            "DELETE",
        ]
    )

    def __init__(self, app, input_name="_method"):
        self.app = app
        self.input_name = input_name

    def __call__(self, environ, start_response):
        if environ["REQUEST_METHOD"].upper() == "POST":
            stream, form, files = parse_form_data(environ)
            method = (form.get(self.input_name) or "").upper()

            if method in self.allowed_methods:
                environ["wsgi._post_form"] = form
                environ["wsgi._post_files"] = files
                environ["REQUEST_METHOD"] = method

            if method in self.bodyless_methods:
                environ["CONTENT_LENGTH"] = "0"

        return self.app(environ, start_response)
