from aiohttp import web as _web


async def convert_request_to_response(
    request: _web.Request, status_code: int
) -> _web.Response:
    return _web.Response(
        headers=request.headers,
        body=await request.read(),
        status=status_code,
    )
