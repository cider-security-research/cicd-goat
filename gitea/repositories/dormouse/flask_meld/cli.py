import os
import secrets
from pathlib import Path
from flask.cli import with_appcontext
from flask import current_app

import click

from flask_meld.templates import (
    base_html_template,
    config_template,
    components,
    components_template,
    env_template,
    index_html_template,
    init_template,
    requirements_template,
    wsgi_template,
)


@click.group()
def meld():
    """Flask-Meld specific commands"""


@meld.group()
def new():
    """Commands for new keyword"""


@new.command("project")
@click.argument("name")
def project(name):
    """Create a new flask-meld app with application defaults"""
    click.echo(f"Creating app {name}")
    generate_meld_app(name)


@new.command("component")
@click.argument("name")
@with_appcontext
def component(name):
    """Create a new component"""
    click.echo(f"Creating component '{name}'.")
    generate_meld_component(name)


def generate_meld_app(name, base_dir=None):
    try:
        if not base_dir:
            base_dir = Path.cwd() / name
        os.makedirs(base_dir / "app" / "meld" / "components")
        os.makedirs(base_dir / "app" / "meld" / "templates")
        os.makedirs(base_dir / "app" / "templates")
        os.makedirs(base_dir / "app" / "static" / "images")
        os.makedirs(base_dir / "app" / "static" / "css")
        os.makedirs(base_dir / "tests")
        generate_file_with_content(
            base_dir, "requirements.txt", requirements_template.template
        )
        generate_file_with_content(base_dir, "config.py", config_template.template)
        generate_file_with_content(base_dir, "app/__init__.py", init_template.template)
        generate_file_with_content(base_dir, "app/wsgi.py", wsgi_template.template)
        generate_file_with_content(
            base_dir, "app/templates/base.html", base_html_template.template
        )
        generate_file_with_content(
            base_dir, "app/templates/index.html", index_html_template.template
        )

        generated_secret_key = secrets.token_hex(16)
        generate_file_with_content(
            base_dir, ".env", env_template.substitute(secret_key=generated_secret_key)
        )
    except OSError:
        pass


def generate_meld_component(name):
    name = name.lower()
    try:
        base_dir = Path(current_app.root_path)
        components_dir = base_dir / "meld" / "components"
        templates_dir = base_dir / "meld" / "templates"

        if not (os.path.exists(components_dir) and os.path.exists(templates_dir)):
            click.echo(f"Failed. Could not find: {components_dir} or {templates_dir}")
            return False

        name_split = name.split("_")

        class_name = ""
        for name_seq in name_split:
            class_name += name_seq.capitalize()

        component = components_dir / f"{name}.html"
        if os.path.exists(component):
            click.echo(f"Failed. Component '{name}' already exists.")
            return False

        template = templates_dir / f"{name}.html"
        if os.path.exists(template):
            click.echo(f"Failed. Template '{template}' already exists.")
            return False

        generate_file_with_content(
            components_dir, f"{name}.py", components.substitute(class_name=class_name)
        )
        generate_file_with_content(
            templates_dir, f"{name}.html", components_template.template
        )
        click.echo(f"Component '{name}' successfully created.")

    except OSError:
        click.echo(
            "Failed. Unable to write to disk. Verify you have sufficient permissions."
        )
        return False


def generate_file_with_content(path, filename, file_contents):
    path = Path(f"{path}/{filename}")
    with open(path, "w") as f:
        f.write(file_contents)
    return path


if __name__ == "__main__":
    meld()
