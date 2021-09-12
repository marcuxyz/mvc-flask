from importlib import import_module
import json

from pathlib import Path
from flask import Flask
from flask.blueprints import Blueprint
from collections import namedtuple


Route = namedtuple("Route", ["method", "path", "controller", "action"])


class FlaskMVC:
    def __init__(self, app: Flask = None, directory: str = "app"):
        self.directory = Path(directory)

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.create_blueprint(app)

    def routes(self):
        routes = []
        with open(self.directory / "routes.json", mode="r") as f:
            routes = [
                Route(
                    route["method"],
                    route["path"],
                    route["controller"],
                    route["action"],
                )
                for route in json.load(f)
            ]
        return routes

    def create_blueprint(self, app: Flask):
        for route in self.routes():
            dd = (
                self.directory
                / "controllers"
                / f"{route.controller}_controller"
            )

            obj = import_module(dd.as_posix().replace("/", "."))
            controller = getattr(obj, f"{route.controller.title()}Controller")

            blueprint = Blueprint(route.controller, route.controller)
            blueprint.add_url_rule(
                rule=route.path,
                endpoint=route.action,
                view_func=getattr(controller(), route.action),
                methods=[route.method],
            )
            app.register_blueprint(blueprint)
