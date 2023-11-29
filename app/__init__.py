# app/__init__.py
from flask import Flask
from .main.routes import main as main_blueprint

def create_app():
  # setup app
  app = Flask(__name__)
  app.config.from_object('config.Config')

  # register blueprints
  app.register_blueprint(main_blueprint)

  return app
