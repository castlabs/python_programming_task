from src._constants import (
    UPSTREAM_IP,
    UPSTREAM_PORT,
    UPSTREAM_SCHEME,
)
from src.utils.request import clone as clone_request


def create_upstream_request(request):
    return clone_request(
        request,
        new_host=UPSTREAM_IP,
        new_port=UPSTREAM_PORT,
        new_scheme=UPSTREAM_SCHEME,
    )
