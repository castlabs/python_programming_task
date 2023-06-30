# Python Programming Task

## Intro

My solution goals are: robustness and development time.

To achive that I: want to write as little code as it is possible. All tasks besides buissness logic will be provided by external packages.

## Solution

### Glossary
  - app - proxy described in README.md
  - user - third party actor, can be human can be machine
  - upstream - location where request should be send to by the app, combination of: ip or fqd, port

To create non-transparent proxy I need a server and a client.

[aiohttp.Server](https://docs.aiohttp.org/en/stable/web.html) is my server of choice (standalone configuration).
[aiohttp.Client](https://docs.aiohttp.org/en/stable/client.html) is my client of choice.


To perform tests I need an upstream address.

Creating custom upstream is my choice mainly to make e2e tests easier and quicker, upstream logic:
   1. receive post request
   2. respond with the same payload as in post request

### Alghoritm

#### Proxy
 1. User makes http request <br>
  1.1 User makes http request to the app <br>
  1.2 App receives http request <br>
 2. App proxy http request  
  2.1 App adds data (JWT) to http request payload <br>
  2.2 App logs info about the request [Optional] <br>
  2.3 App makes http request to the upstream <br>
  2.4 Upstream receives http request <br>
  2.5 Upstream sends http response to the app <br>
  2.6 App receives http response <br>
 3. App proxy http response <br>
  3.2 App sends http response to the user <br>
  3.3 User receives http response <br>

I'll go for all bonus points ;)

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

# Important info from [RFC7519](https://www.ietf.org/rfc/rfc7519.txt)https://www.ietf.org/rfc/rfc7519.txt
```
4.1.6.  "iat" (Issued At) Claim

   The "iat" (issued at) claim identifies the time at which the JWT was
   issued.  This claim can be used to determine the age of the JWT.  Its
   value MUST be a number containing a NumericDate value.  Use of this
   claim is OPTIONAL.
```
```

4.1.7.  "jti" (JWT ID) Claim

   The "jti" (JWT ID) claim provides a unique identifier for the JWT.
   The identifier value MUST be assigned in a manner that ensures that
   there is a negligible probability that the same value will be
   accidentally assigned to a different data object; if the application
   uses multiple issuers, collisions MUST be prevented among values
   produced by different issuers as well.  The "jti" claim can be used
   to prevent the JWT from being replayed.  The "jti" value is a case-
   sensitive string.  Use of this claim is OPTIONAL.
```
```
    NumericDate
      A JSON numeric value representing the number of seconds from
      1970-01-01T00:00:00Z UTC until the specified UTC date/time,
      ignoring leap seconds.  This is equivalent to the IEEE Std 1003.1,
      2013 Edition [POSIX.1] definition "Seconds Since the Epoch", in
      which each day is accounted for by exactly 86400 seconds, other
      than that non-integer values can be represented.  See RFC 3339
      [RFC3339] for details regarding date/times in general and UTC in
      particular.A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z "```
