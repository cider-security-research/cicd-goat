import os
import uuid
from importlib.util import module_from_spec, spec_from_file_location
from itertools import groupby
from operator import itemgetter

import orjson
from bs4 import BeautifulSoup
from bs4.element import Tag
from bs4.formatter import HTMLFormatter
from flask import current_app, jsonify, render_template
from jinja2.exceptions import TemplateNotFound


def convert_to_snake_case(s):
    s.replace("-", "_")
    return s


def convert_to_camel_case(s):
    s = convert_to_snake_case(s)
    return "".join(word.title() for word in s.split("_"))


def get_component_class(component_name):
    """
    Get a component class based on a component name.
    """
    module_name = convert_to_snake_case(component_name)
    class_name = convert_to_camel_case(module_name)
    module = get_component_module(module_name)
    component_class = getattr(module, class_name)

    return component_class


def get_component_module(module_name):
    """
    Get the module from the meld/components directory or from a
    custom location using the config with `MELD_COMPONENT_DIR`.
    """
    user_specified_dir = current_app.config.get("MELD_COMPONENT_DIR", None)

    if not user_specified_dir:
        try:
            full_path = os.path.join(
                current_app.root_path, "meld", "components", module_name + ".py"
            )
            module = load_module_from_path(full_path, module_name)
        except FileNotFoundError:
            full_path = os.path.join("meld", "components", module_name + ".py")
            module = load_module_from_path(full_path, module_name)
    else:
        try:
            full_path = os.path.join(user_specified_dir, module_name + ".py")
            module = load_module_from_path(full_path, module_name)
        except FileNotFoundError:
            full_path = os.path.join(
                user_specified_dir, "components", module_name + ".py"
            )
            module = load_module_from_path(full_path, module_name)
    return module


