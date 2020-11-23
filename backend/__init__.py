import os

from flask import Flask
from backend.settings.base import BACKEND_DIR
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None, debug: bool = False):
    # create and configure the app
    app = Flask("LTV URL Shortener")

    if test_config is None and debug is False:
        app.config.from_pyfile(
            os.path.join(BACKEND_DIR, "settings", "base.py"), silent=True
        )
    elif test_config is None and debug is True:
        app.config.from_pyfile(
            os.path.join(BACKEND_DIR, "settings", "base.py"), silent=False
        )
    else:
        app.config.from_mapping(test_config)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # a simple page that says hello
    @app.route("/")
    def hello():
        return "Hello, World!"

    with app.app_context():
        db.init_app(app)
        return app


flask_app = create_app()
