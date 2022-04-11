import os
from pathlib import Path

import jinja2
import pkg_resources
from flask import send_from_directory
from flask_socketio import SocketIO

from .message import process_init, process_message
from .tag import MeldScriptsTag, MeldTag


class Meld:
    def __init__(self, app=None, socketio=None, **kwargs):
        self.app = app

        if app is not None:
            self.init_app(app, socketio=socketio, **kwargs)

    def send_static_file(self, filename):
        """Send a static file from the flask-meld js directory."""
        directory = Path(pkg_resources.resource_filename('flask_meld', 'meld_js_src'))
        return send_from_directory(directory, filename)

    def init_app(self, app, socketio=None, **kwargs):
        app.jinja_env.add_extension(MeldTag)
        app.jinja_env.add_extension(MeldScriptsTag)

        # Load templates from template dir or app/meld/templates
        custom_template_loader = jinja2.ChoiceLoader([
            app.jinja_loader,
            jinja2.FileSystemLoader(os.path.join(app.root_path, 'meld/templates')),
        ])

        app.jinja_loader = custom_template_loader
        if socketio:
            app.socketio = socketio
        else:
            app.socketio = SocketIO(app, **kwargs)

        meld_dir = app.config.get("MELD_COMPONENT_DIR", None)
        if meld_dir:
            if not os.path.isabs(meld_dir):
                directory = os.path.abspath(os.path.join(app.root_path, meld_dir))
                app.config["MELD_COMPONENT_DIR"] = directory

        if not app.config.get("SECRET_KEY"):
            raise RuntimeError(
                "The Flask-Meld requires the 'SECRET_KEY' config " "variable to be set"
            )

        @app.route("/meld_js_src/<path:filename>")
        def meld_static_file(filename):
            return self.send_static_file(filename)

        @app.socketio.on("meld-message")
        def meld_message(message):
            """meldID, action, componentName"""
            result = process_message(message)
            app.socketio.emit("meld-response", result)

        @app.socketio.on("meld-init")
        def meld_init(message):
            return process_init(message)
