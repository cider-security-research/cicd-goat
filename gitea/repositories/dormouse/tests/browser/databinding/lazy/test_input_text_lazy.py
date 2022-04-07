import pytest
from flask import url_for


@pytest.mark.usefixtures('live_server')
def test_input_text(browser_client, page):
    page.goto(url_for('index', _external=True))
    # wait for component.loaded
    # Click input
    page.click("input")
    # Fill input
    fill_text = "flask-meld input_text_lazy"
    page.fill("input", fill_text)
    page.wait_for_timeout(50)
    assert page.inner_text("#bound-data") == ""
    page.click("#input-last")
    page.wait_for_timeout(200)
    assert page.inner_text("#bound-data") == fill_text
