import pytest
from flask import url_for


@pytest.mark.usefixtures('live_server')
def test_input_defer(browser_client, page):
    page.goto(url_for('index', _external=True))
    # Click input
    page.click("input")
    # Fill input
    page.fill("input", "flask-defer test")
    assert page.inner_text('#bound-data-defer') == ''
    page.click("#button")
    page.wait_for_timeout(100)
    assert page.inner_text('#bound-data-defer') == 'flask-defer test'


@pytest.mark.usefixtures('live_server')
def test_checkbox_defer(browser_client, page):
    page.goto(url_for('index', _external=True))
    foo_id = "#foo-id"
    foo = page.locator("#foo-id")

    assert page.inner_text("#bound-foo") == 'True'
    assert foo.is_checked()

    page.uncheck(foo_id)
    assert page.inner_text("#bound-foo") == 'True'
    page.click("#button")
    page.wait_for_timeout(200)
    assert foo.is_checked() is False
    assert page.inner_text("#bound-foo") == 'False'
    page.click("#button")

    # test_multiple_checkboxes
    page.check("#bar-a")
    assert page.inner_text("#bound-bar") == "[]"
    page.click("#button")
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-bar") == "['q']"
    page.check("#bar-b")
    page.click("#button")
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-bar") == "['q', 'v']"

    # test checkbox with int value
    page.check("#baz-id")
    page.click("#button")
    page.wait_for_timeout(50)
    assert page.inner_text("#bound-baz") == ""
    page.wait_for_timeout(300)
    assert page.inner_text("#bound-baz") == "2"

    # test multiple checkboxes in same request
    page.check("#bar-a")
    page.check("#bar-b")
    page.check("#bar-c")
    page.click("#button")
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-bar") == "['q', 'v', 'c']"
