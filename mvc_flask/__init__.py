import json
from pathlib import Path
from importlib import import_module

from flask import Flask


class FlaskMVC:
    def __init__(self, app: Flask = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.template_folder = "views"
        app.config.setdefault("FLASK_MVC_DIR", "app")

        self.root_path = Path(app.config["FLASK_MVC_DIR"])

        self._register_router(app)

    def _routes(self):
        with open(self.root_path / "routes.json", mode="r") as f:
            return json.load(f)

    def _register_router(self, app):
        for route in self._routes():
            controller = route["controller"]

            mod = import_module(
                f"{self.root_path}.controllers.{controller}_controller"
            )
            clazz = getattr(mod, f"{controller.title()}Controller")

            app.add_url_rule(
                route["path"],
                endpoint=f"{controller}.{route['action']}",
                view_func=getattr(clazz(), route["action"]),
                methods=[route["method"]],
            )
