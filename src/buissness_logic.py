from aiohttp import web as _web
from multidict import CIMultiDict

from src._constants import HEX_STRING_SECRET
from src._constants import JWT_HEADER_NAME
from src._constants import SIGNATURE_ALGHORITM
from src._constants import UPSTREAM_IP
from src._constants import UPSTREAM_PORT
from src._constants import UPSTREAM_SCHEME
from src.utils.datetime import format_datetime_date
from src.utils.datetime import generate_now
from src.utils.datetime import generate_seconds_since_epoch
from src.utils.jwt import generate_jwt
from src.utils.request import clone as clone_request
from src.utils.uuid import generate_uuid


def create_upstream_request(request: _web.Request) -> _web.Request:
    return clone_request(
        request,
        new_host=UPSTREAM_IP,
        new_port=UPSTREAM_PORT,
        new_scheme=UPSTREAM_SCHEME,
        new_headers=generate_upstream_headers(request),
    )


def generate_upstream_headers(request: _web.Request) -> CIMultiDict:
    # If new headers are required, just expand the map
    NEW_HEADERS_VALUES_MAP = {JWT_HEADER_NAME: generate_upstream_jwt()}

    mutable_headers = CIMultiDict(
        request.headers
    )  # i don't see a point of creating interface to basically a dict
    # that's why CIMultiDict is used directly

    for header, value in NEW_HEADERS_VALUES_MAP.items():
        mutable_headers[header] = value

    return mutable_headers


def generate_upstream_jwt():
    jwt_claims = {
        # satisfies task requirement for `jti`
        "jti": generate_unique_value(),
        # satisfies task requirement for `ati`
        "iat": generate_seconds_since_epoch(),
        "payload": {
            # satisfies task requirement for `payload`.
            #  Propably `user` should be logged in username
            #  but that would require sharing db with upstream.
            #  I want to keep things simple for POC.
            #  TO-DO
            #  - get logged in `user` from request
            "user": "username",
            "date": generate_today_date(),
        },
    }

    return generate_jwt(
        claims=jwt_claims,
        # satisfies task requirement for `hex as a secret`
        secret=HEX_STRING_SECRET,
        # satisfies task requirement for `HS512`
        algorithm=SIGNATURE_ALGHORITM,
    )


def generate_unique_value() -> str:
    # I want to keep things simple, that's why uuid.
    return generate_uuid()


def generate_today_date() -> str:
    return format_datetime_date(generate_now())


# def make_upstream_request
