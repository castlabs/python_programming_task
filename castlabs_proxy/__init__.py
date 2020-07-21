from flask import Flask, request, make_response, current_app, render_template
from datetime import datetime
from urllib.parse import urljoin
from requests import post
from castlabs_proxy.forms import ProxyForm
from babel.dates import format_datetime

import secrets
import jwt
import humanize


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['RUNNING_SINCE'] = datetime.now()

    # TODO: Review
    app.config.from_mapping(SECRET_KEY='tralara')

    if test_config is None:
        app.config.from_object('castlabs_proxy.config.base_config.BaseConfig')
    else:
        app.config.from_object(test_config)

    # As this is a very, very basic service, all routes are defined here.
    #
    # On more complex applications, an App folder exists with Blueprints.

    @app.route('/status')
    def status():
        running_since = current_app.config['RUNNING_SINCE']
        elapsed = running_since - datetime.now()
        elapsed_humanized = humanize.naturaldelta(elapsed)
        startup_date = format_datetime(running_since,
                                       format='long',
                                       locale='en_US')

        return render_template('status.html',
                               elapsed=elapsed_humanized,
                               startup_date=startup_date)

    @app.route('/', methods=('POST',), defaults={'path': ''})
    @app.route('/<path:path>')
    def proxy(path):
        jwt_token = app.config['JWT_TOKEN']
        jwt_algorithm = app.config['JWT_ALGORITHM']
        backend_url = app.config['BACKEND_URL']

        # CSRF disabled for demo purposes
        form = ProxyForm(csrf_enabled=False)

        if not form.validate_on_submit():
            errors = []
            for error in form.errors.values():
                errors.append(error[0])

            if not request.is_json:
                errors.append('Missing payload')

            data = {
                'errors': errors
            }
            return make_response(data, 400)

        user = form.user.data
        date = form.date.data

        current = datetime.now()
        nonce = secrets.token_hex()

        data = {
            'iat': int(current.timestamp()),
            'jti': nonce,
            'payload': {
                'username': user,
                'date': date.isoformat(),
            }
        }

        encoded_jwt = jwt.encode(data, jwt_token, algorithm=jwt_algorithm)
        headers = {
            'x-my-jwt': encoded_jwt,
        }

        url = urljoin(backend_url, path)
        r = post(url, headers=headers, json=data)
        response = make_response(r.json())

        return response

    return app