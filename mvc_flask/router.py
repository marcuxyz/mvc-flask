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
            {controller: Model("GET", path, controller, action)}
        )

    @staticmethod
    def post(path: str, resource: str):
        controller, action = resource.split("#")
        Router.ROUTES.append(
            {controller: Model("POST", path, controller, action)}
        )

    @staticmethod
    def put(path: str, resource: str):
        controller, action = resource.split("#")
        Router.ROUTES.append(
            {controller: Model("PUT", path, controller, action)}
        )

    @staticmethod
    def delete(path: str, resource: str):
        controller, action = resource.split("#")
        Router.ROUTES.append(
            {controller: Model("DELETE", path, controller, action)}
        )
