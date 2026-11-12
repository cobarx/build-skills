# The response, the log record and the registry entry

These are the shapes rules 2, 6, 8 and 9 refer to. `examples.md` shows them in use.

## The response

The response to the caller is the same shape for every failure.

- **Status line:** the `responseStatus` of the registry entry.
- **Headers:** `Content-Type: application/problem+json` and `Error-Code: <code>`. Add
  `Retry-After` (seconds) when the registry entry has `retryAfterSeconds`, and `WWW-Authenticate`
  on a 401, which RFC 9110 requires.
- **Body:** four members, `type` (always `about:blank`), `status`, `code` and `requestId`.

Nothing else goes in the response: no message, title, detail, reason, failure-type name, runbook
URL or native error.

## The log record

The server writes one record per failure, with these fields in this order.

| Field | What it holds |
|---|---|
| `time`, `level`, `service`, `requestId` | When, how loud, which service, and the key that joins the response to this record. |
| `code`, `type`, `reason` | The registry entry: the code, the failure type's name, and the reason. |
| `responseStatus`, `retryable` | What the caller was sent, and whether the same request may be sent again. |
| `message` | The registry's summary, written for the person reading the log. |
| `request` | The method and the route template, never the raw URL. |
| `native` | The platform's own error fields, copied unchanged; `null` when there are none. |
| `context` | What the runbook's diagnosis steps need, starting with the `operation`. |
| `cause` | The chain of errors that were caught, outermost first, each with its `name` and `message`; `null` when there is none. |
| `stack` | The runtime's stack trace of the error that was thrown. |

The `level` follows the reason: `error` for service, `warn` for abuse, `info` for client and
business rule.

## The registry entry

Each code has one entry, defined once.

| Field | What it holds |
|---|---|
| `code` | `TT-SSS-NNN`, unique and never reused. |
| `type` | The failure type's name; its number is the `TT` of the code. |
| `reason` | `service`, `client`, `business-rule` or `abuse`. |
| `responseStatus` | The HTTP status this service returns. Its class is 5xx for `service` and 4xx for the other reasons. |
| `retryable` | Whether the same request may succeed if sent again. |
| `retryAfterSeconds` | Optional; the `Retry-After` value for a 429 or 503. |
| `summary` | The log `message`. |

`SSS` in the code is not always the `responseStatus`: when a dependency's HTTP response said no, it
is the status the dependency returned (rule 3).

## Carrying context to the boundary

The context is gathered where the failure is thrown and written where it is handled.

1. At the throw site, create the error from its registry entry, with the caught error as its cause
   and the context as a field of the error.
2. At every catch in between, rethrow the error with its cause and its context, and do not log.
3. At the boundary, turn any error that is not from the registry into the registry's code for an
   unhandled error, keeping the original as its cause.
4. At the boundary, build the record from the error: the registry fields, the native fields, the
   context, the cause chain and the stack. Redact it (rule 7), log it once, and build the response
   from the registry entry.
