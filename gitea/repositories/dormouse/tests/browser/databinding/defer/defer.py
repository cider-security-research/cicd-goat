from flask_meld.component import Component
from flask import redirect, url_for


class Defer(Component):
    first_name = ""

    foo = True
    bar = []
    baz = ""
