# Controllers

Now that configured routes, the `home_controller.py` file must contain the HomeController class, registering the action.

from flask import render_template

```python
class HomeController:
    def index(self):
        return render_template("index.html")
```

If you have a question, please, check the app directory for more details.

To use the hooks as `before_request`, `after_request`, etc... Just describe it in the controller, see:

```python
class HomeController:
    before_request = ["hi"]

    def index(self):
        return "home"

    def hi(self):
        ...
```

The method `hi(self)` will be called whenever the visitors access the controller.

