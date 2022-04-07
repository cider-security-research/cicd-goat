from bs4 import BeautifulSoup
from jinja2 import Template

from flask_meld.component import Component
from flask_meld.message import listen


class ExampleComponent(Component):
    test_var = "test"
    test_var_2 = 12

    def test_method(self):
        return "method_test"


def test_component_variables_are_valid():
    component = ExampleComponent()
    expected_attributes = ["errors", "test_var", "test_var_2"]
    assert list(component._attributes().keys()) == expected_attributes


def test_component_methods_are_valid():
    component = ExampleComponent()
    expected_methods = ["test_method"]
    assert list(component._functions().keys()) == expected_methods


class DirectTemplateComponent(Component):
    text = ""
    texts = []

    def __init__(self, template_string: str, **kwargs):
        super().__init__(**kwargs)
        self._template = Template(template_string)

    def _render_template(self, template_name: str, context_variables: dict):
        return self._template.render(context_variables)


def test_render_model_value(app):
    # GIVEN
    template = """
    <div class="row">
        <input type="text" meld:model="text">
        <button class="btn right" meld:click="add">+</button>
        <span id="text-id">{{ text }}</span>
    </div>
    """
    component = DirectTemplateComponent(template)

    # When
    app.config["SERVER_NAME"] = "localhost"
    with app.app_context():
        component.text = "hello"
        rendered_html = component.render("DirectTemplateComponent")

    # Then
    soup = BeautifulSoup(rendered_html, features="html.parser")
    assert soup.find("span").text == "hello"


def test_render_model_defer_value(app):
    # GIVEN
    template = """
    <div class="row">
        <input type="text" meld:model.defer="text">
        <button class="btn right" meld:click="add">+</button>
        <span id="text-id">{{ text }}</span>
    </div>
    """
    component = DirectTemplateComponent(template)

    # When
    app.config["SERVER_NAME"] = "localhost"
    with app.app_context():
        component.text = "hello"
        rendered_html = component.render("DirectTemplateComponent")

    # Then
    soup = BeautifulSoup(rendered_html, features="html.parser")
    assert soup.find("span").text == "hello"


class CustomEventComponent(Component):
    @listen("foo")
    def foo(self):
        return "foo"

    @listen("foo", "bar")
    def bar(self):
        return "bar"

    def baz(self):
        return "baz"

def test_listeners():
    assert CustomEventComponent._listeners() == {
        "foo": ["foo", "bar"],
        "bar": ["bar"]
    }
