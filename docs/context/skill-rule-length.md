# Why are recent skills' rules longer, and should `skill-review` address it?

Working analysis, written 2026-11-02. Not a decision yet.

## Summary

**Recommendation:** don't add a length rule to `skill-review`, and don't set a word limit. The measure
is the effort a person needs to understand a rule fully, which a word count can't show. Test each
sentence instead, as `skill-review` rule 10 now does. In one pass that test shortened rules, where a
rule against needless words made them longer ([the trial](needless-words-trial.md)).

- **Recent skills are longer, but the library hasn't drifted.** The median across merged build-skills
  rules has stayed near 34 words since 2026-09-21. The rise is in new skills: `operate` averages 60
  words a rule, `organize-project` 53, `procedures` 52 and `skill-review` 64.
- **Nothing limits length except a line cap.** The fifty-line cap allows about 600 words, and the
  longest merged build-skills skill uses 437.
- **Writing guidance only pushes one way.** `writing-style` says to keep the small words, and its
  rule against needless words was left out. Rewording `skill-review` for a general reader added 27%.
- **Causes are partly measured.** Only that 27% is a direct measurement. The rest are explanations
  that fit the numbers.

**The owner's concern (2026-11-02):** "the amount of effort required by a human to fully understand
the rule. clear, concise language helps here. leaving out critical info hurts". So a word count can
only prompt a look. The test is whether a person understands the rule fully with little effort.

## The goal

A person should be able to understand a rule fully with little effort, which takes clear and concise
language with nothing critical left out (the owner, 2026-11-02). Length is only a proxy for that
effort. A long rule can be easy to understand, and a short one can leave out what the reader needs.

## What was measured

Counted 2026-11-02 at `origin/main` and at each open PR's branch: words in each numbered rule under
`## Rules`, including its bold title and number. Title length is the words in the bold text. Skills
with few samples or very different subjects make this suggestive, not conclusive.

| Group | Words per rule | Words in all rules | Title words |
|---|---|---|---|
| Library at 2026-09-20, first 4 skills (median) | 30 | | |
| Library now, 18 merged skills (median of all rules) | 35 | | 6.5 (mean of skills) |
| Longest merged skill by total, `spec` | 44 | 437 | 8.2 |
| Longest merged skill per rule, `adopting-standards` | 57 | 340 | 7 |
| `steward` (stewardship-skills, merged) | 38 | about 420 | 5.9 |
| `procedures` (stewardship-skills, PR 13) | 52 | about 520 | 6.5 |
| `organize-project` (sysadmin-skills, merged) | 53 | about 530 | 8.4 |
| `operate` (sysadmin-skills, PR 5) | 60 | about 600 | 9.6 |
| `skill-review` before rewording (`3fddae6`) | 50 | 454 | 10.1 |
| `skill-review` after rewording (`817df7f`) | 64 | 578 | 12.6 |

Most merged skills barely changed since their first version. The exceptions are `simplicity` (24 to
36 words a rule) and `durable-context` (39 to 51), where most of the increase came from rules added
later. `spec` doubled its rules while its words per rule stayed about the same.

So "our skills are more verbose" holds for `operate`, `organize-project`, `procedures` and
`skill-review`, and not for the merged build-skills library. `steward` (38) and the two writing skills
(40 and 41) are also recent and are not long.

## What may be causing it

These are ordered by how strong the evidence is.

1. **Rewriting for clarity adds words, and nothing pushes back (measured for one skill).**
   Rewording `skill-review` took it from 454 to 578 words, and the review that drove it suggested
   almost no cuts, though its brief asked about clarity and not length. `writing-style` rule 3 says to keep the articles and verbs. Decision 0029 left "omitting
   needless words" out while it is tested, although the
   [writing research](writing-research.md) found it in three or more sources. This doesn't explain
   `operate`, which was opened before the writing skills merged, though it could have been revised
   after.
2. **Long titles repeat the body (measured).** Titles in `skill-review` average 12.6 words against
   about 6.5 across the library, and `operate` averages 9.6. Rule 2's title is itself the rule's
   content.
3. **The only limit is on lines (measured as a gap).** Decisions 0009 and 0031 cap lines, and 0031
   gave most skills more room. At about twelve words a line, fifty lines allow about 600 words, which
   `operate` reaches. Nothing limits a single rule. Whether the cap caused any growth is not shown.
4. **Each review's lesson gets added to a rule (seen in one skill, argued beyond it).** The
   `skill-review` lessons doc shows rules 3, 6, 8 and 9 each growing a clause after one comparison. A
   rule that remembers every failure gets longer each time.
5. **Trimming is discouraged without a counterweight (argued).** Decision 0009 undid cuts that lost
   reasoning, and "move or keep reasoning" is a standing instruction. That protects reasoning, but
   nothing says when text in a rule should move out.
6. **Subject matter (argued).** Skills about operating machines may need more conditions and examples
   than skills about principles. `steward` doesn't fit that neatly, so this is at most part of it.
7. **The drafting agent or model (not tested).** The first skills were also drafted by agents, and I
   have no measure of how the model or its effort affected length.

## Should `skill-review` get a rule?

**The case for it:** reviewers test what a skill tells them to test. The review of `skill-review`
read every sentence closely and suggested almost no cuts, and the owner was the one who questioned
"This check is quick...". A rule would make someone look.

That argument applies now: reviewers aren't looking for excess. But a rule here isn't the only way to
make them, and it has three costs:

- **It would be policy in the wrong skill.** AGENTS.md says not to give a skill policy that belongs to
  another, and `skill-review` says it doesn't govern how a skill is written. How long a rule may be is
  a writing standard.
- **A reviewer has no standard to check.** `review` rule 2 says to check the declared standard rather
  than invent one. No length standard exists beyond the line cap. The test in AGENTS.md, "does this
  change what anyone does?", exists, and rule 1 already covers it through "the skill's own project".
- **It would add length to the skill with the longest rules.** That cost is small, but it points the
  wrong way.

Rule 2 of `skill-review` already has a behavioural version: report a rule that makes no difference
as unproven. It works per rule, because testing each sentence by running would cost too much.

## Recommendation

This recommendation replaces an earlier one (a word-count warning level and a test of the needless-words
rule), after the owner set the measure and the trial ran.

1. **Check each sentence while writing and in review.** Done for this library: the AGENTS.md convention
   and `skill-review` rule 10.
2. **Use the word counts above only to choose where to read first.** A long rule can be easy to
   understand, so a count shouldn't fail a skill or need a recorded limit.
3. **Leave the needless-words rule held under
   [#159](https://github.com/cobarx/build-skills/issues/159).** The trial shortened documents and
   lengthened skill rules, so it isn't the fix for rules.

Confidence is medium. The measurements are solid, but the causes are mostly inferred, the sentence test
has one pass behind it, and I have no evidence on whether shorter rules are followed better.

## What would reverse this

- Rules keep passing the sentence test and still take a person real effort to understand: look for a
  different test, and consider a length check then.
- Tests show that longer rules are followed more reliably: stop treating length as a cost at all.

## Not checked

- Whether length affects how well agents follow a skill. Nothing here tested that.
- What drafted each skill, and how the model or effort affected length.
- Each skill's PR history beyond its first and current versions.
- Other libraries (`ai-skills-cobarx`, `hm-ai-skills`) were not measured.
- Total words for sibling skills are estimated from rules times mean words, so they are marked "about".
