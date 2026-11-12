# 0044. `error-reporting`: classify every error by the fix

- **Status:** Accepted
- **Decided:** 2026-11-11, by the owner in build-skills ("the reason reflects what
  should be done to fix the issue"; "if it's in a situation where the client is unaware, then
  business rule would make sense") · **Recorded:** 2026-11-11 · Claude Sonnet 5.5
- **Affects:** `error-reporting`

## Context

The owner graphs errors to separate what the service fails to handle from what a client must fix.
Grouping by HTTP status cannot do that: a 429 can come from a client calling too often or from a
dependency that is overloaded.

## Options

- **Group by status class.** Rejected: see above.
- **Group by who is at fault.** Rejected: it does not say who acts.
- **Group by the fix** (chosen): `service` (the service or a dependency failed; 5xx), `client` (the
  client should not have made the request), `business-rule` (a valid request the business
  refuses), `abuse` (traffic to block).

## Decision

Every code has one reason, held in the registry and logged, never sent to the caller. Log level
follows the reason: `error` for service, `warn` for abuse, `info` for the others. A borderline
case between client and business rule is decided by whether the client could have known from the
API contract and its own data, without server state that can change.

## Consequences

- "Integration" in the owner's scheme means the client's own integration; the skill calls it
  `client`.
- A reused idempotency key with a different request is `client`.
