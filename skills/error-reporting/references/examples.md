# Examples: twelve failures of an API request

Each example shows one failure of a request to `orders-api`, a hypothetical service that takes
checkout orders. It gives what the caller receives and what the server logs. The payloads are plain
HTTP and JSON; any language can produce them, and `typescript.md` shows one implementation.

The payloads are constructed. The native fields are real platform values in examples 5, 9, 10, 11
and 12 (SQLSTATE `23505` and `53300`, `ECONNRESET`, Stripe's `lock_timeout`, `EMFILE`); the rest
are labeled synthetic where they appear.

## The two shapes

**What the caller receives** is the same shape for every failure. It has the status line, an
`Error-Code` header, and a problem-details body (RFC 9457) with four members. It carries no
message, no title, no detail, no reason and no failure type. `Retry-After` is added where the
registry sets it, and a 401 carries `WWW-Authenticate` because RFC 9110 requires it.

**What the server logs** is one record per failure, with these fields:

| Field | What it holds |
|---|---|
| `time`, `level`, `service`, `requestId` | When, how loud, which service, and the key that joins the response to this record. |
| `code`, `type`, `reason` | The registry entry: the code, the failure type's name, and the reason class. |
| `responseStatus`, `retryable` | What the caller was sent, and whether the same request may be sent again. |
| `message` | The registry's summary, written for the person reading the log. |
| `request` | The method and the route template (never the raw URL). |
| `native` | The platform's own error fields, copied unchanged; `null` when there are none. |
| `context` | What the runbook's diagnosis steps need. |
| `cause` | The chain of errors that were caught, outermost first; `null` when there is none. |
| `stack` | The runtime's stack trace, shortened here. |

The level follows the reason: `error` for service and integration, `warn` for abuse, `info` for a
business rule. A page on `error` then never fires for a caller's mistake.

Every code has a runbook entry in `docs/runbook/<code>.md`.

| # | Code | Failure | Type | Reason | Returned |
|---|---|---|---|---|---|
| 1 | `01-400-001` | A required parameter is missing | request | business rule | 400 |
| 2 | `01-401-001` | The credentials are expired | request | business rule | 401 |
| 3 | `01-403-001` | The caller asks for a resource that is not theirs | request | business rule | 403 |
| 4 | `01-404-001` | The resource does not exist | request | business rule | 404 |
| 5 | `04-409-001` | The idempotency key was already used | db | business rule | 409 |
| 6 | `01-422-001` | The order asks for more stock than exists | request | business rule | 422 |
| 7 | `01-429-001` | The caller exceeded its rate limit | request | abuse | 429 |
| 8 | `06-500-001` | An unhandled error in this service's code | int | service | 500 |
| 9 | `03-502-001` | The inventory service reset the connection | net | integration | 502 |
| 10 | `04-503-001` | No database connection is free | db | service | 503 |
| 11 | `02-429-001` | The payment provider timed out on an object lock | api | integration | 503 |
| 12 | `05-503-001` | The process ran out of file descriptors | sys | service | 503 |

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
  "time": "2026-11-11T09:02:14.331Z", "level": "info", "service": "orders-api",
  "requestId": "req_7b2e41",
  "code": "01-400-001", "type": "request", "reason": "business-rule",
  "responseStatus": 400, "retryable": false,
  "message": "A required parameter is missing",
  "request": { "method": "POST", "route": "/orders" },
  "native": null,
  "context": { "parameter": "customerId", "location": "body", "received": ["items", "currency"] },
  "cause": null,
  "stack": ["validateOrder (orders/validate:31)", "createOrder (orders/create:12)"]
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
  "time": "2026-11-11T09:14:40.007Z", "level": "info", "service": "orders-api",
  "requestId": "req_0c9d52",
  "code": "01-401-001", "type": "request", "reason": "business-rule",
  "responseStatus": 401, "retryable": false,
  "message": "The credentials are missing, expired or invalid",
  "request": { "method": "GET", "route": "/orders/{id}" },
  "native": null,
  "context": { "scheme": "Bearer", "failure": "expired", "expiredAt": "2026-11-11T08:30:00Z", "tokenId": "tok_91c2" },
  "cause": null,
  "stack": ["verifyToken (auth/verify:58)", "authenticate (auth/middleware:20)"]
}
```

The log holds the token's ID and never the token. One 401 is a policy outcome; a run of them from
one source is what the abuse graphs look for, by counting this code.

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
  "time": "2026-11-11T09:21:03.882Z", "level": "info", "service": "orders-api",
  "requestId": "req_5a18f3",
  "code": "01-403-001", "type": "request", "reason": "business-rule",
  "responseStatus": 403, "retryable": false,
  "message": "The caller may not access this resource",
  "request": { "method": "GET", "route": "/orders/{id}" },
  "native": null,
  "context": {
    "resource": "order", "resourceId": "9001", "principal": "cust_204",
    "ownerId": "cust_377", "requiredScope": "orders:read:any", "grantedScopes": ["orders:read:own"]
  },
  "cause": null,
  "stack": ["authorizeRead (orders/policy:44)", "getOrder (orders/get:19)"]
}
```

