import json
from collections import namedtuple
from importlib import import_module
from pathlib import Path
from typing import List
from .hook import Hook

from flask import Flask
from flask.blueprints import Blueprint

Route = namedtuple(
    "Route", ["method", "path", "controller", "action", "hooks"]
)


class FlaskMVC:
    """FlaskMVC extension mvc-flask

    Usage:
        mvc = FlaskMVC()
        mvc.init_app(app)
    """

    def __init__(self, app: Flask = None, directory: str = "app"):
        self.directory = Path(directory)

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.hook = Hook()

        self.create_blueprint(app)

    def routes(self) -> List[Route]:
        """Get all routes registered in routes.json

        Returns:
            List[Route]: Route is a class that contains properties such as: method, path, controller, action and hooks.
        """
        routes = []
        with open(self.directory / "routes.json", mode="r") as f:
            routes = [
                Route(
                    route["method"],
                    route["path"],
                    route["controller"],
                    route["action"],
                    route.get("hooks"),
                )
                for route in json.load(f)
            ]
        return routes

    def create_blueprint(self, app: Flask):
        """Create blueprint for register all routes

        Args:
            app (Flask): instance of current flask application
        """
        for route in self.routes():
            controller_file = (
                self.directory
                / "controllers"
                / f"{route.controller}_controller"
            )

            obj = import_module(controller_file.as_posix().replace("/", "."))
            controller = getattr(obj, f"{route.controller.title()}Controller")

            blueprint = Blueprint(route.controller, route.controller)
            blueprint.add_url_rule(
                rule=route.path,
                endpoint=route.action,
                view_func=getattr(controller(), route.action),
                methods=[route.method],
            )

            self.hook.register(
                route.hooks, blueprint=blueprint, controller=controller
            )

            app.register_blueprint(blueprint)
