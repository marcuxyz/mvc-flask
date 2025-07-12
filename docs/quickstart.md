# Quickstart

To start the use `flask_mvc` you need to import and register in your application, e.g:

```python
from flask import Flask
from flask_mvc import FlaskMVC

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

Now, you can use src as the default directory to prepare your application. Your structure should look like this:

```python
app
├── __ini__.py
├── controllers
│   └── home_controller.py
├── routes.py
└── views
    ├── index.html
```

**By default, the flask_mvc assumes that your application directory will be app and if it doesn't exist, create it! If you can use another directory, you can use the path parameter when the instance of FlaskMVC is initialized. E.g:**

```python
mvc = FlaskMVC()

def create_app():
  ...
  mvc.init_app(app, path='src')
```

