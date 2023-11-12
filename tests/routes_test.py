from unittest import TestCase
from collections import Counter

from tests.app import create_app


class TestStringMethods(TestCase):
    def setUp(self) -> None:
        app = create_app()
        app.testing = True
        self.client = app.test_client()

    def test_when_blueprints_have_been_registered(self):
        expected_blueprints = {"messages", "health", "user", "posts"}

        self.assertEqual(set(self.blueprints), expected_blueprints)

    def test_when_not_exists_registered_blueprints(self):
        self.assertEqual(
            Counter(self.blueprints.keys()),
            {"messages": 1, "health": 1, "user": 1, "posts": 1},
        )

    def test_when_routes_have_been_registered(self):
        endpoints = [
            "/messages",
            "/messages/new",
            "/messages/<id>",
            "/messages/<id>/edit",
            "/api/v1/health",
            "/api/v1/posts",
            "/api/v1/posts/<id>",
            "/api/v1/user",
            "/api/v1/user/new",
            "/api/v1/user/<id>",
            "/api/v1/user/<id>/edit",
        ]
        routes = [route.rule for route in self.client.application.url_map.iter_rules()]

        for endpoint in endpoints:
            self.assertIn(endpoint, routes)

    def test_when_endpoints_have_been_registered(self):
        for resource in ["messages", "user"]:
            self.assertIn(f"{resource}.index", self.endpoints)
            self.assertIn(f"{resource}.show", self.endpoints)
            self.assertIn(f"{resource}.new", self.endpoints)
            self.assertIn(f"{resource}.create", self.endpoints)
            self.assertIn(f"{resource}.edit", self.endpoints)
            self.assertIn(f"{resource}.update", self.endpoints)
            self.assertIn(f"{resource}.delete", self.endpoints)

    def test_when_when_there_are_many_registered_routes(self):
        methods = [
            route
            for routes in self.client.application.url_map.iter_rules()
            for route in routes.methods
        ]

        self.assertEqual(methods.count("GET"), 13)
        self.assertEqual(methods.count("POST"), 3)
        self.assertEqual(methods.count("PUT"), 3)
        self.assertEqual(methods.count("PATCH"), 3)
        self.assertEqual(methods.count("DELETE"), 2)

    @property
    def endpoints(self):
        return [url.endpoint for url in self.client.application.url_map.iter_rules()]

    @property
    def blueprints(self):
        return self.client.application.blueprints