def load_module_from_path(full_path, module_name):
    """
    Load a module given from a given path based on the name of the module
    """
    spec = spec_from_file_location(module_name, full_path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


CSRF_TOKEN_ATTR = "csrf_token"


class Component:
    """
    The meld Component class does most of the heavy lifting to handle data-binding,
    template context variable binding, template rendering and additional hooks.
    """

    def __init__(self, id=None, **kwargs):
        if not id:
            id = uuid.uuid4()
        self.errors = {}
        self._form = None
        self.__dict__.update(**kwargs)
        self.id = id

        if hasattr(self, "form"):
            self._bind_form(kwargs)

    def __repr__(self):
        return f"<meld.Component {self.__class__.__name__}>"

    @classmethod
    def _listeners(cls):
        """
        Dictionary containing all listeners and the methods they call
        """
        listeners = [
            (event_name, func.__name__)
            for func in cls.__dict__.values()
            if hasattr(func, "_meld_event_names")
            for event_name in func._meld_event_names
        ]
        return {
            event_name: [t[1] for t in group]
            for event_name, group in groupby(listeners, itemgetter(0))
        }

    @property
    def _meld_attrs(self):
        """
        A list of meld variables and functions that are hidden from the view
        """
        return ["id", "render", "validate", "updated", "form"]

    def _bind_form(self, kwargs):
        """
        Create a form from the form_class, add meld:model to each field and
        bind kwargs to field data.
        """
        self._form = getattr(self, "form")
        for field in self._form:
            if not field.type == "SubmitField":
                # add render_kw defined in form field and add databinding
                render_kw = field.render_kw or dict()
                if not any(key.startswith("meld:model") for key in render_kw):
                    render_kw["meld:model"] = field.name
                setattr(self._form[field.name], "render_kw", render_kw)
                self._bind_data_to_form(field, kwargs)

    def _set_token(self, field):
        """
        Gather the CSRF token from the form and apply it to the component.
        """
        soup = BeautifulSoup(field.__call__(), features="html.parser")
        token = soup.find(attrs={"name": CSRF_TOKEN_ATTR}).get("value")
        self.csrf_token = token

    def _bind_data_to_form(self, field, kwargs):
        """
        Bind any attributes from kwargs that are form fields to the form.
        """
        if field.name in kwargs:
            self._set_field_data(field.name, kwargs[field.name])
            if field.name == CSRF_TOKEN_ATTR:
                self._set_token(field)
        else:
            setattr(self, field.name, None)

    def _set_field_data(self, field_name, value):
        """
        Set the data attribute on a form field.
        """
        setattr(self._form[field_name], "data", value)

    def validate(self, field=None):
        """
        Validate a form or a field.
        """
        if not self._form:
            return True

        if field:
            validate = field.validate(self._form)
        else:
            validate = self._form.validate()

        if not validate:
            for field in self._form:
                if field.errors:
                    self.errors[field.name] = field.errors
        return validate

    def _attributes(self):
        """
        Get attributes that can be called in the component.
        """
        attributes = {}

        attributes_names = [
            attr
            for attr in dir(self)
            if not callable(getattr(self, attr))
            and not attr.startswith("_")
            and attr not in self._meld_attrs
        ]
        for name in attributes_names:
            attributes[name] = getattr(self, name)

        return attributes

    def _functions(self):
        """
        Get methods that can be called in the component.
        """

        functions = {}

        function_list = [
            func
            for func in dir(self)
            if callable(getattr(self, func))
            and not func.startswith("_")
            and func not in self._meld_attrs
        ]

        for func in function_list:
            functions[func] = getattr(self, func)

        return functions

    def __context__(self):
        """
        Collects every thing that could be used in the template context.
        """
        return {
            "attributes": self._attributes(),
            "methods": self._functions(),
        }

    def updated(self, name):
        """
        Hook that gets called when a component's data is about to get updated.
        """
        pass

    def render(self, component_name: str):
        return self._view(component_name)

    def _render_template(self, template_name: str, context_variables: dict):
        try:
            return render_template(template_name, **context_variables)
        except TemplateNotFound:
            return render_template(f"meld/{template_name}", **context_variables)

    def _view(self, component_name: str):
        data = self._attributes()
        context = self.__context__()
        context_variables = {}
        context_variables.update(context["attributes"])
        context_variables.update(context["methods"])
        context_variables.update({"form": self._form})

        rendered_template = self._render_template(
            f"{component_name}.html", context_variables
        )

        soup = BeautifulSoup(rendered_template, features="html.parser")
        root_element = Component._get_root_element(soup)
        root_element["meld:id"] = str(self.id)
        self._set_values(root_element, context_variables)

        script = soup.new_tag("script", type="module")
        init = {"id": str(self.id), "name": component_name, "data": jsonify(data).json}
        init_json = orjson.dumps(init).decode("utf-8")

        meld_import = 'import {Meld} from "/meld_js_src/meld.js";'
        script.string = f"{meld_import} Meld.componentInit({init_json});"
        root_element.append(script)

        rendered_template = Component._desoupify(soup)

        return rendered_template

    def _set_values(self, soup, context_variables):
        """
        Set the value on model fields
        """
        for element in soup.select("input,select,textarea"):
            model_attrs = [
                attr for attr in element.attrs.keys() if attr.startswith("meld:model")
            ]
            if len(model_attrs) > 1:
                raise Exception(
                    "Multiple 'meld:model' attributes not allowed on one tag."
                )

            for model_attr in model_attrs:
                value = context_variables[element.attrs[model_attr]]
                if element.name == "select":
                    element.attrs["value"] = value
                    for e in element.find_all("option"):
                        if type(e) is Tag and e.attrs.get("value") == value:
                            e["selected"] = ""

                elif (
                    element.attrs.get("type")
                    and element.attrs.get("type") == "checkbox"
                ):
                    if value is True:
                        if not element.attrs.get("value"):
                            element["checked"] = ""
                    else:
                        if element.attrs.get("value"):
                            value = context_variables[element.attrs[model_attr]]
                            if (
                                len(value)
                                and value[0]
                                not in context_variables[element.attrs[model_attr]]
                            ):
                                context_variables[element.attrs[model_attr]].append(
                                    value[0]
                                )

    @staticmethod
    def _get_root_element(soup):
        for element in soup.contents:
            if element.name:
                return element

        raise Exception("No root element found")

    @staticmethod
    def _desoupify(soup):
        soup.smooth()
        return soup.encode(formatter=UnsortedAttributes()).decode("utf-8")


class UnsortedAttributes(HTMLFormatter):
    """
    Prevent beautifulsoup from re-ordering attributes.
    """

    def attributes(self, tag):
        for k, v in tag.attrs.items():
            yield k, v
