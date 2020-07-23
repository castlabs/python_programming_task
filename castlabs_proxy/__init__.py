from flask import Flask
from datetime import datetime
from castlabs_proxy.utils import get_secret

import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['RUNNING_SINCE'] = datetime.now()


    if test_config is None:
        app.config.from_object('castlabs_proxy.config.base_config.BaseConfig')
    else:
        app.config.from_object(test_config)

    app.config.from_mapping(SECRET_KEY=get_secret('flask_secret', app.testing))
    app.config['JWT_TOKEN'] = get_secret('jwt_token', app.testing)

    from castlabs_proxy.routes import init_routes
    init_routes(app)

    return app