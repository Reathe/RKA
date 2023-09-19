from threading import Thread

import pytest

from replit_keep_alive import keep_alive


@pytest.fixture
def flask_app_thread() -> Thread:
    return keep_alive.run()


def test_run(flask_app_thread):
    pass
