def clone(request, new_host, new_port, new_headers, new_scheme="http"):
    return request.clone(
        host=f"{new_host}:{new_port}", scheme=new_scheme, headers=new_headers
    )
