import ast
from werkzeug.wrappers.response import Response
import functools

from .component import get_component_class
from flask import jsonify, current_app
import orjson


def process_message(message):
    meld_id = message["id"]
    component_name = message["componentName"]
    action_queue = message["actionQueue"]

    data = message["data"]
    Component = get_component_class(component_name)
    component = Component(meld_id, **data)
    return_data = None

    for action in action_queue:
        payload = action.get("payload", None)
        if "syncInput" in action["type"]:
            if hasattr(component, payload["name"]):
                setattr(component, payload["name"], payload["value"])
                if component._form:
                    field_name = payload.get("name")
                    if field_name in component._form._fields:
                        field = getattr(component._form, field_name)
                        component._set_field_data(field_name, payload["value"])
                        component.updated(field)
                        component.errors[field_name] = field.errors or ""
                else:
                    component.updated(payload["name"])

        elif "callMethod" in action["type"]:
            call_method_name = payload.get("name", "")
            method_name, params = parse_call_method_name(call_method_name)
            message = payload.get("message")

            if method_name is not None and hasattr(component, method_name):
                func = getattr(component, method_name)
                if params:
                    return_data = func(*params)
                elif message:
                    return_data = func(**message)
                else:
                    return_data = func()
                if component._form:
                    component._bind_form(component._attributes())

    rendered_component = component.render(component_name)

    res = {
        "id": meld_id,
        "dom": rendered_component,
        "data": orjson.dumps(jsonify(component._attributes()).json).decode("utf-8"),
    }

    if type(return_data) is Response and return_data.status_code == 302:
        res["redirect"] = {"url": return_data.location}
    return res


def process_init(component_name):
    Component = get_component_class(component_name)
    return Component._listeners()


def parse_call_method_name(call_method_name: str):
    params = None
    method_name = call_method_name

    if "(" in call_method_name and call_method_name.endswith(")"):
        param_idx = call_method_name.index("(")
        params_str = call_method_name[param_idx:]

        # Remove the arguments from the method name
        method_name = call_method_name.replace(params_str, "")

        # Remove parenthesis
        params_str = params_str[1:-1]
        if params_str != "":
            try:
                params = ast.literal_eval("[" + params_str + "]")
            except (ValueError, SyntaxError):
                params = list(map(str.strip, params_str.split(",")))

    return method_name, params


def listen(*event_names: str):
    """
    Decorator to indicate that the decorated method should listen for custom events.
    It can be called using `flask_meld.emit`. Keyword arguments from `flask_meld.emit`
    will be passed as keyword arguments to the decorated method.

    Params:
        *event_names (str): One or more event names to listen for.
    """
    def dec(func):
        func._meld_event_names = event_names
        return func
    return dec


def emit(event_name: str, **kwargs):
    """
    Emit a custom event which will call any Component methods with the `@listen`
    decorator that are listening for the given event. Keyword arguments to this
    function are passed as keyword arguments to each of the decorated methods.

    Params:
        event_name (str): The name of the custom event to emit.
        **kwargs: Arguments to be passed as keyword arguments to the listening
            methods.
    """
    current_app.socketio.emit("meld-event", {"event": event_name, "message": kwargs})
