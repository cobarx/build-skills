# 0043. `error-reporting`: the code form is `TT-SSS-NNN`

- **Status:** Accepted
- **Decided:** 2026-11-10, by the owner in build-skills ("tightly aligned with the http status
  codes"; "one option would be to have the category be a number. 02-429-02 for example") ·
  **Recorded:** 2026-11-11 · Claude Sonnet 5.5
- **Affects:** `error-reporting`

## Context

Codes must be unique, tied to HTTP status, and say nothing about the failure to the caller.

## Options

- **`SSS-NNN` (status and counter).** Rejected: the owner's example includes a category.
- **Letter prefixes such as `DB-001`.** Rejected: they name the failing part to the caller (0042).
- **`TT-SSS-NNN`** (chosen): `TT` is a two-digit failure-type number (01 request, 02 api, 03 net,
  04 db, 05 sys, 06 int), `SSS` the status of the party that failed, `NNN` a counter within
  `TT-SSS`.

## Decision

Rule 2 of `error-reporting` uses `TT-SSS-NNN`. The failure-type name appears only in the log.

## Consequences

- Two choices are the draft's, not the owner's, and are unconfirmed: the counter has three digits
  (the owner's example had two), and the type numbering is the draft's own.
- Programs with no HTTP response have no `SSS` (issue #196).
