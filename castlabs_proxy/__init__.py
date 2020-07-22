from flask import Flask
from datetime import datetime


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['RUNNING_SINCE'] = datetime.now()

    # TODO: Review
    app.config.from_mapping(SECRET_KEY='tralara')

    if test_config is None:
        app.config.from_object('castlabs_proxy.config.base_config.BaseConfig')
    else:
        app.config.from_object(test_config)

    from castlabs_proxy.routes import init_routes
    init_routes(app)

    return app