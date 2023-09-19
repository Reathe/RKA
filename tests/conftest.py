import pytest

from replit_keep_alive.keep_alive import app


@pytest.fixture
def client():
    return app.test_client()
