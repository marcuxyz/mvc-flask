# Usage

We know that the HTML form doesn't send the payload for methods other than Get and Post. But, the FLASK MVC does the work for you, everything you need is to add the tag in the HTML template. Look:

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
  <form action="{{ url_for('messages.update', id=message.id) }}" method="post">
    {{ method('PUT') }}
    <input type="text" name="title" id="title" value="Yeahh!">

    <input type="submit" value="send">
  </form>
{% endblock %}
```

You can use the `{{ method('PUT|DELETE|PATCH') }}` to creates supports for PUT and DELETE methods to forms.
