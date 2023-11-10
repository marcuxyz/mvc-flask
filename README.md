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
