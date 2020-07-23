from flask import Flask
from datetime import datetime

import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['RUNNING_SINCE'] = datetime.now()

    SECRET_TOKEN = os.environ['SECRET_TOKEN']

    app.config.from_mapping(SECRET_KEY=SECRET_TOKEN)

    if test_config is None:
        app.config.from_object('castlabs_proxy.config.base_config.BaseConfig')
    else:
        app.config.from_object(test_config)

    from castlabs_proxy.routes import init_routes
    init_routes(app)

    return app