RFC 9110 lets a service answer 404 instead, to hide that the resource exists. A service that does
so registers the 404 code for this case and logs the same context.

## 4. The resource does not exist: `01-404-001`

The request is `GET /orders/777777`.

**The caller receives**

```http
HTTP/1.1 404 Not Found
Content-Type: application/problem+json
Error-Code: 01-404-001

{"type":"about:blank","status":404,"code":"01-404-001","requestId":"req_e4410b"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:25:51.120Z", "level": "info", "service": "orders-api",
  "requestId": "req_e4410b",
  "code": "01-404-001", "type": "request", "reason": "business-rule",
  "responseStatus": 404, "retryable": false,
  "message": "The resource does not exist",
  "request": { "method": "GET", "route": "/orders/{id}" },
  "native": null,
  "context": { "resource": "order", "resourceId": "777777", "principal": "cust_204" },
  "cause": null,
  "stack": ["getOrder (orders/get:27)"]
}
```

## 5. The idempotency key was already used: `04-409-001`

The request is `POST /orders` with `Idempotency-Key: order_4412_checkout`, sent a second time. The
database refuses the insert. The failure is a business rule, and its type is `db` because the
platform's own code comes from the database.

**The caller receives**

```http
HTTP/1.1 409 Conflict
Content-Type: application/problem+json
Error-Code: 04-409-001

{"type":"about:blank","status":409,"code":"04-409-001","requestId":"req_b7730a"}
```

**The server logs**

```json
{
  "time": "2026-11-11T09:31:12.664Z", "level": "info", "service": "orders-api",
  "requestId": "req_b7730a",
  "code": "04-409-001", "type": "db", "reason": "business-rule",
  "responseStatus": 409, "retryable": false,
  "message": "An order with this idempotency key already exists",
  "request": { "method": "POST", "route": "/orders" },
  "native": {
    "sqlstate": "23505", "condition": "unique_violation", "severity": "ERROR",
    "table": "orders", "constraint": "orders_idempotency_key_key"
  },
  "context": { "idempotencyKey": "order_4412_checkout", "existingOrderId": "4412" },
  "cause": [{ "name": "DatabaseError", "message": "duplicate key value violates unique constraint \"orders_idempotency_key_key\"" }],
  "stack": ["insertOrder (orders/repo:73)", "createOrder (orders/create:40)"]
}
```

`native.sqlstate` is `23505`, `unique_violation` in PostgreSQL's table of error codes, kept as the
database sent it.

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
  "time": "2026-11-11T09:36:29.015Z", "level": "info", "service": "orders-api",
  "requestId": "req_91ac07",
  "code": "01-422-001", "type": "request", "reason": "business-rule",
  "responseStatus": 422, "retryable": false,
  "message": "The order asks for more stock than is available",
  "request": { "method": "POST", "route": "/orders" },
  "native": null,
  "context": { "sku": "SKU-88121", "requested": 5, "available": 2, "warehouse": "ams-1" },
  "cause": null,
  "stack": ["reserveStock (orders/stock:61)", "createOrder (orders/create:33)"]
}
```

## 7. The caller exceeded its rate limit: `01-429-001`

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
  "time": "2026-11-11T09:41:55.402Z", "level": "warn", "service": "orders-api",
  "requestId": "req_3f6e9d",
  "code": "01-429-001", "type": "request", "reason": "abuse",
  "responseStatus": 429, "retryable": true,
  "message": "The caller exceeded its request rate",
  "request": { "method": "GET", "route": "/orders" },
  "native": null,
  "context": { "principal": "key_ab12", "limit": 100, "windowSeconds": 60, "observed": 101, "clientAddress": "203.0.113.9" },
  "cause": null,
  "stack": ["consume (ratelimit/bucket:29)", "limitRate (ratelimit/middleware:15)"]
}
```

