![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/marcuxyz/mvc_flask) ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/marcuxyz/mvc_flask/unit%20test) ![GitHub](https://img.shields.io/github/license/marcuxyz/mvc_flask) ![PyPI - Downloads](https://img.shields.io/pypi/dm/mvc_flask) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mvc_flask) ![PyPI](https://img.shields.io/pypi/v/mvc_flask)

You can use the mvc pattern in your flask application using this extension.

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

## Namespace
In `app/routes.py`, you can start register namespace, e.g:

```python
from mvc_flask import Router

api = Router.namespace("/api/v1")

api.get("/health", "health#index")

api.all("user")

posts = api.namespace("/posts")
posts.get("", "posts#index")
posts.post("", "posts#create")
posts.get("/<id>", "posts#show")
posts.put("/<id>", "posts#update")
posts.get("/<id>", "posts#delete")

```

The source produce this:
```shell
health.index     GET         /api/v1/health
posts.create     POST        /api/v1/posts
posts.delete     GET         /api/v1/posts/<id>
posts.index      GET         /api/v1/posts
posts.show       GET         /api/v1/posts/<id>
posts.update     PATCH, PUT  /api/v1/posts/<id>
user.create      POST        /api/v1/user
user.delete      DELETE      /api/v1/user/<id>
user.edit        GET         /api/v1/user/<id>/edit
user.index       GET         /api/v1/user
user.new         GET         /api/v1/user/new
user.show        GET         /api/v1/user/<id>
user.update      PATCH, PUT  /api/v1/user/<id>
```

## Controller

Now that configure routes, the `home_controller.py` file must contain the `HomeController` class, registering the `action`, e.g:

```python
from flask import render_template

class HomeController:
    def index(self):
        return render_template("index.html")
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

## PUT / PATCH / DELETE ...

we know that the HTML form doesn't send payload to `action` with `put` or `delete` method as attribute of `form tag`. But,
the `FLASK MVC` does the work for you, everything you need is add the tag in HTML template. Look:

```python
# app/controllers/messages_controller.py

from flask import render_template, redirect, url_for, flash, request

class MessagesController:
    def edit(self, id):
        message = Message.query.get(id)

        return render_template("messages/edit.html", message=message)

    def update(self, id):
        message = Message.query.get(id)
        message.title = request.form.get('title')

        db.session.add(message)
        db.session.commit()
        flash('Message sent successfully!')

        return redirect(url_for(".edit"))
```


```jinja
<!--  app/views/messages/edit.html -->

{% block content %}
  <form action="{{ url_for('messages.update', id=message.id) }}" method="POST">
    <input type="hidden" name="_method" value="put">
    <input type="text" name="title" id="title" value="Yeahh!">

    <input type="submit" value="send">
  </form>
{% endblock %}
```

The `<input type="hidden" name="_method" value="put">` is necessary to work sucessfully!

## Views

Flask use the `templates` directory by default to store `HTMLs` files. However, using the `mvc-flask` the default becomes `views`. You can use the `app/views` directory to stores templates.

## Result

Adding result session to show image that is represented by project build with library.

<img width="2560" alt="Captura de Tela 2023-04-05 às 23 23 12" src="https://user-images.githubusercontent.com/9499562/230256574-5c33ef3a-a584-4878-bc59-b174be4a2a65.png">
