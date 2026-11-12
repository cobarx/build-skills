# 0042. `error-reporting`: a response carries only the code and the request ID

- **Status:** Accepted
- **Decided:** 2026-11-11, by the owner in build-skills ("i don't think we should include any
  details about what failed in an api response. so error messages should be stripped out") ·
  **Recorded:** 2026-11-11 · Claude Sonnet 5.5
- **Affects:** `error-reporting`

## Context

The style guides read for this skill all put a human-readable message in the error response:
RFC 9457's `title` and `detail`,[^rfc9457] Google's `message` and `ErrorInfo.reason`,[^aip193]
the Azure guidelines' required `message`,[^azure] Stripe's `message`,[^stripe] and JSON:API's
`title` and `detail`.[^jsonapi] Security guidance
says a response should not reveal how the service failed.[^owasp][^rfc9457s5]

## Options

- **Follow the guides:** a generic message plus a code. Rejected by the owner: any text invites
  detail to creep in later, and the code already names the failure for anyone with the registry.
- **A code and nothing else** (chosen), with the request ID so support can find the log record.

## Decision

The response carries the code (in the body and in an `Error-Code` header) and the request ID.
Message, title, detail, reason, failure-type name, runbook URL and native error stay in the log.

## Consequences

- This departs from every style guide read, and a client developer gets less from a response. The
  code is the lookup key into documentation the service publishes.
- The code still reveals a number: the status and a counter. That is accepted.

[^rfc9457]: IETF, *RFC 9457: Problem Details for HTTP APIs* (2023), s3.1,
    <https://www.rfc-editor.org/rfc/rfc9457.html>.
[^aip193]: Google, *AIP-193: Errors*, <https://google.aip.dev/193>.
[^azure]: Microsoft, *Azure REST API Guidelines*, "Handling Errors", ErrorDetail table,
    <https://github.com/microsoft/api-guidelines/blob/vNext/azure/Guidelines.md>: `message` is
    required, "A human-readable representation of the error."
[^stripe]: Stripe, *API Reference: Errors*, <https://docs.stripe.com/api/errors>: `message` is "A
    human-readable message providing more details about the error."
[^jsonapi]: JSON:API, *Format*, "Error Objects", <https://jsonapi.org/format/#error-objects>:
    `title` is "a short, human-readable summary of the problem"; `detail` is "a human-readable
    explanation specific to this occurrence of the problem."
[^owasp]: OWASP, *Error Handling Cheat Sheet*,
    <https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html>: return a
    generic message to the user and keep the detail in the log.
[^rfc9457s5]: RFC 9457 s5, <https://www.rfc-editor.org/rfc/rfc9457.html#section-5>: problem
    details can reveal implementation detail that helps an attacker.