This is the same HTTP status as example 11, with the opposite fault: here the caller is at fault,
there a dependency is. The reason separates them, and only the log shows it.

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
  "time": "2026-11-11T09:47:08.771Z", "level": "error", "service": "orders-api",
  "requestId": "req_c28a54",
  "code": "06-500-001", "type": "int", "reason": "service",
  "responseStatus": 500, "retryable": false,
  "message": "An unhandled error reached the boundary",
  "request": { "method": "POST", "route": "/orders" },
  "native": null,
  "context": { "operation": "orders.create", "orderDraftId": "draft_5521" },
  "cause": [{ "name": "NullReferenceError", "message": "order.pricing is null" }],
  "stack": ["totalPrice (orders/pricing:88)", "priceOrder (orders/pricing:41)", "createOrder (orders/create:36)", "route (http/router:102)"]
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
  "time": "2026-11-11T09:52:30.209Z", "level": "error", "service": "orders-api",
  "requestId": "req_6d03b8",
  "code": "03-502-001", "type": "net", "reason": "integration",
  "responseStatus": 502, "retryable": true,
  "message": "The inventory service reset the connection",
  "request": { "method": "POST", "route": "/orders" },
  "native": { "code": "ECONNRESET", "errno": -104, "syscall": "read" },
  "context": {
    "dependency": "inventory", "method": "POST", "url": "http://inventory.internal/reserve",
    "reusedSocket": true, "attempt": 1, "idleSocketTimeoutMs": 15000, "idempotencyKey": "order_4412_reserve"
  },
  "cause": [
    { "name": "FetchError", "message": "request to http://inventory.internal/reserve failed, reason: read ECONNRESET" },
    { "name": "SystemError", "message": "read ECONNRESET" }
  ],
  "stack": ["reserve (inventory/client:57)", "createOrder (orders/create:38)"]
}
```

`native.errno` is `-104` on Linux, where `ECONNRESET` is 104. The shape follows
npm/make-fetch-happen issue 199, where an idle connection outlived the server's keep-alive timeout.

## 10. No database connection is free: `04-503-001`

The request is `POST /orders`; all twenty pooled connections are in use and thirty-seven requests
are waiting.

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
  "time": "2026-11-11T09:58:14.540Z", "level": "error", "service": "orders-api",
  "requestId": "req_a19e60",
  "code": "04-503-001", "type": "db", "reason": "service",
  "responseStatus": 503, "retryable": true,
  "message": "No database connection is available",
  "request": { "method": "POST", "route": "/orders" },
  "native": {
    "sqlstate": "53300", "condition": "too_many_connections", "severity": "FATAL",
    "message": "remaining connection slots are reserved for non-replication superuser connections"
  },
  "context": { "operation": "orders.insert", "pool": { "max": 20, "total": 20, "idle": 0, "waiting": 37 }, "instance": "orders-api-7d9f" },
  "cause": [{ "name": "DatabaseError", "message": "remaining connection slots are reserved for non-replication superuser connections" }],
  "stack": ["acquire (db/pool:112)", "insertOrder (orders/repo:70)", "createOrder (orders/create:40)"]
}
```

The error text is the one GitLab's production issue 122 recorded. `context.pool` is what the runbook
reads first: `idle: 0` with many waiting means the pool is held, not too small.

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
  "time": "2026-11-11T10:03:41.918Z", "level": "error", "service": "orders-api",
  "requestId": "req_47fd12",
  "code": "02-429-001", "type": "api", "reason": "integration",
  "responseStatus": 503, "retryable": true,
  "message": "The payment provider timed out on an object lock",
  "request": { "method": "POST", "route": "/orders/{id}/capture" },
  "native": {
    "httpStatus": 429, "provider": { "type": "invalid_request_error", "code": "lock_timeout" },
    "rateLimitedReasonHeader": null
  },
  "context": {
    "dependency": "stripe", "operation": "payment_intents.update", "providerObjectId": "pi_3Q1x",
    "attempt": 1, "maxRetries": 0, "idempotencyKey": "order_4412_capture"
  },
  "cause": [{ "name": "ProviderApiError", "message": "This object cannot be accessed right now because another API request or Stripe process is currently accessing it." }],
  "stack": ["updatePaymentIntent (payments/client:90)", "capture (orders/capture:25)"]
}
```

The code ends in 429 because that is the status the provider returned; the response is 503
because the fault is not the caller's. Stripe's documentation says a 429 without a
`Stripe-Rate-Limited-Reason` header is not a rate limit, which is why `native` records its absence.
Stripe assigns no request ID to a lock timeout, so none is logged.

## 12. The process ran out of file descriptors: `05-503-001`

The request is `POST /orders`; writing the receipt fails because the process holds 1,021 of its
1,024 descriptors.

**The caller receives**

```http
HTTP/1.1 503 Service Unavailable
Content-Type: application/problem+json
Error-Code: 05-503-001
Retry-After: 5

{"type":"about:blank","status":503,"code":"05-503-001","requestId":"req_d80b36"}
```

**The server logs**

```json
{
  "time": "2026-11-11T10:09:27.356Z", "level": "error", "service": "orders-api",
  "requestId": "req_d80b36",
  "code": "05-503-001", "type": "sys", "reason": "service",
  "responseStatus": 503, "retryable": true,
  "message": "The process has no free file descriptors",
  "request": { "method": "POST", "route": "/orders" },
  "native": { "code": "EMFILE", "errno": -24, "syscall": "open", "path": "/var/data/receipts/4412.pdf" },
  "context": { "operation": "receipts.write", "fdSoftLimit": 1024, "fdOpen": 1021, "writesInFlight": 380 },
  "cause": [{ "name": "SystemError", "message": "EMFILE: too many open files, open '/var/data/receipts/4412.pdf'" }],
  "stack": ["writeReceipt (receipts/store:34)", "createOrder (orders/create:44)"]
}
```

`native.errno` is `-24` on Linux, where `EMFILE` is 24. The context separates a leak from a low
limit: `fdOpen` near `fdSoftLimit` with hundreds of writes in flight points to unbounded concurrency.
