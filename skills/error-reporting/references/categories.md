# Failure types and reasons

Every code is classified twice, in the registry. The reason appears only in the log record. The
failure type appears in the log record by name, and in a response only as the opaque number in the
code (rule 9).

## Failure type: the first segment of a code

The type says where the failure arose. Its number is the `TT` in `TT-SSS-NNN`. Choose the type by
the origin of the native error, not by who is at fault. When one situation can be detected in two
places (a constraint in the database, a check in the service), register one code and give it the
type of the check the service relies on, so that refactoring the check does not change the code.

| `TT` | Type | Use it when | Native fields to capture |
|---|---|---|---|
| `01` | `request` | This service rejects the request itself: its shape, credentials, permissions, rate or rules. | None, or the parser's position. |
| `02` | `api` | A dependency's HTTP response said no. | The dependency's status, error type and error code. |
| `03` | `net` | No response arrived: a reset, a timeout, a DNS failure. | `code`, `errno`, `syscall`, `address`, `port`. |
| `04` | `db` | The database refused or failed. | SQLSTATE, condition, severity, table, constraint. |
| `05` | `sys` | The operating system or a resource limit refused. | `code`, `errno`, `syscall`, `path`. |
| `06` | `int` | This service's own code failed. | None; the cause chain and stack carry it. |

Add a type by taking the next number. Never reuse or renumber one.

## Reason: why the request failed

The reason names the fix. To classify a code, ask what has to change for the request to succeed,
and who changes it. A code has exactly one reason, and each reason has its own dashboard, so a
change in one means one thing.

| Reason | Meaning | The fix | Status class | Log level |
|---|---|---|---|---|
| `service` | This service, or a dependency it relies on, failed. | Repair the service or the dependency. | 5xx | `error` |
| `client` | The client should not have made this request: a missing parameter, an expired token, a resource it may not read, too many requests. | The client changes its request. | 4xx | `info` |
| `business-rule` | The request is valid, and a rule of the business refuses it: a stock limit, a plan limit, a one-per-customer limit. | The customer's situation or the rule changes. | 4xx | `info` |
| `abuse` | Traffic that should be blocked: a known bad address, a scanner's user agent. | The operator blocks the traffic. | 4xx | `warn` |

Judge the reason by the fix the rejection calls for, not by suspected intent. Where two reasons
seem to fit, decide with these tests:

- **Client or business rule.** Ask whether the client could have known the request would fail
  from the API contract and its own data, without server state that can change. If it could, the
  code is `client`: a missing parameter, an expired token, a resource it does not own, a rate
  limit, a reused idempotency key. If the answer depends on state that changes between the
  client's last read and its request, the code is `business-rule`: stock, or an order that has
  shipped. When one request cannot tell the two apart, register one code and classify it by the fix.
- **Client or abuse.** A client over its rate limit is `client`. Traffic is `abuse` only when it
  should be blocked outright.
- **Service or client.** If the same request would succeed once the service or its dependency
  recovers, it is `service`.

Two codes that share a status but differ in reason get two codes. Examples 3 and 7 both return 403,
and the codes of examples 4 and 11 both end in 429.

## Dashboards

Build one dashboard per reason, graph each by `code`, and watch each against its own baseline. A
rise means something different in each, and the usual response differs.

| Reason | A rise usually means | Who responds |
|---|---|---|
| `service` | This service or a dependency is failing. Split by `type` to find which. | The service owner. |
| `client` | A client release or integration changed, or a change here broke clients. | Check this service's last deploy, then contact the client owner. |
| `business-rule` | A limit or rule is being hit more often. | The product owner. |
| `abuse` | Hostile traffic is arriving. | The security owner extends the blocking. |
