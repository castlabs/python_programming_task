# As this is a very, very basic service, all routes are defined here.
#
# On more complex applications, an App folder exists with Blueprints.

from flask import render_template, request, make_response
from castlabs_proxy.forms import ProxyForm
from datetime import datetime
from babel.dates import format_datetime
from requests import post
from urllib.parse import urljoin

import humanize
import secrets
import jwt


def init_routes(app):

    @app.route('/status')
    def status():
        running_since = app.config['RUNNING_SINCE']
        elapsed = running_since - datetime.now()
        elapsed_humanized = humanize.naturaldelta(elapsed)
        startup_date = format_datetime(running_since,
                                       format='long',
                                       locale='en_US')
        times = 0

        return render_template('status.html',
                               elapsed=elapsed_humanized,
                               startup_date=startup_date,
                               times=times)


    @app.route('/', methods=('POST',), defaults={'path': ''})
    @app.route('/<path:path>')
    def proxy(path):
        jwt_token = app.config['JWT_TOKEN']
        jwt_algorithm = app.config['JWT_ALGORITHM']
        backend_url = app.config['BACKEND_URL']

        # CSRF disabled for demo purposes
        form = ProxyForm(meta={'csrf': False})

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