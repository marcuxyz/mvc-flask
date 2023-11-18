from flask import Flask
from importlib import import_module

from flask.blueprints import Blueprint

from .hook_middleware import HookMiddleware

from .http.router_middleware import RouterMiddleware as Router


class BlueprintMiddleware:
    def __init__(self, app: Flask, path: str) -> None:
        self.app = app
        self.path = path

        # load routes defined from users
        import_module(f"{self.path}.routes")

    def register(self):
        for route in Router._method_route().items():
            controller = route[0]
            blueprint = Blueprint(controller, controller)

            obj = import_module(f"{self.path}.controllers.{controller}_controller")
            view_func = getattr(obj, f"{controller.title()}Controller")
            instance_of_controller = view_func()

            HookMiddleware().register(instance_of_controller, blueprint)

            for resource in route[1]:
                blueprint.add_url_rule(
                    rule=resource.path,
                    endpoint=resource.action,
                    view_func=getattr(instance_of_controller, resource.action),
                    methods=resource.method,
                )

            self.app.register_blueprint(blueprint)
