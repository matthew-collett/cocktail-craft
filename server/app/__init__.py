import os
from flask import Flask
from flask_cors import CORS
from server.app.config import config
from server.app.api.routes import api as api_blueprint
from server.app.extensions import cache


def create_app():
    # setup app
    app = Flask(__name__)
    flask_env = os.getenv('FLASK_ENV')
    config_class = config.get(flask_env)
    app.config.from_object(config_class)

    # register blueprints
    app.register_blueprint(api_blueprint)

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
