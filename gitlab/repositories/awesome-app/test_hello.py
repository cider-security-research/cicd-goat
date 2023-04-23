import pytest
from app import app as flask_app


@pytest.fixture()
def app():
    yield flask_app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_hello(client):
    response = client.get("/hello")
    assert b"Hello, User" in response.data
