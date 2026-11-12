# Examples: twelve failures of an API request

Each example shows one failure of a request to `orders-api`, a hypothetical service that takes
checkout orders. It gives what the caller receives and what the server logs. The payloads are plain
HTTP and JSON; any language can produce them. `record.md` defines the response and the log record.

The payloads are constructed. The native fields in examples 5, 9, 10 and 11 follow real platform
values (SQLSTATE `23505` and `53300`, `ECONNRESET`, Stripe's `lock_timeout`). The database field
names (`code`, `severity`) follow node-postgres's documented error shape and were not captured
here. The other values are made up.

Rule 5 gives every code a runbook entry, `runbook/<code>.md` in the service's repository. The
entries are not written yet (#193).

| # | Code | Failure | Type | Reason | Returned |
|---|---|---|---|---|---|
| 1 | `01-400-001` | A required parameter is missing | request | client | 400 |
| 2 | `01-401-001` | The credentials are expired | request | client | 401 |
| 3 | `01-403-001` | The client asks for a resource that is not theirs | request | client | 403 |
| 4 | `01-429-001` | The client exceeded its rate limit | request | client | 429 |
| 5 | `04-422-001` | The idempotency key was reused for a different request | db | client | 422 |
| 6 | `01-422-001` | The order asks for more stock than exists | request | business-rule | 422 |
| 7 | `01-403-002` | The request comes from a blocked address | request | abuse | 403 |
| 8 | `06-500-001` | An unhandled error in this service's code | int | service | 500 |
| 9 | `03-502-001` | The inventory service reset the connection | net | service | 502 |
| 10 | `04-503-001` | No database connection is free | db | service | 503 |
| 11 | `02-429-001` | The payment provider timed out on an object lock | api | service | 503 |
| 12 | `01-409-001` | A shipped order cannot be cancelled | request | business-rule | 409 |

---

## 1. A required parameter is missing: `01-400-001`

The request is `POST /orders` with a body that has no `customerId`.

**The caller receives**

```http
HTTP/1.1 400 Bad Request
Content-Type: application/problem+json
Error-Code: 01-400-001

{"type":"about:blank","status":400,"code":"01-400-001","requestId":"req_7b2e41"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:02:14.331Z",
  "level": "info",
  "service": "orders-api",
  "requestId": "req_7b2e41",
  "code": "01-400-001",
  "type": "request",
  "reason": "client",
  "responseStatus": 400,
  "retryable": false,
  "message": "A required parameter is missing",
  "request": {
    "method": "POST",
    "route": "/orders"
  },
  "native": null,
  "context": {
    "operation": "orders.create",
    "parameter": "customerId",
    "location": "body",
    "received": ["items", "currency"]
  },
  "cause": null,
  "stack": [
    "validateOrder (orders/validate:31)",
    "createOrder (orders/create:12)"
  ]
}
```

The caller is told only that the request was bad. The log names the missing parameter, which the
caller finds in the API documentation.

## 2. The credentials are expired: `01-401-001`

The request is `GET /orders/4412` with a bearer token that expired at 08:30.

**The caller receives**

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/problem+json
Error-Code: 01-401-001
WWW-Authenticate: Bearer

{"type":"about:blank","status":401,"code":"01-401-001","requestId":"req_0c9d52"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:14:40.007Z",
  "level": "info",
  "service": "orders-api",
  "requestId": "req_0c9d52",
  "code": "01-401-001",
  "type": "request",
  "reason": "client",
  "responseStatus": 401,
  "retryable": false,
  "message": "The credentials are missing, expired or invalid",
  "request": {
    "method": "GET",
    "route": "/orders/{id}"
  },
  "native": null,
  "context": {
    "operation": "orders.get",
    "scheme": "Bearer",
    "failure": "expired",
    "expiredAt": "2026-11-11T08:30:00Z",
    "tokenId": "tok_91c2"
  },
  "cause": null,
  "stack": ["verifyToken (auth/verify:58)", "authenticate (auth/middleware:20)"]
}
```

The log holds the token's ID and never the token. One 401 is a client to fix; a run of them from
one source is a lead for whoever owns the blocklist, found by counting this code per source.

## 3. The caller asks for a resource that is not theirs: `01-403-001`

The request is `GET /orders/9001` from customer `cust_204`; the order belongs to `cust_377`.

**The caller receives**

```http
HTTP/1.1 403 Forbidden
Content-Type: application/problem+json
Error-Code: 01-403-001

{"type":"about:blank","status":403,"code":"01-403-001","requestId":"req_5a18f3"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:21:03.882Z",
  "level": "info",
  "service": "orders-api",
  "requestId": "req_5a18f3",
  "code": "01-403-001",
  "type": "request",
  "reason": "client",
  "responseStatus": 403,
  "retryable": false,
  "message": "The caller may not access this resource",
  "request": {
    "method": "GET",
    "route": "/orders/{id}"
  },
  "native": null,
  "context": {
    "operation": "orders.get",
    "resource": "order",
    "resourceId": "9001",
    "principal": "cust_204",
    "ownerId": "cust_377",
    "requiredScope": "orders:read:any",
    "grantedScopes": ["orders:read:own"]
  },
  "cause": null,
  "stack": ["authorizeRead (orders/policy:44)", "getOrder (orders/get:19)"]
}
```

RFC 9110 lets a service answer 404 instead, to hide that the resource exists. A service that does
so registers the 404 code for this case and logs the same context.

## 4. The caller exceeded its rate limit: `01-429-001`

The request is the 101st `GET /orders` in a minute from API key `key_ab12`, whose limit is 100.

**The caller receives**

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/problem+json
Error-Code: 01-429-001
Retry-After: 30

{"type":"about:blank","status":429,"code":"01-429-001","requestId":"req_3f6e9d"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:41:55.402Z",
  "level": "info",
  "service": "orders-api",
  "requestId": "req_3f6e9d",
  "code": "01-429-001",
  "type": "request",
  "reason": "client",
  "responseStatus": 429,
  "retryable": true,
  "message": "The caller exceeded its request rate",
  "request": {
    "method": "GET",
    "route": "/orders"
  },
  "native": null,
  "context": {
    "operation": "orders.list",
    "principal": "key_ab12",
    "limit": 100,
    "windowSeconds": 60,
    "observed": 101
  },
  "cause": null,
  "stack": [
    "consume (ratelimit/bucket:29)",
    "limitRate (ratelimit/middleware:15)"
  ]
}
```

The code of example 11 also ends in 429, because the payment provider returned that status, but
its response is 503 and its reason is `service`. The reason separates them, and only the log shows
it.

## 5. The idempotency key was reused for a different request: `04-422-001`

The request is `POST /orders` with `Idempotency-Key: order_4412_checkout`, the key of an earlier
order, but with different items. A request that repeats the first one exactly is a retry, not a
failure: the service returns the saved order and logs no error. Here the database refuses the
insert, and the service finds that the stored request differs from this one. The IETF draft for the
`Idempotency-Key` header asks for a 422 in this case, and for a 409 while the first request is
still being processed. The reason is `client`, because the fix is a new key. The type is `db`
because the native code comes from the database.

**The caller receives**

```http
HTTP/1.1 422 Unprocessable Content
Content-Type: application/problem+json
Error-Code: 04-422-001

{"type":"about:blank","status":422,"code":"04-422-001","requestId":"req_b7730a"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:31:12.664Z",
  "level": "info",
  "service": "orders-api",
  "requestId": "req_b7730a",
  "code": "04-422-001",
  "type": "db",
  "reason": "client",
  "responseStatus": 422,
  "retryable": false,
  "message": "An idempotency key was reused for a different request",
  "request": {
    "method": "POST",
    "route": "/orders"
  },
  "native": {
    "code": "23505",
    "severity": "ERROR",
    "table": "orders",
    "constraint": "orders_idempotency_key_key"
  },
  "context": {
    "operation": "orders.create",
    "idempotencyKey": "order_4412_checkout",
    "existingOrderId": "4412",
    "storedRequestHash": "sha256:9f2c61",
    "receivedRequestHash": "sha256:41ab07"
  },
  "cause": [
    {
      "name": "DatabaseError",
      "message": "duplicate key value violates unique constraint \"orders_idempotency_key_key\""
    }
  ],
  "stack": ["insertOrder (orders/repo:73)", "createOrder (orders/create:40)"]
}
```

`native.code` is `23505`, `unique_violation` in PostgreSQL's table of error codes, kept as the
driver reports it. The two hashes show that the requests differ without logging either payload.

## 6. The order asks for more stock than exists: `01-422-001`

The request is `POST /orders` for five units of `SKU-88121`; two are in stock.

**The caller receives**

```http
HTTP/1.1 422 Unprocessable Content
Content-Type: application/problem+json
Error-Code: 01-422-001

{"type":"about:blank","status":422,"code":"01-422-001","requestId":"req_91ac07"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:36:29.015Z",
  "level": "info",
  "service": "orders-api",
  "requestId": "req_91ac07",
  "code": "01-422-001",
  "type": "request",
  "reason": "business-rule",
  "responseStatus": 422,
  "retryable": false,
  "message": "The order asks for more stock than is available",
  "request": {
    "method": "POST",
    "route": "/orders"
  },
  "native": null,
  "context": {
    "operation": "orders.create",
    "sku": "SKU-88121",
    "requested": 5,
    "available": 2,
    "warehouse": "ams-1"
  },
  "cause": null,
  "stack": ["reserveStock (orders/stock:61)", "createOrder (orders/create:33)"]
}
```

## 7. The request comes from a blocked address: `01-403-002`

The request is `GET /orders` from an address on the blocklist, with a scanner's user agent.

**The caller receives**

```http
HTTP/1.1 403 Forbidden
Content-Type: application/problem+json
Error-Code: 01-403-002

{"type":"about:blank","status":403,"code":"01-403-002","requestId":"req_2e95c0"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:44:19.640Z",
  "level": "warn",
  "service": "orders-api",
  "requestId": "req_2e95c0",
  "code": "01-403-002",
  "type": "request",
  "reason": "abuse",
  "responseStatus": 403,
  "retryable": false,
  "message": "The request comes from a blocked source",
  "request": {
    "method": "GET",
    "route": "/orders"
  },
  "native": null,
  "context": {
    "operation": "orders.list",
    "clientAddress": "203.0.113.77",
    "userAgent": "masscan/1.3",
    "matchedRule": "blocklist:address",
    "listEntry": "203.0.113.64/26",
    "listUpdatedAt": "2026-11-10T00:00:00Z"
  },
  "cause": null,
  "stack": [
    "checkBlocklist (security/blocklist:37)",
    "guard (security/middleware:12)"
  ]
}
```

This is the same status as example 3 with a different reason: example 3 is a client asking for
something that is not theirs, and this is traffic that should be blocked. The code differs, so a
blocked caller can tell the two apart. A service that wants to hide that returns one code for both
and gives up the separate graph.

## 8. An unhandled error in this service's code: `06-500-001`

The request is `POST /orders`; a pricing step reads a field that is null.

**The caller receives**

```http
HTTP/1.1 500 Internal Server Error
Content-Type: application/problem+json
Error-Code: 06-500-001

{"type":"about:blank","status":500,"code":"06-500-001","requestId":"req_c28a54"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:47:08.771Z",
  "level": "error",
  "service": "orders-api",
  "requestId": "req_c28a54",
  "code": "06-500-001",
  "type": "int",
  "reason": "service",
  "responseStatus": 500,
  "retryable": false,
  "message": "An unhandled error reached the boundary",
  "request": {
    "method": "POST",
    "route": "/orders"
  },
  "native": null,
  "context": {
    "operation": "orders.create",
    "orderDraftId": "draft_5521"
  },
  "cause": [
    {
      "name": "Error",
      "message": "order.pricing is null"
    }
  ],
  "stack": [
    "totalPrice (orders/pricing:88)",
    "priceOrder (orders/pricing:41)",
    "createOrder (orders/create:36)",
    "route (http/router:102)"
  ]
}
```

The boundary wraps anything it did not expect in this code and keeps the original as the cause,
so the stack still points at `orders/pricing:88`. A rise in this code means a bug to find.

## 9. The inventory service reset the connection: `03-502-001`

The request is `POST /orders`; the call to the inventory service reuses a keep-alive connection
that the inventory service has already closed.

**The caller receives**

```http
HTTP/1.1 502 Bad Gateway
Content-Type: application/problem+json
Error-Code: 03-502-001

{"type":"about:blank","status":502,"code":"03-502-001","requestId":"req_6d03b8"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:52:30.209Z",
  "level": "error",
  "service": "orders-api",
  "requestId": "req_6d03b8",
  "code": "03-502-001",
  "type": "net",
  "reason": "service",
  "responseStatus": 502,
  "retryable": true,
  "message": "The inventory service reset the connection",
  "request": {
    "method": "POST",
    "route": "/orders"
  },
  "native": {
    "code": "ECONNRESET",
    "errno": -104,
    "syscall": "read"
  },
  "context": {
    "operation": "inventory.reserve",
    "dependency": "inventory",
    "method": "POST",
    "url": "http://inventory.internal/reserve",
    "reusedSocket": true,
    "attempt": 1,
    "idleSocketTimeoutMs": 15000,
    "idempotencyKey": "order_4412_reserve"
  },
  "cause": [
    {
      "name": "FetchError",
      "message": "request to http://inventory.internal/reserve failed, reason: read ECONNRESET"
    },
    {
      "name": "Error",
      "message": "read ECONNRESET"
    }
  ],
  "stack": ["reserve (inventory/client:57)", "createOrder (orders/create:38)"]
}
```

`native.errno` is `-104` on Linux, where `ECONNRESET` is 104. The shape follows
npm/make-fetch-happen issue 199, where an idle connection outlived the server's keep-alive timeout.

## 10. No database connection is free: `04-503-001`

The request is `POST /orders`. The pool holds 12 of its 20 connections, all busy, and the database
refuses a thirteenth because it has reached its connection limit across every instance.

**The caller receives**

```http
HTTP/1.1 503 Service Unavailable
Content-Type: application/problem+json
Error-Code: 04-503-001
Retry-After: 2

{"type":"about:blank","status":503,"code":"04-503-001","requestId":"req_a19e60"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:58:14.540Z",
  "level": "error",
  "service": "orders-api",
  "requestId": "req_a19e60",
  "code": "04-503-001",
  "type": "db",
  "reason": "service",
  "responseStatus": 503,
  "retryable": true,
  "message": "No database connection is available",
  "request": {
    "method": "POST",
    "route": "/orders"
  },
  "native": {
    "code": "53300",
    "severity": "FATAL",
    "message": "remaining connection slots are reserved for non-replication superuser connections"
  },
  "context": {
    "operation": "orders.insert",
    "pool": {
      "max": 20,
      "total": 12,
      "idle": 0,
      "waiting": 37
    },
    "instance": "orders-api-7d9f"
  },
  "cause": [
    {
      "name": "DatabaseError",
      "message": "remaining connection slots are reserved for non-replication superuser connections"
    }
  ],
  "stack": [
    "acquire (db/pool:112)",
    "insertOrder (orders/repo:70)",
    "createOrder (orders/create:40)"
  ]
}
```

The error text is the one GitLab's production issue 122 recorded. `53300` is the database's limit
across every client, not this pool's `max`, so the runbook's first step compares the server's
`max_connections` with the sum of every instance's pool `max`. `idle: 0` with requests waiting shows
that the pool cannot grow.

## 11. The payment provider timed out on an object lock: `02-429-001`

The request is `POST /orders/4412/capture`; Stripe answers 429 with `lock_timeout` because another
request holds the same payment object. This service answers 503.

**The caller receives**

```http
HTTP/1.1 503 Service Unavailable
Content-Type: application/problem+json
Error-Code: 02-429-001
Retry-After: 2

{"type":"about:blank","status":503,"code":"02-429-001","requestId":"req_47fd12"}
```

**The server logs**

```json
{
  "time": "2026-11-11T10:03:41.918Z",
  "level": "error",
  "service": "orders-api",
  "requestId": "req_47fd12",
  "code": "02-429-001",
  "type": "api",
  "reason": "service",
  "responseStatus": 503,
  "retryable": true,
  "message": "The payment provider timed out on an object lock",
  "request": {
    "method": "POST",
    "route": "/orders/{id}/capture"
  },
  "native": {
    "httpStatus": 429,
    "body": {
      "error": {
        "type": "invalid_request_error",
        "code": "lock_timeout",
        "message": "This object cannot be accessed right now because another API request or Stripe process is currently accessing it."
      }
    }
  },
  "context": {
    "operation": "orders.capture",
    "dependency": "stripe",
    "providerOperation": "payment_intents.update",
    "providerObjectId": "pi_3Q1x",
    "attempt": 1,
    "maxRetries": 0,
    "idempotencyKey": "order_4412_capture",
    "rateLimitedReasonHeader": null
  },
  "cause": [
    {
      "name": "ProviderApiError",
      "message": "This object cannot be accessed right now because another API request or Stripe process is currently accessing it."
    }
  ],
  "stack": [
    "updatePaymentIntent (payments/client:90)",
    "capture (orders/capture:25)"
  ]
}
```

The code ends in 429 because that is the status the provider returned; the response is 503 because
the fault is not the caller's. Stripe's documentation says a 429 without a
`Stripe-Rate-Limited-Reason` header is not a rate limit, which is why `context` records its
absence. Stripe assigns no request ID to a lock timeout, so none is logged. The error type and
code come from the report in stripe-node issue 2056.

## 12. A shipped order cannot be cancelled: `01-409-001`

The request is `POST /orders/4412/cancel`; the order shipped yesterday.

**The caller receives**

```http
HTTP/1.1 409 Conflict
Content-Type: application/problem+json
Error-Code: 01-409-001

{"type":"about:blank","status":409,"code":"01-409-001","requestId":"req_d80b36"}
```

**The server logs**

```json
{
  "time": "2026-11-11T10:09:27.356Z",
  "level": "info",
  "service": "orders-api",
  "requestId": "req_d80b36",
  "code": "01-409-001",
  "type": "request",
  "reason": "business-rule",
  "responseStatus": 409,
  "retryable": false,
  "message": "The order is in a state that does not allow this action",
  "request": {
    "method": "POST",
    "route": "/orders/{id}/cancel"
  },
  "native": null,
  "context": {
    "operation": "orders.cancel",
    "orderId": "4412",
    "action": "cancel",
    "orderState": "shipped",
    "allowedStates": ["pending", "paid"],
    "shippedAt": "2026-11-10T14:12:00Z"
  },
  "cause": null,
  "stack": [
    "assertCancellable (orders/cancel:22)",
    "cancelOrder (orders/cancel:9)"
  ]
}
```

The request is valid and the order exists; a rule of the business refuses it. Retrying does not
help, and the customer's route is a return, which is a different request.
