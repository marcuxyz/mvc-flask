"""Custom exceptions for MVC Flask CLI."""


class MVCFlaskError(Exception):
    """Base exception for MVC Flask CLI errors."""

    pass


class ControllerGenerationError(MVCFlaskError):
    """Exception raised when controller generation fails."""

    pass


class TemplateNotFoundError(MVCFlaskError):
    """Exception raised when template file is not found."""

    pass


class InvalidControllerNameError(MVCFlaskError):
    """Exception raised when controller name is invalid."""

    pass
