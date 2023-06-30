import uuid
from datetime import datetime

import jwt as _jwt
from aiohttp import web as _web

from src._constants import HEX_STRING_SECRET
from src._constants import SIGNATURE_ALGHORITM
from src._constants import UPSTREAM_IP
from src._constants import UPSTREAM_PORT
from src._constants import UPSTREAM_SCHEME
from src.utils.request import clone as clone_request


def create_upstream_request(request: _web.Request) -> _web.Request:
    return clone_request(
        request,
        new_host=UPSTREAM_IP,
        new_port=UPSTREAM_PORT,
        new_scheme=UPSTREAM_SCHEME,
    )


def handle_upstream_request(request: _web.Request) -> _web.Request:
    jwt_claims, _ = {
        # satisfies task requirement for `jti`
        "jti": generate_unique_value(),
        # satisfies task requirement for `ati`
        "iat": generate_datetime_value(),
    }, {
        # satisfies task requirement for `payload`.
        #  Propably `user` should be generated but
        #  that would require sharing db with upstream.
        #  I want to keep things simple for POC.
        #  TO-DO
        #  - get logged in `user` from request
        "user": "username",
        "date": "todays date",
    }

    jwt_value = generate_jwt(jwt_claims)

    return request


def generate_unique_value() -> str:
    return str(uuid.uuid4())


def generate_datetime_value() -> datetime:
    return datetime.now()


def generate_jwt(claims: dict) -> str:
    return _jwt.encode(
        payload=claims,
        # satisfies task requirement for `hex as a secret`
        key=HEX_STRING_SECRET,
        # satisfies task requirement for `HS512`
        algorithm=SIGNATURE_ALGHORITM,
    )
