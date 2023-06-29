from aiohttp import web

from src._constants import (
    NESTED_URL_NAME,
    NESTED_URL_REGEX,
)
from src.utils.buissness_logic import create_upstream_request

_routes = web.RouteTableDef()


@_routes.post("/{" + NESTED_URL_NAME + ":" + NESTED_URL_REGEX + "}")
async def proxy(request):
    upstream_request = create_upstream_request(request)

    print(request.url.port, upstream_request.url.port)

    # for arg in dir(request):
    #     try:
    #         print(arg, getattr(request, arg))
    #     except AttributeError:
    #         continue

    return web.Response(text="Hello, world")


# create app
_app = web.Application()
# register urls
_app.add_routes(_routes)


def run_app():
    web.run_app(_app)
