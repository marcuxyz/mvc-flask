from collections import namedtuple

Model = namedtuple("Model", "method path controller action")


class Router:
    ROUTES = []

    @staticmethod
    def _method_route():
        routes = {}

        for route in Router.ROUTES:
            value = list(route.values())[0]
            for key in route:
                if key not in routes:
                    routes[key] = [value]
                else:
                    routes[key].append(value)
        return routes

    @staticmethod
    def get(path: str, resource: str):
        controller, action = resource.split("#")
        Router.ROUTES.append(
            {controller: Model(["GET"], path, controller, action)}
        )

    @staticmethod
    def post(path: str, resource: str):
        controller, action = resource.split("#")
        Router.ROUTES.append(
            {controller: Model(["POST"], path, controller, action)}
        )

    @staticmethod
    def put(path: str, resource: str):
        controller, action = resource.split("#")
        Router.ROUTES.append(
            {controller: Model(["PUT", "PATCH"], path, controller, action)},
        )

    @staticmethod
    def delete(path: str, resource: str):
        controller, action = resource.split("#")
        Router.ROUTES.append(
            {controller: Model(["DELETE"], path, controller, action)}
        )

    @staticmethod
    def all(resource: str, only=None):
        group = [
            "index",
            "show",
            "new",
            "create",
            "edit",
            "update",
            "delete",
        ]
        actions = only.split() if isinstance(only, str) else only
        Router._add_routes(resource, actions if actions else group)

    @staticmethod
    def _add_routes(name, actions):
        groups = {
            "index": "get",
            "new": "get",
            "create": "post",
        }
        parameters = {
            "show": "get",
            "edit": "get",
            "update": "put",
            "delete": "delete",
        }
        urls = {
            "new": "/new",
            "edit": "/<id>/edit",
            "show": "/<id>",
            "update": "/<id>",
            "delete": "/<id>",
        }

        for action in actions:
            path = f"/{name}{urls[action]}" if action in urls else f"/{name}"

            if action in parameters:
                getattr(Router, parameters[action])(path, f"{name}#{action}")
                continue

            getattr(Router, groups[action])(path, f"{name}#{action}")
