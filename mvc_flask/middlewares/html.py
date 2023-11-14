import markupsafe


class HTMLMiddleware:
    def _input_html(self, input_method):
        return f"<input type='hidden' name='_method' value={input_method.upper()}>"

    def _put(self):
        return self._input_html("put")

    def _delete(self):
        return self._input_html("delete")

    def method(self, string):
        result = {
            "put": self._put(),
            "delete": self._delete(),
        }[string.lower()]

        return markupsafe.Markup(result)
