# Retiring `organize`

**Proposal, 2026-10-06. Not settled.** Remove `organize` from ai-skills-cobarx, and move each of
its responsibilities to a skill that already owns it or to one new skill, `readme`.

`organize` does six jobs under one name. Four of them already have an owner in this library, and
in two places the owner here disagrees with `organize` (#118). Two jobs are left without an owner:
what an entry point says, and how original files are kept. This proposal gives the first to a new
skill and the second to `durable-context`. Removal waits for an eval showing no loss of quality
(below).

## Where each part of `organize` goes

| `organize` section | Goes to | Change needed |
|---|---|---|
| README.md: four questions | `readme` (new) | New skill |
| CLAUDE.md: briefing, index, purpose notes | `readme` (what it says), `durable-context` rule 3 (that it indexes everything) | New skill |
| Write as you go, then tighten | `durable-context` rules 1 and 6 already | None |
| `docs/` layout: decisions, context, runbooks | `durable-context` rule 5 | None |
| Decision template | `decision-log` | None |
| `artifacts/<subject>/` and its README | `durable-context` (where), `readme` (the folder README) | New rule in `durable-context` |
| Directory layouts | `project-setup` (planned) | Carried into its draft |
| Code-level docs | `contracts` rule 5 | None |

## Responsibilities

### `readme` (new): an entry point answers the questions its reader arrives with

Owns what an entry point *says*. There are three kinds, and each has its own reader: the project
`README.md` (someone who will use the project), `AGENTS.md` or `CLAUDE.md` (whoever works on it),
and a folder's `README.md` (someone who has landed in that folder).

Kicks in when an entry point is written or edited; when a change alters status, setup or layout
that an entry point describes; when a file is added to a folder that has an index; and when work
starts in a project whose entry point is missing or out of date.

Does not own whether a file can be reached from an entry point, or where files live.

Examples:
- **Stale status.** playhead's `README.md` says "Pre-implementation… No code yet." The stats
  overlay shipped in #7. Rule: the entry point changes in the same PR as the thing it describes.
- **An index that says when.** `Cars/Datsun240Z/stewardship/datsun-240z/README.md` links
  `photos/from-trong-texts/` as "83 photos (Aug 2023–May 2026) recovered from the SMS/MMS backup
  after the original iCloud album link went dead". The reader learns when to open it, not just
  what is inside.
- **A folder README for its reader.** `Antiques/Sony-STR-7065/photos/README.md` has a row for each
  file, with columns *File | Contents | When to use*. Someone who lands in that folder can find
  the nameplate photo without opening each image.
- **A placement guide, not an index.** `Antiques/1946-GE-Refrigerator/images/README.md` describes
  what goes in each subfolder but lists no files. It helps someone filing a photo, and not someone
  looking for one. Whether a folder README must serve both is open (question 2).

Draft: [skills/readme/SKILL.md](../../skills/readme/SKILL.md) on branch `readme-skill`.

### `durable-context` (updated): context lives in the project, where the next reader will find it

Keeps everything it owns now: where each kind of document lives, and that each one can be reached
from an entry point. Gains one kind of document: **originals**, meaning files from outside the
project such as manuals, receipts, invoices, photos and screenshots.

Proposed rule: keep the file itself, not a link to it. File originals by subject, not by file
type, and record where each one came from and when it was retrieved. That is rule 1 applied to
files. A receipt in Gmail, or an album behind an iCloud link, is context that isn't in the
project. Its "Not here" stops pointing at `organize` and points at `readme` and `project-setup`.

Examples:
- **Why the file, not the link.** The 240Z's body-shop photos lived in an iCloud album until the
  link went dead. They were recovered from an SMS backup into
  `photos/from-trong-texts/`.
- **Provenance in the index.** `Computers/Julian/artifacts/manuals/README.md` records *Source* and
  *Retrieved* for each PDF, and says why they are local: "needed exactly when the machine is down".
- **Unfiled originals.** `Antiques/1946-GE-Refrigerator/20260906_171702.jpg` and
  `Computers/Julian/s-l1600.webp` sit at their project roots, and no document links them.
  Nothing can find them.
- **By subject, not type.** `Antiques/SF2Cabinet/artifacts/manuals/` and `artifacts/cps-3/` are
  filed by subject. The fridge's `images/` and `manuals/` are filed by file type.

### `fixtures` (unchanged): test data comes from the real world, or says that it does not

Owns captured data that a test reads. The line between it and `durable-context`: **a file a test
reads is a fixture; any other file from outside the project is an original.**

Examples:
- `CampaignStop/fixtures/google-messages-inbox-2026-10-03.json`, captured by
  `tools/capture-conversation-list.js` and written by `tools/save-capture.py`.
- `pubnet-tools/crates/pubnetchk/tests/fixtures/home-wifi-macos/`, captured by `capture.sh` and
  recaptured at each new network.

### `steward` (ai-skills-cobarx, unchanged): what to record about a thing you own

Keeps the per-asset layout (`README.md`, `specs.md`, `history.md`, `costs.md`, `docs/`,
`photos/`, `bids/`) and its rule to save the original, not a summary. After the removal, a
stewardship project gets its entry points and originals rules from this library.

Examples: `Cars/Datsun240Z/stewardship/datsun-240z/`, `Cars/Datsun510/stewardship/datsun-510/`,
`Antiques/RandomAntiques/stewardship/busy-b-fan/`, `Computers/Julian/stewardship/`.

A later peer skill could publish stewardship records as a website or wiki. That would be the case
for bringing stewardship into a library of its own; it is out of scope here.

### Unchanged owners

- `decision-log`: what a decision record says. playhead's and Julian's dated decision files stay
  as they are.
- `contracts`: doc comments on the exported surface.
- `project-setup` (planned): directory layout of a new project.

## Eval before removal

Same prompt, same model, two clean copies of each project. Copy A has `organize`; copy B has
`durable-context` and `readme` without `organize`. Graded blind by a separate agent, then read by
the owner. The criteria are what `organize` gets right today, and must not regress:

- every document and original can be reached from an entry point;
- index entries say when to open each file;
- the README answers the four questions, and matches the project's current state;
- originals are kept as files, filed by subject, and indexed with their source;
- the agent file stays short enough to read before starting work.

| Project | Prompt | What it tests |
|---|---|---|
| playhead | The stats overlay landed; bring the docs up to date | Stale README, agent file, `artifacts/` index |
| Computers/Julian | File the two new manuals and the stray image | Originals beside `steward` folders |
| Antiques/1946-GE-Refrigerator | Add these photos and the warranty card | Folder README, filing by subject |
| Cars/Datsun240Z | Record the body-shop update, with photos from texts | Originals from texts, `steward` README |
| CampaignStop, pubnet-tools | Add a new capture | Captures stay under `fixtures`, and stay indexed |

The result goes in `docs/context/`, and the removal decision cites it.

## Order

1. `readme` skill (PR here).
2. The eval.
3. Decision record, and the `durable-context` update (closes #118).
4. Remove `organize` from ai-skills-cobarx: the skill and two README lines.

## Open questions

1. **Do originals go in `durable-context`, or in a peer skill?** The rule touches
   `durable-context`, `fixtures` and `steward`. Three is the line where `simplicity` rule 2 makes
   a concern a peer. Recommendation: `durable-context`, because keeping the file rather than a
   link is its rule 1, and `fixtures` and `steward` add only their own specifics.
2. **Must a folder README list every file, or can it be a placement guide?** The fridge's
   `images/README.md` is a placement guide; Sony's `photos/README.md` lists every file.
3. **Do this library's skills fit a project with no code?** `~/Projects/Cars` and
   `~/Projects/Antiques` are not git repositories. They have no PRs for `readme` rule 6, and no
   tracker for `durable-context` rule 2's follow-ups. If a
   stewardship project needs different rules, that argues for keeping a cut-down `organize`
   rather than removing it.
4. **Standard Readme.** The draft adopts its section names and order. That means this repo's
   README renames "Installation" to "Install", and stewardship READMEs don't fit it at all. Adopt
   it for software projects only, or drop it?
