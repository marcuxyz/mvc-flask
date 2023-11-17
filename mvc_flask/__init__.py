from flask import Flask

from .middlewares.http.router_middleware import RouterMiddleware as Router

from .middlewares.http.method_override_middleware import MethodOverrideMiddleware
from .middlewares.http.custom_request_middleware import CustomRequestMiddleware
from .middlewares.blueprint_middleware import BlueprintMiddleware


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
        # register_blueprint(app)
        BlueprintMiddleware(app, path).register()

        @app.context_processor
        def inject_stage_and_region():
            return dict(method=InputMethodHelper().input_hidden_method)
