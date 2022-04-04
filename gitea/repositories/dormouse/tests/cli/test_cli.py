from pathlib import Path
from flask_meld.component import get_component_class
from flask_meld.cli import (
    generate_meld_app,
    generate_file_with_content,
    generate_meld_component,
)
from flask_meld.templates import requirements_template
from expectations import expected_requirements


def test_generate_file_content(tmpdir_factory):
    test_dir = tmpdir_factory.mktemp("test_file_content_generator")
    path = generate_file_with_content(
        test_dir, "requirements.txt", requirements_template.template
    )
    with path.open("r") as f:
        contents = f.read()
        assert contents == expected_requirements


def test_creates_component_dir(generate_app):
    # generate_app fixture creates directory structure of project
    expected_path = Path(generate_app / "test_project" / "app" / "meld" / "components")
    assert expected_path.is_dir()


def test_creates_tests_dir(generate_app):
    expected_path = Path(generate_app / "test_project" / "tests")
    assert expected_path.is_dir()


def test_creates_tests_static(generate_app):
    expected_path = Path(generate_app / "test_project" / "app" / "static" / "images")
    assert expected_path.is_dir()


def test_creates_templates_dir(generate_app):
    expected_path = Path(generate_app / "test_project" / "app" / "meld" / "templates")

    assert expected_path.is_dir()


def test_creates_config_file(generate_app):
    expected_path = Path(generate_app / "test_project" / "config.py")
    assert expected_path.exists()


def test_creates_init_file(generate_app):
    expected_path = Path(generate_app / "test_project" / "app" / "__init__.py")
    assert expected_path.exists()


def test_creates_wsgi_file(generate_app):
    expected_path = Path(generate_app / "test_project" / "app" / "wsgi.py")
    assert expected_path.exists()


def test_creates_env_file(generate_app):
    expected_path = Path(generate_app / "test_project" / ".env")
    assert expected_path.exists()


def test_creates_base_html_file(generate_app):
    expected_path = Path(
        generate_app / "test_project" / "app" / "templates" / "base.html"
    )
    assert expected_path.exists()


def test_generate_component_file_exists(app_factory_ctx, tmpdir_factory):
    components_path = Path(
        tmpdir_factory.getbasetemp() / "app_factory_project" / "app" / "meld"
    )
    component_name = "test_one"
    generate_meld_component(component_name)
    generated_component_path = Path(
        components_path / "components" / f"{component_name}.py"
    )
    component_class = get_component_class("test_one")
    assert component_class.__name__ == "TestOne"
    assert generated_component_path.exists()

    component_name = "test_two"
    generate_meld_component(component_name)
    generated_component_path = Path(
        components_path / "components" / f"{component_name}.py"
    )
    component_class = get_component_class("test_two")
    assert component_class.__name__ == "TestTwo"
    assert generated_component_path.exists()

    component_name = "Test_Two"
    component = generate_meld_component(component_name)
    assert not component
