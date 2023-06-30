from aiohttp import web as _web

from src._constants import ENDPOINT_STATUS_CODE
from src._constants import NESTED_URL_NAME
from src._constants import NESTED_URL_REGEX
from src.buissness_logic import convert_request_to_response

_routes = _web.RouteTableDef()


@_routes.post("/{" + NESTED_URL_NAME + ":" + NESTED_URL_REGEX + "}")
async def proxy(request: _web.Request) -> _web.Response:
    return await convert_request_to_response(request, ENDPOINT_STATUS_CODE)


# create app
_app = _web.Application()
# register urls
_app.add_routes(_routes)


def run_app() -> None:
    _web.run_app(_app)
