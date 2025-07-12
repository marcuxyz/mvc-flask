# Router

You can create routes in `app/routes.py` and after creating file, you can start to register routes, e.g:

```python
from flask_mvc import Router

Router.get("/", "home#index")
```

The same must be done to `POST`, `PUT` and `DELETE` methods. E.g: `Router.post("/messages", "messages#create")`

The first param represents the relative path and the second represents the controller#action. Remember that we are working with an MVC pattern, so we have a controller and action.

The controller can be created in `app/controllers` and action is a method of the controller.

You can use `Router.all()` to register all routes of CRUD.

```python
Router.all("messages")
```

The previous command produces this:

```python
messages.create  POST        /messages
messages.delete  DELETE      /messages/<id>
messages.edit    GET         /messages/<id>/edit
messages.index   GET         /messages
messages.new     GET         /messages/new
messages.show    GET         /messages/<id>
messages.update  PATCH, PUT  /messages/<id>
```

You can also use only parameters to control routes, e.g:

```python
Router.all("messages", only="index show new create")
```

The previous command produces this:

```python
messages.index   GET      /messages
messages.show    GET      /messages/<id>
messages.new     GET      /messages/new
messages.create  POST     /messages
```

The parameter only accept `string` or `array`, so, you can use `only=["index", "show", "new", "create"]` or `only='index show new create'`

## Namespaces

You can use namespaces to group the routes.

```python
from flask_mvc import Router

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

The previous command produces this:

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
