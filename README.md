# AsyncProxy - Python Programming Task

Your task is to build an asynchronous HTTP proxy (see definition in
[RFC2616](https://www.ietf.org/rfc/rfc2616.txt)) complying to the requirements
specified below.

## Requirements

1. Range requests must be supported as defined in
[RFC2616](https://www.ietf.org/rfc/rfc2616.txt), but also via `range` query
parameter.

2. HTTP 416 error must be returned in case where both header and query parameter are
specified, but with a different value.

3. Program must start with a single command `docker-compose up`.

4. Proxy must be reachable at `http://<docker-host>:8080` .

5. Usage statistics must be available at `http://<docker-host>:8080/stats`

  * total bytes transferred
  * uptime

6. Code must run with Python 3.5+.

7. Code must be delivered as a link to public GitHub repository.
