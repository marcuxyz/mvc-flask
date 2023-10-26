import os
from black import format_str, FileMode

import click
from flask.cli import with_appcontext


BASEDIR = os.path.dirname(os.path.dirname(__file__))
MVC_DIR = os.path.join(BASEDIR, "mvc_flask")


@click.group()
def generate():
    """Use this command for generate controller, models, auth and etc."""
    pass


@generate.command()
@click.argument("name")
@with_appcontext
def controller(name):
    """Generate controller, e.g: flask generate controller home"""
    controller_template = os.path.join(MVC_DIR, "templates", "controller.md")
    controller_filename = f"{name}_controller.py".lower()
    file_content = None

    with open(controller_template, "r") as controller:
        file_content = controller.read()

    file = os.path.join(os.getcwd(), "app", "controllers", controller_filename)

    if os.path.exists(file):
        print(
            "\033[31m conflict"
            + f"\033[37m app/controllers/{controller_filename} already exists"
        )
        quit()

    with open(file, "w+") as f:
        string = file_content.format(name=f"{name}".title())
        content = format_str(string, mode=FileMode())
        f.write(content)

    print(
        "\033[92m create" + f"\033[37m app/controllers/{controller_filename}"
    )


def init_app(app):
    app.cli.add_command(generate)
