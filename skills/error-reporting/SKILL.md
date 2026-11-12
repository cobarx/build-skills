---
name: error-reporting
description: This skill should be used when writing code that throws, catches, wraps, logs or returns an error; when adding an error code, an error class or an error response; when an incident cannot be diagnosed from its logs; or when a runbook is written or checked. It governs how an error is identified and reported, not how a failure is retried or what is alerted on.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/error-reporting"}
---

# error-reporting

Report every error with enough to fix it without reproducing it.

An error that arrives as a message string sends the next person to the code to guess. A code, the
original failure, and the context at the moment it happened let them look the error up and act.
`references/examples.md` shows twelve failures of an API request, with what the caller receives and
what the server logs.

## Rules

1. **Keep the native error as the cause.** Pass it as `cause` when wrapping, and copy its own code
   (`ECONNRESET`, SQLSTATE `53300`, the HTTP status and body) unchanged into `native`. Done when
   the code the OS, driver or API produced appears in the record exactly as it produced it.

2. **Give every error one code `TT-SSS-NNN`, and never reuse a code.** Write the failure type's
   number (`references/categories.md`), an HTTP status, and a counter that starts at 001 within
   that pair. Define each code once, in one registry (`references/record.md`). Done when a search
   of the repository for the code finds one definition; a retired code stays marked retired.

3. **Set `SSS` to the status of the party that failed.** Use the status a dependency returned when
   its HTTP response said no, and the status this service returns for every other failure. Done
   when `SSS` equals the status in the response, or the dependency's status in `native`.

4. **Classify every code by failure type and by reason, in the registry only.** Choose the reason
   by the fix the failure calls for (`references/categories.md`): service, client, business rule
   or abuse. Return 5xx for service and 4xx for the rest. Done when every log record carries both,
   and a registry test fails on a reason whose `responseStatus` is in the other class.

5. **Write the runbook entry in the same change as the code.** The entry holds the symptom, what it
   means, the likely causes, the diagnosis steps with their commands, the fix, whether a retry is
   safe, and who to escalate to. Done when a test fails for any registry code without an entry.

6. **Capture the context a diagnosis needs where the error is thrown, and attach it to the error.**
   Record the stack trace, the operation, the identifiers of its inputs, the request ID, the
   attempt number, the upstream status, headers and body (truncated), and the settings in play (a
   pool's `max`). Done when every diagnosis step in the runbook can be carried out from the logged
   record alone.

7. **Redact before logging.** Log payload and header fields from an allowlist, and drop secrets,
   tokens and any personal data the runbook's diagnosis does not need. Done when a test logs an
   error carrying a token and the record does not contain it.

8. **Log each error once, as the record in `references/record.md`, at the boundary that handles
   it.** Rethrow with `cause` at every other catch, and set the level from the reason: `error` for
   service, `warn` for abuse, `info` for client and business rule. Done when one failure produces
   one record, and every service names its fields the same way.

9. **Describe nothing to the caller but the code and the request ID.** Send them in the body as
   problem details (`type` `about:blank`, `status`, `code`, `requestId`) and the code in the
   `Error-Code` header, and add only the headers HTTP requires or a retry needs. Leave out any
   message, title, detail, reason, failure-type name, runbook URL and native error. Done when a
   forced failure returns none of them, and its log record is found by the `requestId` alone.

## Not here

Where the records are shipped, the thresholds that page someone, and the retry policy are not
here. Programs with no HTTP response (workers, command-line tools) are not covered yet. Whether to
adopt a standard for the record or the response is `adopting-standards`. Where logs live on a host
is `platform-correctness`. Where a runbook lives so it can be found is `durable-context`.

---

Decisions affecting this skill: `docs/decisions/*-error-reporting-*.md`
