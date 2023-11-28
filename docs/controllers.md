# Controllers

Now that configured routes, the `home_controller.py` file must contain the HomeController class, registering the action.

from flask import render_template

```python
class HomeController:
    def index(self):
        return render_template("index.html")
```

## Callbacks

You can use the callbacks as `before_request` and `after_request` to called the function before or after request... See:

```python
class HomeController:
    before_request = dict(callback="hi", actions="index")

    def index(self):
        return "home"

    def hi(self):
        ...
```

The method `hi(self)` will be called whenever the visitors access the controller.

