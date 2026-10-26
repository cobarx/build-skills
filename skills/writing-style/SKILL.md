---
name: writing-style
description: This skill should be used when writing or revising sentences someone else will read, such as docs, READMEs, PR descriptions, issues, commit messages, or a report or reply handed to a person; when a sentence reads as clipped, formal or coined; when a term may be new to the reader; or when choosing how to join a point to what elaborates it. It governs how sentences read, not how a document is ordered.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/writing-style"}
---

# writing-style

Write sentences a reader understands on the first reading.

A sentence the reader has to decode twice has handed its work to the reader. Prose that sounds
like one colleague talking to another is usually more exact than clipped or formal prose, because
it keeps the small words that say how one idea relates to the next.

## Rules

1. **The project's own guidance comes first.** Follow the style guide, contributing guide or
   writing conventions of the project you are writing in, including what its existing docs show.
   These rules fill what it leaves unsaid, and any of them gives way when breaking it makes the
   text clearer.[^google]

2. **Use plain words and full sentences.** Write it the way you would say it to a colleague: keep
   the articles and the verbs, and prefer the everyday word ("use", "is") to the formal one. Keep a
   technical term when it is the exact name for the thing. If no one would say a sentence out loud,
   rewrite it.[^fplg][^spec]

3. **Define a term the reader may not know when it first appears.** That includes any name coined
   while working, which means nothing to a reader who wasn't there.[^jargon]

4. **Refer to people by their role.** Not as "I", "we" or "you" meaning the author or the agent,
   but as the owner, the reviewer, the maintainer. "You" addressed to the reader is fine.

5. **Join two ideas with the mark that says how they relate.** Use a colon when what follows
   explains, illustrates or lists what came before; a semicolon for two closely related statements;
   a comma and a word ("because", "so", "but") for cause, consequence or contrast; parentheses for
   an aside; and a period when each idea deserves its own weight. A dash says none of these, so use
   one only when no other mark fits. Swapping every dash for one other mark repeats the
   problem.[^strunk][^sw][^williams]

## Not here

What goes where in a document, including leading with the point and introducing every list, is
`writing-structure`. Spelling, capitalization and other house mechanics are the project's own
guide's (rule 1). Sentence rules still being tested (active voice as a default, omitting needless
words, positive form) are not here yet.

---

Decisions affecting this skill: `docs/decisions/*-writing-style-*.md`

[^google]: Google, *Google developer documentation style guide*, "About this guide", CC BY 4.0,
    <https://developers.google.com/style>: "Follow style guidance specific to your project or
    product."
[^fplg]: *Federal Plain Language Guidelines* (2011), "Use short, simple words", reposted by the
    Center for Plain Language,
    <https://centerforplainlanguage.org/wp-content/uploads/2025/12/FederalPLGuidelines.pdf>.
[^spec]: OpenAI, *Model Spec* (2026-08-18), CC0, <https://model-spec.openai.com/2026-08-18.html>: a
    professional tone "doesn't mean the model should sound stuffy and formal."
[^jargon]: Google, *Google developer documentation style guide*, "Jargon", CC BY 4.0,
    <https://developers.google.com/style/jargon>: define necessary jargon clearly on first use.
[^strunk]: William Strunk Jr., *The Elements of Style* (1920), Rule 5 and the entry on "While",
    public domain, <https://www.gutenberg.org/ebooks/37134>: the semicolon is "this simple method of
    indicating relationship between statements"; an all-purpose connective comes from "uncertainty
    which of the two connectives is the more appropriate."
[^sw]: William Strunk Jr. and E. B. White, *The Elements of Style*, 4th ed. (Allyn & Bacon,
    2000), Rule 8: "Use a dash only when a more common mark of punctuation seems inadequate."
[^williams]: Joseph M. Williams and Joseph Bizup, *Style: Lessons in Clarity and Grace*, 11th ed.
    (Pearson, 2014), Appendix I: punctuation as choices with different effects. Paraphrased.
