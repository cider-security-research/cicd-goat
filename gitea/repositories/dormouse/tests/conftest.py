import os
import shutil
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from time import sleep

import pytest
from flask import Flask
from meld_test_project import create_app

from flask_meld import Meld
from flask_meld.cli import generate_meld_app


def init_app(app_dir):
    meld = Meld()
    app = Flask(app_dir)
    app.secret_key = __name__
    meld.init_app(app)
    return app


"""
Can we pass in a test directory to the application?
"""


@pytest.fixture(scope="session")
def app():
    app = create_app()
    return app


@pytest.fixture(scope="module")
def app_mod(tmpdir_factory):
    # create directory structure of project/meld/components
    app_dir = tmpdir_factory.mktemp("project")
    meld = Meld()
    app = Flask(f"{app_dir}", root_path=app_dir)
    create_test_component(app_dir)
    app.secret_key = __name__
    meld.init_app(app)
    return app


@pytest.fixture(scope="session")
def app_factory(tmpdir_factory):
    # create directory structure of project/app/meld/components
    project_dir = tmpdir_factory.mktemp("app_factory_project", numbered=False)
    Path(f"{project_dir}/app").mkdir(parents=True, exist_ok=True)
    app_dir = Path(f"{project_dir}/app")

    create_test_component(f"{app_dir}")
    factory_init = Path(f"{app_dir}/__init__.py")
    write_init_contents(factory_init)
    spec = spec_from_file_location(f"{app_dir}", f"{app_dir}/__init__.py")
    test = module_from_spec(spec)
    spec.loader.exec_module(test)

    app = test.create_app("test_config")
    app.root_path = app_dir
    return app


@pytest.fixture(scope="function")
def browser_client(pytestconfig):
    current_test = os.getenv('PYTEST_CURRENT_TEST')
    base = pytestconfig.rootdir
    meld_base = Path(f"{base}/meld_test_project/meld")
    index = Path(f"{base}/meld_test_project/templates/index.html")

    templates = Path(f"{meld_base}/templates/")
    components = Path(f"{meld_base}/components/")

    component_name_path = Path(current_test.split("::")[0].split(".")[0])

    component_base_path = Path(base, "/".join(component_name_path.parts[:-1]))
    component_name = component_name_path.parts[-1].replace("test_", "")

    template = Path(f"{component_base_path}/{component_name}.html")
    component = Path(f"{component_base_path}/{component_name}.py")

    shutil.copyfile(template, f"{templates}/{component_name}.html")
    shutil.copyfile(component, f"{components}/{component_name}.py")
    insert_component_to_index(index, component_name)


@pytest.fixture
def client(app_factory):
    return app_factory.test_client()


@pytest.fixture
def app_factory_ctx(app_factory):
    with app_factory.app_context() as ctx:
        yield ctx


@pytest.fixture
def app_ctx(app_mod):
    with app_mod.app_context() as ctx:
        yield ctx


@pytest.fixture(scope="module")
def generate_app(tmp_path_factory):
    name = "test_project"
    generate_meld_app(name, tmp_path_factory.getbasetemp() / name)
    return tmp_path_factory.getbasetemp()


def create_test_component(app_dir):
    Path(f"{app_dir}/meld/components").mkdir(parents=True, exist_ok=True)
    Path(f"{app_dir}/meld/templates").mkdir(parents=True, exist_ok=True)
    component = Path(f"{app_dir}/meld/components/search.py")
    write_component_class_contents(component)
    return app_dir


def insert_component_to_index(index, component_name):
    with index.open("w") as f:
        class_def = [
            '{% extends "base.html" %}',
            '{% block content %}',
            f"{{% meld '{component_name}' %}}"
            '{% endblock %}',
        ]
        f.writelines(f"{line}\n" for line in class_def)


def write_component_class_contents(component_file):
    with component_file.open("w") as f:
        class_def = [
            "from flask_meld.component import Component",
            "class Search(Component):",
            "\tstate=''",
        ]
        f.writelines(f"{line}\n" for line in class_def)


def write_init_contents(factory_init):
    with factory_init.open("w") as f:
        class_def = [
            "from flask import Flask",
            "from flask_meld import Meld",
            "meld = Meld()",
            "def create_app(config_name):",
            "\tapp = Flask(__name__)",
            '\tapp.config["SECRET_KEY"] = "super_secret_test_key"',
            "\tmeld.init_app(app)",
            "\treturn app",
        ]
        f.writelines(f"{line}\n" for line in class_def)
