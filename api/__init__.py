# api/__init__.py
from flask import Flask
from flask_cors import CORS
from api.config import config
import os
from .main.routes import main as main_blueprint
from .utils.cache import cache


def create_app():
    # setup app
    app = Flask(__name__)
    flask_env = os.getenv('FLASK_ENV')
    config_class = config.get(flask_env)
    app.config.from_object(config_class)

    # register blueprints
    app.register_blueprint(main_blueprint)

    # configure cors
    CORS(app, resources={r"/api/*": {
        "origins": app.config['CORS_ORIGINS'],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": app.config['CORS_HEADERS'],
        "supports_credentials": app.config['CORS_SUPPORTS_CREDENTIALS'],
        "max_age": app.config['CORS_MAX_AGE'],
    }})

    # setup cache
    cache.init_app(app)

    return app
