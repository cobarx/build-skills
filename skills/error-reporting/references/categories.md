# Failure types and reasons

Every code is classified twice, in the registry. The classification appears in the log record and
never in a response (rule 4).

## Failure type: the first segment of a code

The type says where the failure arose. Its number is the `TT` in `TT-SSS-NNN`. Choose the type by
the origin of the native error, not by who is at fault.

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

The reason says who must act. A code has exactly one.

| Reason | Meaning | Who acts | Status class | Log level |
|---|---|---|---|---|
| `integration` | A dependency failed or refused this service. | The service owner, with the dependency's owner. | 5xx | `error` |
| `service` | This service or its infrastructure failed. | The service owner. | 5xx | `error` |
| `business-rule` | A request the domain refuses, or that breaks the request's contract. | The caller. | 4xx | `info` |
| `abuse` | A rejection that exists to protect the service. | The caller, or the security owner. | 4xx | `warn` |

Judge the reason by the policy that rejected the request, not by suspected intent. A single 401 is
a policy outcome, and a run of them is found by counting its code.

Two codes that share a status but differ in reason get two codes. Example 7 and example 11 are both
429: the first is `abuse`, the second `integration`.

## Graphing

Graph by `reason`, then by `code`. The roll-up "the service is failing" is `service` plus
`integration`; the roll-up "the caller must change something" is `business-rule` plus `abuse`.
A rise in a `business-rule` code right after a deploy can still be this service's bug, so watch the
rate of each such code against its own baseline.
