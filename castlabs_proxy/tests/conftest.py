from castlabs_proxy import create_app

import pytest


@pytest.fixture()
def client():
    flask_app = create_app('castlabs_proxy.config.testing.TestingConfig')
    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()