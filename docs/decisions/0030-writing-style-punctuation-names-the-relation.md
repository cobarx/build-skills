# 0030. Punctuation names the relation, rather than banning the dash

- **Status:** Accepted
- **Decided:** 2026-10-26 · **Recorded:** 2026-10-26 · Claude Opus 5.5
- **Affects:** `writing-style` (new)

## Context

The owner bans em dashes in his own agent instructions. Asked whether that is house style, he
answered that it is a matter of quality: "it's sloppy writing because it's the only convention that
AI typically uses to make a point and elaborate on it." One mark doing every job (explaining,
adding an aside, contrasting, emphasizing) leaves the reader to work out how the second half of a
sentence relates to the first.

The research for 0029 ([docs/context/writing-research.md](../context/writing-research.md)) found
no source that bans the dash, and every source that discusses it choosing the joining mark by the
relation between the two parts. Strunk (1920, Rule 5) recommends the semicolon as a way of
"indicating relationship between statements", and in his entry on "while" diagnoses the same
failure in a word: writers reach for an all-purpose connective out of "uncertainty which of the
two connectives is the more appropriate." Strunk & White (4th ed., Rule 8): "Use a dash only when
a more common mark of punctuation seems inadequate." Williams (*Style*, Appendix I) gives each mark
a reading: a colon as "for example, that is, therefore", a dash as a casual afterthought. Google's
style guide limits the em dash to a break in a sentence and prefers a colon or period between an
item and its description.

Wikipedia's editors, cataloguing signs of AI writing, report that models hard-coded against em
dashes stopped using other kinds of punctuation, and that the resulting run of commas and
periods "has become its own sign of AI writing." The claim is tagged "citation needed".
Anthropic's prompting guidance makes the general point: tell a model what to do rather than what
not to do.

## Options

- **Ban the em dash in the skill.** Matches the owner's preference, but the skill must work in
  other people's repos (0029), where a dash may be their house style, and a ban alone tends to
  produce a new single default.
- **Leave punctuation to house style.** Treats as preference what the owner and the sources treat
  as clarity.
- **Choose the mark by the relation.** Name which mark fits which relation, and make the dash the
  last resort, after Strunk & White.

## Decision

Choose the mark by the relation. `writing-style` rule 5 names a mark for each relation (colon,
semicolon, a comma with "because", "so" or "but", parentheses, a period) and allows a dash only
when none fits. It also says that replacing every dash with one other mark repeats the problem,
since the fault is the single default, not the particular mark.

The owner's outright ban stays in his own agent instructions, where it applies to his writing; a
project's own guide decides for itself (0029).

## Consequences

- In the owner's repos the ban and the rule agree. Elsewhere, a writer following the rule rarely
  reaches for a dash, without the skill overriding a project that uses them.
- Whether the rule changes what an agent writes is untested; it belongs in the evals that
  [#159](https://github.com/cobarx/build-skills/issues/159) covers.
