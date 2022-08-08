![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/marcuxyz/mvc_flask) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/marcuxyz/mvc_flask/unit%20test) ![GitHub](https://img.shields.io/github/license/marcuxyz/mvc_flask) ![PyPI - Downloads](https://img.shields.io/pypi/dm/mvc_flask) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mvc_flask) ![PyPI](https://img.shields.io/pypi/v/mvc_flask)

You can use the mvc pattern in your flask application using this extension.

This real world implementation `FLASK MVC` example: https://github.com/negrosdev/negros.dev 

## Installation

Run the follow command to install `mvc_flask`:

```shell
$ pip install mvc_flask
```

## Configuration

To configure the `mvc_flask` you need import and register in your application, e.g:


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
**If you can use other directory, you can use the `path` paramenter when the instance of FlaskMVC is initialized. E.g:**

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

## Router
You can create routes in `app/routes.py` and after create file, you can start register routes, e.g:

```python
from mvc_flask import Router

Router.get("/", "home#index")
```

The same must be make done to `POST`, `PUT` and `DELETE` methods. E.g: `Router.post("/messages", "messages#create")`

The first param represent the relative path and second represent the `controller#action`. Remember that we are working with `MVC pattern`, so we have `controller` and `action`.

The `controller` can be created in `app/controllers` and action is method of `controller`.

You can use `Router.all()` to register all routes of `CRUD`.

```python
Router.all("messages")
```

The previous command produce this:

```shell
messages.create  POST        /messages
messages.delete  DELETE      /messages/<id>
messages.edit    GET         /messages/<id>/edit
messages.index   GET         /messages
messages.new     GET         /messages/new
messages.show    GET         /messages/<id>
messages.update  PATCH, PUT  /messages/<id>
```

You can also use `only parameter` to controll routes, e.g:

```python
Router.all("messages", only="index show new create")
```

The previous command produce this:

```shell
messages.index   GET      /messages
messages.show    GET      /messages/<id>
messages.new     GET      /messages/new
messages.create  POST     /messages
```

The paramenter `only` accept `string` or `array`, so, you can use `only=["index", "show", "new", "create"]`

## Controller

Now that configure routes, the `home_controller.py` file must contain the `HomeController` class, registering the `action`, e.g:  

```python
class HomeController:
    def index(self):
        return view("index.html")
```

If you have question, please, check de [app](https://github.com/marcuxyz/mvc-flask/tree/main/tests/app) directory to more details.

To use the hooks as `before_request`, `after_request` and etc... Just describe it in the controller, see:

```python
class HomeController:
    before_request = ["hi"]

    def index(self):
        return "home"

    def hi(self):
        ...
```

The previous example describes the `hi(self)` will be called every times that the visitors access the controller.

## Views

Flask use the `templates` directory by default to store `HTMLs` files. However, using the `mvc-flask` the default becomes `views`. You can use the `app/views` directory to stores templates.
