![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/marcuxyz/mvc_flask) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/marcuxyz/mvc_flask/unit%20test) ![GitHub](https://img.shields.io/github/license/marcuxyz/mvc_flask) ![PyPI - Downloads](https://img.shields.io/pypi/dm/mvc_flask) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mvc_flask) ![PyPI](https://img.shields.io/pypi/v/mvc_flask)

You can use the MVC pattern in your Flask application using this extension.

## Installation

Run the follow command to install `mvc_flask`:

```shell
$ pip install mvc_flask
```

## Basic Usage

To start the `mvc_flask` you need to import and register in your application.


```python
from flask import Flask
from mvc_flask import FlaskMVC

app = Flask(__name__)
FlaskMVC(app)
```

Or use `application factories`, e.g:

```python
mvc = FlaskMVC()

def create_app():
  ...
  mvc.init_app(app)
```

**By default the `mvc_flask` assumes that your application directory will be `app` and if it doesn't exist, create it!**
**If you can use other directories, you can use the `path` parameter when the instance of FlaskMVC is initialized. E.g:**

```python
mvc = FlaskMVC()

def create_app():
  ...
  mvc.init_app(app, path='src')
```

Now, you can use `src` as default directory for prepare your application.

You structure should be look like this:

```text
app
├── __ini__.py
├── controllers
│   └── home_controller.py
├── routes.py
└── views
    ├── index.html
```

Please visit the documentation to check more details https://marcuxyz.github.io/mvc-flask

## Changelog

### Version 2.9.0 - Test Infrastructure Refactor

#### Test Structure Improvements
- **Major Test Refactor**: Converted all test files from class-based to function-based structure for improved readability and maintainability
- **Comprehensive Test Coverage**: Enhanced test coverage across all major components including:
  - Controllers (CRUD operations, error handling, integration workflows)
  - Callbacks (middleware system, hooks, configuration)
  - Helpers (HTML input method helpers, method override functionality)
  - Integration (complete workflows, performance, security)
  - Version management (semantic versioning, metadata validation)
- **Test Organization**: Reorganized test files with clear naming convention using `test_*_functional.py` pattern
- **Performance Testing**: Added comprehensive performance benchmarking and optimization validation
- **Security Testing**: Enhanced security validation including CSRF protection, method override security, and input sanitization

#### Code Quality Enhancements
- **Comment Cleanup**: Removed unnecessary comments throughout test codebase while preserving critical documentation
- **English Standardization**: Ensured all code, comments, and documentation use native American English
- **Test Utilities**: Improved test helper functions and utilities for better test maintainability
- **Error Handling**: Enhanced error handling validation across all test scenarios

#### Developer Experience
- **Improved Readability**: Function-based tests are more straightforward to read and understand
- **Better Isolation**: Each test function is completely isolated, reducing interdependencies
- **Faster Development**: Simplified test structure enables faster test development and debugging
- **Enhanced Documentation**: Added comprehensive test documentation outlining best practices and patterns

#### Technical Improvements
- **Memory Optimization**: Added memory usage stability testing to prevent memory leaks
- **Concurrent Testing**: Enhanced concurrent access simulation and testing
- **Configuration Testing**: Comprehensive testing across different Flask configuration scenarios
- **Scalability Validation**: Added large dataset handling and scalability characteristic testing

#### Migration Notes
- All existing test functionality remains intact
- No breaking changes to core MVC Flask functionality
- Test execution performance improved due to simplified structure
- Enhanced debugging capabilities with clearer test failure reporting

This release significantly improves the development experience and code quality while maintaining full backward compatibility with existing applications.
