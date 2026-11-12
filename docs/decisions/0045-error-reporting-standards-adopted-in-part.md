# 0045. `error-reporting`: standards adopted in part, and what was left out

- **Status:** Accepted
- **Decided:** 2026-11-11, by the owner in build-skills, on accepting the draft's choices as they
  stood · **Recorded:** 2026-11-11 · Claude Sonnet 5.5
- **Affects:** `error-reporting`

## Context

`adopting-standards` rule 6 requires a record of what was searched and what was taken. Searched:
IETF RFCs, the OWASP cheat sheet, OpenTelemetry semantic conventions, the Node.js and PostgreSQL
docs, and the Google, Microsoft, Zalando and JSON:API style guides.

## Options

- **Adopt each standard whole.** Rejected: RFC 9457 and RFC 6585 both ask for human-readable
  detail in a response, which 0042 rules out.
- **Invent a format.** Rejected: `adopting-standards` rule 1; the standards below cover every
  field but the one 0042 removes.
- **Adopt each in part and name what is left** (chosen).

## Decision

- **RFC 9457** is adopted in part:[^rfc9457] media type `application/problem+json`, `type` set to
  `about:blank`, `status`, and two extension members, `code` and `requestId`. `title`, `detail` and
  `instance` are left out (0042). This breaks a SHOULD: for `about:blank`, `title` SHOULD be the
  HTTP status phrase.[^rfc9457s421] `code`, not `type`, is the identifier.
- **RFC 6585** says a 429 response SHOULD include details;[^rfc6585] this SHOULD is deliberately
  not followed.
- **`Error-Code` header:** the IANA field registry has no such field;[^iana] the name has no `X-`
  prefix, per RFC 6648.[^rfc6648]
- **`Error.cause`** holds the native error (rule 1).[^cause] Native fields follow Node.js[^node] and
  PostgreSQL SQLSTATE.[^pg]
- **Idempotency-Key draft (rev 08):** reuse with a different payload is 422, and a key whose
  original request is in flight is 409.[^idem]
- **OpenTelemetry** exception attribute names are considered and deferred (issue #194).

## Consequences

- A client cannot rely on `title` or `detail`; RFC 9457 consumers that expect them get defaults.
- The Idempotency-Key draft may change before publication; the statuses are a line in the registry.

[^rfc9457]: IETF, *RFC 9457*, <https://www.rfc-editor.org/rfc/rfc9457.html>.
[^rfc9457s421]: RFC 9457 s4.2.1, <https://www.rfc-editor.org/rfc/rfc9457.html#section-4.2.1>:
    "When "about:blank" is used, the title SHOULD be the same as the recommended HTTP status phrase
    for that code".
[^rfc6585]: IETF, *RFC 6585*, s4, <https://www.rfc-editor.org/rfc/rfc6585.html#section-4>.
[^iana]: IANA, *Hypertext Transfer Protocol (HTTP) Field Name Registry*,
    <https://www.iana.org/assignments/http-fields/http-fields.xhtml>.
[^rfc6648]: IETF, *RFC 6648*, <https://www.rfc-editor.org/rfc/rfc6648.html>: deprecates `X-`
    prefixes.
[^cause]: MDN, *Error: cause*,
    <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause>.
[^node]: Node.js, *Errors*, <https://nodejs.org/api/errors.html>.
[^pg]: PostgreSQL, *Appendix A: Error Codes*,
    <https://www.postgresql.org/docs/current/errcodes-appendix.html>.
[^idem]: IETF, *The Idempotency-Key HTTP Header Field*,
    draft-ietf-httpapi-idempotency-key-header-08,
    <https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/>.
