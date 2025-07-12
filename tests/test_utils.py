"""
Test utilities and helper functions for mvc-flask tests.
"""

import functools
import time
from contextlib import contextmanager
from typing import Any, Callable, Dict, List

import pytest
from flask import Flask

from tests.app import db
from tests.app.models.message import Message


class TimerUtil:
    """Context manager for timing test operations."""

    def __init__(self, max_duration: float = None):
        self.max_duration = max_duration
        self.start_time = None
        self.end_time = None
        self.duration = None

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.duration = self.end_time - self.start_time

        if self.max_duration and self.duration > self.max_duration:
            pytest.fail(
                f"Operation took {self.duration:.3f}s, expected < {self.max_duration}s"
            )


def performance_test(max_duration: float = 1.0):
    """Decorator for performance testing."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with TimerUtil(max_duration):
                return func(*args, **kwargs)

        return wrapper

    return decorator


class DatabaseHelper:
    """Helper class for database operations in tests."""

    @staticmethod
    def create_sample_messages(count: int = 3) -> List[Message]:
        """Create sample messages for testing."""
        messages = []
        for i in range(count):
            message = Message(title=f"Test Message {i + 1}")
            db.session.add(message)
            messages.append(message)
        db.session.commit()
        return messages

    @staticmethod
    def clear_messages():
        """Clear all messages from database."""
        Message.query.delete()
        db.session.commit()

    @staticmethod
    def count_messages() -> int:
        """Get count of messages in database."""
        return Message.query.count()

    @staticmethod
    @contextmanager
    def transaction():
        """Context manager for database transactions."""
        try:
            yield
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise


class RouteHelper:
    """Helper class for route testing."""

    @staticmethod
    def get_all_routes(app: Flask) -> List[Dict[str, Any]]:
        """Get all routes from Flask app."""
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append(
                {
                    "rule": rule.rule,
                    "methods": list(rule.methods),
                    "endpoint": rule.endpoint,
                    "subdomain": rule.subdomain,
                }
            )
        return routes

    @staticmethod
    def get_routes_by_blueprint(app: Flask, blueprint_name: str) -> List[Dict[str, Any]]:
        """Get routes for specific blueprint."""
        all_routes = RouteHelper.get_all_routes(app)
        return [
            route
            for route in all_routes
            if route["endpoint"].startswith(f"{blueprint_name}.")
        ]

    @staticmethod
    def get_routes_by_method(app: Flask, method: str) -> List[Dict[str, Any]]:
        """Get routes that support specific HTTP method."""
        all_routes = RouteHelper.get_all_routes(app)
        return [route for route in all_routes if method.upper() in route["methods"]]


class ResponseHelper:
    """Helper class for response validation."""

    @staticmethod
    def assert_status_code(response, expected_code: int):
        """Assert response has expected status code."""
        assert (
            response.status_code == expected_code
        ), f"Expected status {expected_code}, got {response.status_code}"

    @staticmethod
    def assert_json_response(response, expected_data: Dict[str, Any] = None):
        """Assert response is valid JSON and optionally matches expected data."""
        assert response.is_json, "Response is not JSON"

        if expected_data:
            assert (
                response.json == expected_data
            ), f"JSON mismatch. Expected: {expected_data}, Got: {response.json}"

    @staticmethod
    def assert_redirect(response, expected_location: str = None):
        """Assert response is a redirect."""
        assert (
            300 <= response.status_code < 400
        ), f"Expected redirect (3xx), got {response.status_code}"

        if expected_location:
            assert response.location.endswith(
                expected_location
            ), f"Expected redirect to end with '{expected_location}', got '{response.location}'"

    @staticmethod
    def assert_contains_text(response, text: str):
        """Assert response contains specific text."""
        response_text = response.get_data(as_text=True)
        assert text in response_text, f"Response does not contain '{text}'"

    @staticmethod
    def assert_header_present(response, header_name: str, expected_value: str = None):
        """Assert response has specific header."""
        assert (
            header_name in response.headers
        ), f"Header '{header_name}' not found in response"

        if expected_value:
            actual_value = response.headers[header_name]
            assert (
                actual_value == expected_value
            ), f"Header '{header_name}' has value '{actual_value}', expected '{expected_value}'"


class MockHelper:
    """Helper class for creating mocks and test doubles."""

    @staticmethod
    def create_mock_controller(actions: List[str] = None):
        """Create a mock controller with specified actions."""
        if actions is None:
            actions = ["index", "show", "create", "update", "delete"]

        class MockController:
            def __init__(self):
                self.call_history = []

            def _record_call(self, action, *args, **kwargs):
                self.call_history.append(
                    {
                        "action": action,
                        "args": args,
                        "kwargs": kwargs,
                        "timestamp": time.time(),
                    }
                )

        # Dynamically add action methods
        for action in actions:

            def make_action_method(action_name):
                def action_method(self, *args, **kwargs):
                    self._record_call(action_name, *args, **kwargs)
                    return f"{action_name} called"

                return action_method

            setattr(MockController, action, make_action_method(action))

        return MockController

    @staticmethod
    def create_mock_request_context(app: Flask, path: str = "/", method: str = "GET"):
        """Create a mock request context."""
        return app.test_request_context(path, method=method)


class ValidationHelper:
    """Helper class for common validation tasks."""

    @staticmethod
    def validate_restful_routes(app: Flask, resource_name: str):
        """Validate that RESTful routes exist for a resource."""
        expected_routes = {
            f"/{resource_name}": ["GET", "POST"],
            f"/{resource_name}/new": ["GET"],
            f"/{resource_name}/<id>": ["GET", "PUT", "PATCH", "DELETE"],
            f"/{resource_name}/<id>/edit": ["GET"],
        }

        routes = RouteHelper.get_all_routes(app)
        route_dict = {route["rule"]: route["methods"] for route in routes}

        for expected_rule, expected_methods in expected_routes.items():
            assert expected_rule in route_dict, f"Route '{expected_rule}' not found"

            for method in expected_methods:
                assert (
                    method in route_dict[expected_rule]
                ), f"Method '{method}' not found for route '{expected_rule}'"

    @staticmethod
    def validate_blueprint_structure(
        app: Flask, blueprint_name: str, expected_endpoints: List[str]
    ):
        """Validate blueprint has expected endpoints."""
        routes = RouteHelper.get_routes_by_blueprint(app, blueprint_name)
        actual_endpoints = {route["endpoint"] for route in routes}

        for expected_endpoint in expected_endpoints:
            full_endpoint = f"{blueprint_name}.{expected_endpoint}"
            assert (
                full_endpoint in actual_endpoints
            ), f"Endpoint '{full_endpoint}' not found in blueprint '{blueprint_name}'"

    @staticmethod
    def validate_controller_methods(controller_class, expected_methods: List[str]):
        """Validate controller has expected methods."""
        for method_name in expected_methods:
            assert hasattr(
                controller_class, method_name
            ), f"Controller {controller_class.__name__} missing method '{method_name}'"

            method = getattr(controller_class, method_name)
            assert callable(method), f"Controller method '{method_name}' is not callable"


class BenchmarkHelper:
    """Helper class for performance benchmarking."""

    @staticmethod
    def benchmark_function(func: Callable, iterations: int = 100) -> Dict[str, float]:
        """Benchmark a function and return statistics."""
        times = []

        for _ in range(iterations):
            start = time.time()
            func()
            end = time.time()
            times.append(end - start)

        return {
            "min_time": min(times),
            "max_time": max(times),
            "avg_time": sum(times) / len(times),
            "total_time": sum(times),
            "iterations": iterations,
        }

    @staticmethod
    def compare_performance(
        func1: Callable, func2: Callable, iterations: int = 100
    ) -> Dict[str, Any]:
        """Compare performance of two functions."""
        stats1 = BenchmarkHelper.benchmark_function(func1, iterations)
        stats2 = BenchmarkHelper.benchmark_function(func2, iterations)

        return {
            "function1": stats1,
            "function2": stats2,
            "speedup": stats1["avg_time"] / stats2["avg_time"],
            "winner": (
                "function2" if stats2["avg_time"] < stats1["avg_time"] else "function1"
            ),
        }


# Pytest fixtures using helpers
@pytest.fixture
def db_helper():
    """Provide database helper for tests."""
    return DatabaseHelper()


@pytest.fixture
def route_helper():
    """Provide route helper for tests."""
    return RouteHelper()


@pytest.fixture
def response_helper():
    """Provide response helper for tests."""
    return ResponseHelper()


@pytest.fixture
def validation_helper():
    """Provide validation helper for tests."""
    return ValidationHelper()


@pytest.fixture
def benchmark_helper():
    """Provide benchmark helper for tests."""
    return BenchmarkHelper()
