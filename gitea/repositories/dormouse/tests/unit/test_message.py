import pytest

from flask_meld.message import parse_call_method_name, listen


@pytest.mark.parametrize(
    ["message_name", "expected_params"],
    [
        ("call(hello)", ["hello"]),
        ("call(!)", ["!"]),
        ("call('hello')", ["hello"]),
        ("call('hello, world')", ["hello, world"]),
        ("call(hello, world)", ["hello", "world"]),
        ("call(1)", [1]),
        ("call(1, 2)", [1, 2]),
        ("call(1, 2, 'hello')", [1, 2, "hello"]),
        # ("call(1, 2, hello)", [1, 2, "hello"]), # should this be supported?
    ],
)
def test_parse(message_name, expected_params):
    method_name, params = parse_call_method_name(message_name)
    assert method_name == "call"
    assert params == expected_params

@pytest.mark.parametrize(
    ["event_names"], [([],), (["foo"],), (["foo", "bar"],)],
)
def test_listen(event_names):
    listen(*event_names)(lambda: None)._meld_event_names == event_names
