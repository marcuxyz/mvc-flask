![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/marcuxyz/mvc_flask) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/marcuxyz/mvc_flask/unit%20test) ![GitHub](https://img.shields.io/github/license/marcuxyz/mvc_flask) ![PyPI - Downloads](https://img.shields.io/pypi/dm/mvc_flask) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mvc_flask) ![PyPI](https://img.shields.io/pypi/v/mvc_flask)

You can use the mvc pattern in your flask application using this extension.

# Installation

Run the follow command to install `mvc_flask`:

```shell
$ pip install mvc_flask
```

# Configuration

To configure the `mvc_flask` you need import and register in your application:


```python
from mvc_flask import FlaskMVC
mvc = FlaskMVC()
```

Or use factory function

```python
mvc = FlaskMVC()

def create_app():
  ...
  mvc.init_app(app)
```

By default the `mvc_flask` assumes that your application directory will be `app`, but, you can change it. Passing the object of configuration:

```python
app.config["FLASK_MVC_DIR"] = "sample_app"
```

# Create MVC Pattern

`mvc_flask` assumes that your application will have these characteristics: 

```text
app
├── __ini__.py
├── controllers
│   ├── contact_controller.py
│   └── home_controller.py
├── model
├── routes.json
└── views
    ├── index.html
    └── post
        └── new.html
```

The routes will be something as:

```json
[
  {
    "method": "GET",
    "path": "/",
    "controller": "home",
    "action": "index"
  },
  {
    "method": "get",
    "path": "/new",
    "controller": "home",
    "action": "new"
  },
  {
    "method": "post",
    "path": "/create",
    "controller": "home",
    "action": "create"
  },
  {
    "method": "GET",
    "path": "/contact",
    "controller": "contact",
    "action": "index"
  }
]
```

# Tests

You can run the tests, executing the follow command:

```shell
$ make test
```

![](/prints/test_runner.png)
