from string import Template

requirements_template = Template(
    """
Flask>=0.9
Flask-Meld>=0.7.0
python-dotenv>=0.17.0
"""
)

config_template = Template(
    """
import os
import secrets


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
"""
)

init_template = Template(
    """
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
    """
)

env_template = Template(
    """
SECRET_KEY=$secret_key
FLASK_ENV=development
"""
)

wsgi_template = Template(
    """
from app import create_app

app = create_app(config_name='production')
socketio = app.socketio


if __name__ == "__main__":
    socketio.run(app=app)
"""
)

base_html_template = Template(
    """
<html>
    <head>
        <title>Welcome to Flask-Meld</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">

        {% block head_scripts %}
        {% endblock %}
    </head>
    <body>
        {% meld_scripts %}

        {% block content %}

        {% endblock %}

        {% block page_scripts %}
        {% endblock %}
    </body>
</html>
"""
)

index_html_template = Template(
    """
{% extends "base.html" %}

{% block content %}
<h1>Flask-Meld</h1>
{% endblock %}
"""
)

components = Template(
    """
from flask_meld.component import Component


class $class_name(Component):
    example_variable = False

    def example_function(self):
        self.example_variable = not self.example_variable
"""
)

components_template = Template(
    """
<div>
    <button meld:click="example_function">Toggle</button>
    <input type="text" meld:model="example_variable" readonly></input>
</div>
"""
)
