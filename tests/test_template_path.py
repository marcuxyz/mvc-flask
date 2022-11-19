from flask import Flask
from ward import each, test
from mvc_flask.__init__ import FlaskMVC

@test("app should have template_path equal to './app/views' if it set", tags=["Flask.template_path"])
def _():
  expected_path = './app/views'
  app = Flask(__name__, template_folder = expected_path)
  FlaskMVC(app, path = 'app')
  assert app.template_path == expected_path
