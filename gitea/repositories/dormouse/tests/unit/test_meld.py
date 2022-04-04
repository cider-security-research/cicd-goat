import pytest
from flask_meld.component import get_component_class


def test_module_load_with_app_factory(app_factory_ctx):
    component_class = get_component_class("search")
    assert component_class.__name__ == "Search"


def test_module_load_with_single_file_app(app_ctx):
    component_class = get_component_class("search")
    assert component_class.__name__ == "Search"


def test_module_load_exception_with_single_file_app(app_ctx):
    with pytest.raises(FileNotFoundError):
        get_component_class("non-existant-module")


def test_module_load_exception_with_app_factory(app_factory_ctx):
    with pytest.raises(FileNotFoundError):
        get_component_class("non-existant-module")


def test_module_load_exception_without_user_specified_dir(app):
    app.config["MELD_COMPONENT_DIR"] = None
    with app.app_context():
        with pytest.raises(FileNotFoundError):
            get_component_class("non-existant-module")
