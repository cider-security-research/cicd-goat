
from flask import Flask, render_template
from config import config
from flask_meld import Meld
# from .db import db
# from app import models

# extensions
meld = Meld()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # db.init_app(app)

    meld.init_app(app)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
    