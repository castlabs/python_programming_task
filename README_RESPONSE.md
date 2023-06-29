# Python Programming Task

## Intro

My first solution goals are: robustness and development time.

To achive that I: want to write as little code as it is possible. All tasks besides buissness logic will be provided by external packages.

## Solution

To create non-transparent proxy I need a server and a client.

[Django](https://www.djangoproject.com/)+[Gunicorn](https://gunicorn.org) is my server of choice.
[Requests](https://pypi.org/project/requests/) is my client of choice.

Custom upstream is my choice mainly to make e2e tests easier and quicker, upstream app logic:
   1. receive post request
   2. respond with the same payload as in post request

### Alghoritm
Glossary: <br>
  - app - proxy about which talk is about in task description
  - user - third party actor, can be human can be machine
  - upstream - location where request should be send to by the app, combination of: ip or fqd, port
  
Algoritm: <br>
 1. User makes http request <br>
  1.1 User makes http request to the app <br>
  1.2 App receives http request <br>
 2. App proxy http request  
  2.1 App adds data to http request payload <br>
  2.2 App logs info about the request [Optional] <br>
  2.3 App makes http request to the upstream <br>
  2.4 Upstream receives http request <br>
  2.5 Upstream sends http response to the app <br>
  2.6 App receives http response <br>
 3. App proxy http response <br>
  3.2 App sends http response to the user <br>
  3.3 User receives http response <br>

I'll go for all bonus points except `Use asyncronous programming` cause I would like to propose a second solution especially for it ;)

###TO-DO
1. write 2.1 in details
2. write 2.2 in details

# Important info from [RFC2616](https://www.ietf.org/rfc/rfc2616.txt)

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
```
14.10 Connection

   The Connection general-header field allows the sender to specify
   options that are desired for that particular connection and MUST NOT
   be communicated by proxies over further connections.

   The Connection header has the following grammar:

       Connection = "Connection" ":" 1#(connection-token)
       connection-token  = token

   HTTP/1.1 proxies MUST parse the Connection header field before a
   message is forwarded and, for each connection-token in this field,
   remove any header field(s) from the message with the same name as the
   connection-token. Connection options are signaled by the presence of
   a connection-token in the Connection header field, not by any
   corresponding additional header field(s), since the additional header
   field may not be sent if there are no parameters associated with that
   connection option.

   Message headers listed in the Connection header MUST NOT include
   end-to-end headers, such as Cache-Control.

   HTTP/1.1 defines the "close" connection option for the sender to
   signal that the connection will be closed after completion of the
   response. For example,

       Connection: close

   in either the request or the response header fields indicates that
   the connection SHOULD NOT be considered `persistent' (section 8.1)
   after the current request/response is complete.

   HTTP/1.1 applications that do not support persistent connections MUST
   include the "close" connection option in every message.

   A system receiving an HTTP/1.0 (or lower-version) message that
   includes a Connection header MUST, for each connection-token in this
   field, remove and ignore any header field(s) from the message with
   the same name as the connection-token. This protects against mistaken
   forwarding of such header fields by pre-HTTP/1.1 proxies. See section
   19.6.2.
```
```
19.6.2 Compatibility with HTTP/1.0 Persistent Connections

   Some clients and servers might wish to be compatible with some
   previous implementations of persistent connections in HTTP/1.0
   clients and servers. Persistent connections in HTTP/1.0 are
   explicitly negotiated as they are not the default behavior. HTTP/1.0
   experimental implementations of persistent connections are faulty,
   and the new facilities in HTTP/1.1 are designed to rectify these
   problems. The problem was that some existing 1.0 clients may be
   sending Keep-Alive to a proxy server that doesn't understand
   Connection, which would then erroneously forward it to the next
   inbound server, which would establish the Keep-Alive connection and
   result in a hung HTTP/1.0 proxy waiting for the close on the
   response. The result is that HTTP/1.0 clients must be prevented from
   using Keep-Alive when talking to proxies.

   However, talking to proxies is the most important use of persistent
   connections, so that prohibition is clearly unacceptable. Therefore,
   we need some other mechanism for indicating a persistent connection
   is desired, which is safe to use even when talking to an old proxy
   that ignores Connection. Persistent connections are the default for
   HTTP/1.1 messages; we introduce a new keyword (Connection: close) for
   declaring non-persistence. See section 14.10.

   The original HTTP/1.0 form of persistent connections (the Connection:
   Keep-Alive and Keep-Alive header) is documented in RFC 2068. [33]
```
