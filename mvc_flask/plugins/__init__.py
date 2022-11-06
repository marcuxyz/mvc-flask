from .form import Form


def register(app):
    """Register the plugins for Flask MVC

    :param app: The instance of flask application
    """
    Form(app).register()
