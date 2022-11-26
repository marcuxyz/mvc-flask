import os
import platform
import shutil
import subprocess
from distutils.dir_util import copy_tree
from black import format_str, FileMode


import click
from flask.cli import with_appcontext


BASEDIR = os.path.dirname(os.path.dirname(__file__))
MVC_DIR = os.path.join(BASEDIR, "mvc_flask")


@click.group()
def generate():
    """ Use this command for generate controller, models, auth and etc. """
    pass

@generate.command()
@click.argument('name')
@with_appcontext
def controller(name):
    """ Generate controller, e.g: flask generate controller home """
    controller_template = os.path.join(MVC_DIR, "templates", "controller.md")
    file_content = None

    with open(controller_template, 'r') as controller:
        file_content = controller.read()

    path = os.path.join(os.getcwd(), "app", "controllers", f"{name}_controller.py".lower())
    with open(path, 'w+') as f:
        string = file_content.format(name=f"{name}".title())
        content = format_str(string, mode=FileMode())
        f.write(content)


# @mvc.command()
# @click.option("--init", default=False)
# @with_appcontext
# def init(init):
#     """ Configure your project. """
#     front_original = os.path.join(BASEDIR, "flask_vuejs")

#     if (
#         os.path.isdir("frontend")
#         or os.path.isfile("package.json")
#         or os.path.isfile("webpack.config.js")
#     ):
#         return click.echo(
#             f"You already configured your application. Try running {Fore.GREEN}\
# flask vue restore {Fore.WHITE}command before running this command again."
#         )

#     # copy directories locals to application directory
#     copy_tree(os.path.join(front_original, "bootstrap"), ".")

#     return click.echo(
#         f"Everything went well, now you need to execute the following commands:\
# \n\n{Fore.GREEN}$ flask vue install\n{Fore.GREEN}$ flask vue compile\n"
#     )


# @vue.command()
# @with_appcontext
# def install():
#     """ Install the vue packages """
#     subprocess.check_call("npm i --silent", shell=True)


# @vue.command()
# @with_appcontext
# def compile():
#     """ Compile assets only once """
#     subprocess.check_call("npm run build", shell=True)
#     return click.echo("\nCompiled!\n")


# @vue.command()
# @with_appcontext
# def watch():
#     """ Watch the vue files """
#     text = "Before execute this command, you should be set FLASK_ENV as development mode. \n\n$ {} FLASK_ENV=development\n"

#     if os.getenv("FLASK_ENV") == "development":
#         subprocess.check_call("npm run watch", shell=True)

#     if platform.system() == "Windows":
#         return click.echo(text.format("set"))
#     return click.echo(text.format("export"))


# @vue.command()
# def restore():
#     """ Restore factory application """
#     files = ["webpack.config.js", "package.json", "package-lock.json"]
#     dirs = ["frontend", "node_modules"]

#     for f in files:
#         if os.path.isfile(f):
#             os.remove(f)

#     for d in dirs:
#         if os.path.isdir(d):
#             shutil.rmtree(d)

#     return click.echo(f"Restored successfully!")


def init_app(app):
    app.cli.add_command(generate)