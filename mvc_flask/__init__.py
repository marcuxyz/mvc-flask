from importlib import import_module

from flask import Flask
from flask.blueprints import Blueprint

from .router import Router

from .middlewares.http.method_override_middleware import MethodOverrideMiddleware
from .middlewares.http.custom_request_middleware import CustomRequestMiddleware
from .middlewares.hook_middleware import HookMiddleware

from .helpers.html.input_method_helper import InputMethodHelper


class FlaskMVC:
    def __init__(self, app: Flask = None, path="app"):
        if app is not None:
            self.init_app(app, path)

    def init_app(self, app: Flask = None, path="app"):
        self.path = path

        app.template_folder = "views"
        app.request_class = CustomRequestMiddleware
        app.wsgi_app = MethodOverrideMiddleware(app.wsgi_app)

        # register blueprint
        self.register_blueprint(app)

        @app.context_processor
        def inject_stage_and_region():
            return dict(method=InputMethodHelper().input_hidden_method)

    def register_blueprint(self, app: Flask):
        # load routes defined from users
        import_module(f"{self.path}.routes")

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

            app.register_blueprint(blueprint)
