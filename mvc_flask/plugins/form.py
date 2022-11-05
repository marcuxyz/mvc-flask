from markupsafe import Markup


class Form:
    """Create form plugin for work with put and delete HTTP form method.

    :param app: The instance of flask application
    """

    def __init__(self, app) -> None:
        self.app = app

    def register(self):
        self.app.jinja_env.globals["mvc_form"] = self.build()

    def build(self):
        """Create javascript block for intercept request HTTP form that contains put or delete
        methods. The script work to send payload to update or delete method.
        """
        return Markup(
            """
            <script>
                const form = document.querySelector('form');

                form.addEventListener('submit', async (event) => {
                    event.preventDefault();

                    const formData = new FormData(form)
                    const formAction = form.getAttribute('action');
                    const formMethod = form.getAttribute('method').toLowerCase();

                    if (formMethod == 'put' || formMethod == 'delete') {
                    const response = await fetch(formAction, { method: formMethod, body: formData })

                    if (response.redirected) window.location.href = response.url
                    }
                })
            </script>
        """
        )
