from importlib import import_module
from pathlib import Path

from flask import Flask
from flask.blueprints import Blueprint

from .router import Router


class FlaskMVC:
    def __init__(self, app: Flask = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.template_folder = "views"

        self.register_blueprint(app)

    def register_blueprint(self, app: Flask):
        # load routes defined from users
        import_module(f"app.routes")

        for route in Router._method_route().items():
            controller = route[0]
            blueprint = Blueprint(controller, controller)
            obj = import_module(f"app.controllers.{controller}_controller")
            view_func = getattr(obj, f"{controller.title()}Controller")
            for resource in route[1]:
                blueprint.add_url_rule(
                    rule=resource.path,
                    endpoint=resource.action,
                    view_func=getattr(view_func(), resource.action),
                    methods=[resource.method],
                )
            app.register_blueprint(blueprint)
