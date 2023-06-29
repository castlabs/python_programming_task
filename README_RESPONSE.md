# Python Programming Task

My first solution goals are robustness and development time.

Django is my web server of choice on shich proxy will be built on.\


# [Important info from](https://www.ietf.org/rfc/rfc2616.txt)

```
  server
      An application program that accepts connections in order to
      service requests by sending back responses. Any given program may
      be capable of being both a client and a server; our use of these
      terms refers only to the role being performed by the program for a
      particular connection, rather than to the program's capabilities
      in general. Likewise, any server may act as an origin server,
      proxy, gateway, or tunnel, switching behavior based on the nature
      of each request.
```

```
  proxy
      An intermediary program which acts as both a server and a client
      for the purpose of making requests on behalf of other clients.
      Requests are serviced internally or by passing them on, with
      possible translation, to other servers. A proxy MUST implement
      both the client and server requirements of this specification. A
      "transparent proxy" is a proxy that does not modify the request or
      response beyond what is required for proxy authentication and
      identification. A "non-transparent proxy" is a proxy that modifies
      the request or response in order to provide some added service to
      the user agent, such as group annotation services, media type
      transformation, protocol reduction, or anonymity filtering. Except
      where either transparent or non-transparent behavior is explicitly
      stated, the HTTP proxy requirements apply to both types of
      proxies.
```

```
8.1.3 Proxy Servers

   It is especially important that proxies correctly implement the
   properties of the Connection header field as specified in section
   14.10.

   The proxy server MUST signal persistent connections separately with
   its clients and the origin servers (or other proxy servers) that it
   connects to. Each persistent connection applies to only one transport
   link.

   A proxy server MUST NOT establish a HTTP/1.1 persistent connection
   with an HTTP/1.0 client (but see RFC 2068 [33] for information and
   discussion of the problems with the Keep-Alive header implemented by
   many HTTP/1.0 clients).
```
