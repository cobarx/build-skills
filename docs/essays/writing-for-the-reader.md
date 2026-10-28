# Writing for the reader

**2026-10-26 · Claude Opus 5.5**

`writing-structure` and `writing-style` say very little that is new. The guidance on how to write
clearly was mostly settled long ago, and a century of style guides, military and government
standards, documentation frameworks and developer conventions agree on a small core. What an agent
needed was a version of that core it could apply: which rules give way to a project's own guide,
how to state a rule so it doesn't create a new bad habit, and which famous rules to hold back.
This essay covers how the two skills came about, what the research found, and why some well-known
advice is not in them yet.

## A document that didn't work

The skills started with one document. In a session on sysadmin-skills, I had written a file of
lessons from 35 solved troubleshooting cases, kept for skills that hadn't been written yet. Hampton
reviewed it and found it hard to use, and his corrections came one at a time.

The first was about a single line: "What bore on `operate` went into it." His reaction: "this
doesn't read like english. what bore on is not a common phrase." The second was about the whole
opening: "there's nothing that bridges the header of the doc to the findings. Like, it's not even
clear what the findings are, just that there are findings." The third was a word: "You note
findings when really these are lessons. If you approach it that way, you may see that it shapes
the doc. Towards a more actionable flow." The fourth was how to work: "start with end goals in mind
and then work backwards. That then you are filling in details that help you arrive at the
conclusion rather than just throwing information at the problem."

Each correction pointed at the same mistake. I had written the document in the order I found the
material: where the cases came from, then what turned up, sorted by skill. Its reader was someone
about to write one of those skills, and that person needed to know first what to do with an item,
then the items, and only last where they came from. Rebuilt in that order, with each item stated
as something to do, the document worked.

## Begin with the end in mind

Hampton's fourth correction is Stephen Covey's second habit, "begin with the end in mind".[^covey]
When I first relayed the research, I called Covey the weak link, because no source applied Habit 2
to how a document is organized. Hampton disagreed: "ideas are routinely transferred from one domain
to another, or in this case, it's a general principle for life being applied to technical
writing. That's exactly what he intended." He was right, and the research shows why the transfer
works. The methods written specifically for documents are this principle with the mechanics filled
in.

Barbara Minto's Pyramid Principle groups everything under a single point that answers the question
in the reader's mind.[^minto] The US Army requires "putting the main point at the beginning of the
correspondence (bottom line up front)."[^bluf] Journalism's inverted pyramid puts what matters most
first, so a reader who stops early still has it.[^owl] The plain-language standard ISO 24495-1
defines success as readers who "can easily find what they need, understand what they find, and use
that information."[^iso] Diátaxis, the most widely adopted open framework for documentation, keeps
how-to guides, reference and explanation in separate places,[^diataxis] and DITA (the OASIS
standard for technical documentation) splits its topics the same way. Six traditions, from
self-management to technical documentation, arrive at one sequence: name the reader's goal, put the
point first, keep different kinds of material apart, and put background last. That sequence is
rules 2 to 4 of `writing-structure`.

Hampton's word correction became rule 6, and I think it's the most useful thing to come out of the
session. Calling the items "findings" named how they were produced. Calling them "lessons" named
what they were to the reader, and once they were lessons, each one had to be something to do, and
the document had to start with how to use one. The name chose the order.

## Writing for someone who wasn't there

The fifth rule-shaped correction came from a commit message. I showed Hampton two versions of the
same message, one that only made sense to someone who had seen our conversation ("Address review
comment on line 107, per the patch/sed discussion") and one that stated the finding, how it was
checked and when. He noted that participants may not need the context spelled out, "however, the
second one still reads better even if you do have the context. And you would have to spend a bit of
time to determine, are you squashed and merging or relying on the PR description or relying on the
commit log? That's tough. So generalizing to the more complete case is probably better."

That second point is why `writing-structure` rule 7 has no exception for insiders. A writer can't
know which surface the text will end up on, and the version written for a stranger costs the
insider nothing. The git project says the same about commit messages: summarize the discussion
rather than link to it.[^git] Google's guide to change descriptions lists "Phase 1." as a bad
example,[^cl] which is the session label in its purest form.

## Whose standard

The two skills had to work in places their author doesn't control. Hampton raised both cases:
"Somebody might pull down the sysadmin skills repo, but not have build skills. Also, I'm going to
be using build skills with other people's repos where they aren't using it." He then drew the line
that settled it: there are skills "that help shape how I contribute documentation and PR
descriptions," and there are "standards or best practices that are going to define what docs
should look like in a given repo."

So a repo states its own standard in its own files, where anyone can read it without these skills.
The skills govern how a contributor writes, and defer to that standard wherever there is one.
Google's developer style guide already had the rule, in nearly the words we needed: "Follow style
guidance specific to your project or product. ... If project-specific style guidelines don't provide
explicit guidance, then follow this guide."[^google] It also says to depart from the guide "when
doing so improves your content." That became rule 1 of both skills, with one addition of ours: a
project's visible conventions (its existing docs, its `git log`) count as its guidance even when
nothing is written down. Hampton's own preferences, such as no em dashes, stay in his own agent
instructions.

## Two skills, because structure and style are different jobs

Hampton suggested the split early: "Maybe that needs to be a separate skill too, in terms of style
versus how you outline and make points." The research agreed. Joseph Williams' *Style* divides
itself this way, with one part on sentences and another on whole documents.[^williams] The Federal
Plain Language Guidelines separate organizing a document from writing it.[^fplg] The literatures
specialize too: Strunk and Orwell say nothing about how to plan a document, and Minto and Diátaxis
say nothing about sentences. The failures in our own case split the same way. A bare list under a
heading is a structure failure, and "what bore on" is a sentence failure.

Hampton also turned down putting this in `organize`, his skill for laying out projects and
READMEs: "A more specific skill that's tuned to writing is probably going to produce better
results."

## The em dash

Hampton bans em dashes in his own instructions, and I first filed that under house style, like the
serial comma. He corrected me: "it's not just that it's a tell, it's sloppy writing because it's
the only convention that AI typically uses to make a point and elaborate on it." The fault is one
mark doing every job, so the reader can't tell whether the second half explains, qualifies or
contrasts with the first.

No source bans the dash, but every source that discusses it chooses the joining mark by how the
two parts relate. Strunk diagnosed the same habit a century ago in a word rather than a mark:
writers use "while" for "and" or "but" out of "uncertainty which of the two connectives is the more
appropriate."[^strunk] Strunk & White: "Use a dash only when a more common mark of punctuation
seems inadequate."[^sw] Wikipedia's editors, cataloguing the signs of AI writing, add the warning
that made us word the rule carefully. They report that models hard-coded against em dashes stopped
using other punctuation and produced a flat run of commas and periods, which "has become its own
sign of AI writing" (a claim the page itself marks as needing a citation).[^wiki] A ban moves the
habit to a new mark. So `writing-style` rule 5 names a mark for each relation and makes the dash
the last resort. Decision 0030 records why.

## What isn't in the skills yet

The classic sentence rules are the obvious gap. Hampton was candid about them: "I don't have enough
familiarity with them to blindly accept them," and he asked to "adopt the things that I have high
confidence in, and then do some tests with the other ideas and see how they inform the documents
that are generated."

The research gives good reason to test before adopting. Strunk's rules hold up better than their
reputation, but only with the qualifications he attached. He calls the passive "frequently
convenient and sometimes necessary," and Geoffrey Pullum shows that three of the four "passive"
examples in Strunk & White aren't passives at all.[^pullum] Active voice, which most people would
assume is always better, isn't: the passive is right when who acted is unknown or doesn't matter,
or when it keeps the familiar term at the front of the sentence. A study of AI-written text found
that GPT-4o uses agentless passives at about half the human rate, while instruction-tuned models in
general overuse nominalizations and "-ing" clauses.[^pnas] Williams' versions of the rules (make
the characters the subjects and their actions the verbs, put familiar information before new)
target those excesses directly. They are the strongest candidates for the tests.

Some advice is left out on purpose: usage folklore such as the split-infinitive ban, which Pullum
and Williams both reject; lists of banned words, which go stale with each model generation; fixed
sentence-length caps; and maxims like "be clear" that no one can check. Conventions for specific
artifacts (commit messages, PR descriptions, issues, READMEs) are well established and come next,
as a reference file.

## What it shapes

Both skills cite every rule's source in a footnote, quoting public-domain and openly licensed text
and paraphrasing the rest. The research behind them, with every link and licence, is in
[docs/context/writing-research.md](../context/writing-research.md). The decisions are
[0029](../decisions/0029-writing-structure-writing-style-two-skills-project-guide-first.md) (two
skills, and the project's guide first) and
[0030](../decisions/0030-writing-style-punctuation-names-the-relation.md) (punctuation by relation).

One small test ran before the first PR. Two agents turned the same raw notes into a document, one
with `writing-structure` and one without. The one without wrote "Findings that bore on `operate`
went into it," nearly the sentence that started all this, and put the document's history before
how to use it. The one with the skill called the items lessons, introduced every list, and put the
history last. One run each proves little, and the evals are the real test.

## Notes

The corrections quoted here are Hampton's, from a sysadmin-skills session on 2026-10-26 (some
spoken, by dictation). The reading of them, and the rest of the argument, are mine.

## Revisions

- **v1.0 · 2026-10-26 · Claude Opus 5.5.** First version.

[^covey]: Stephen R. Covey, *The 7 Habits of Highly Effective People* (1989), Habit 2,
    <https://www.franklincovey.com/courses/the-7-habits/habit-2/>.
[^minto]: Barbara Minto, *The Pyramid Principle*, <https://www.barbaraminto.com/>.
[^bluf]: US Army, *Army Regulation 25-50* (2020), para. 1-38b.
[^owl]: Purdue OWL, "The Inverted Pyramid",
    <https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/the_inverted_pyramid.html>.
[^iso]: ISO 24495-1:2023, *Plain language, Part 1: Governing principles*, definition as quoted by
    <https://plainlanguage.com/what-is-plain-language/iso-plain-language-standard/>. Not read in
    full; the standard is paid.
[^diataxis]: Daniele Procida, *Diátaxis*, <https://diataxis.fr/>. Paraphrased (CC BY-SA 4.0).
[^git]: The Git project, *SubmittingPatches*, <https://git-scm.com/docs/SubmittingPatches>.
[^cl]: Google, *Engineering Practices*, "Writing good CL descriptions", CC BY 3.0,
    <https://google.github.io/eng-practices/review/developer/cl-descriptions.html>.
[^google]: Google, *Google developer documentation style guide*, CC BY 4.0,
    <https://developers.google.com/style>.
[^williams]: Joseph M. Williams and Joseph Bizup, *Style: Lessons in Clarity and Grace*, 11th ed.
    (Pearson, 2014), Parts Two and Three.
[^fplg]: *Federal Plain Language Guidelines* (2011), reposted by the Center for Plain Language,
    <https://centerforplainlanguage.org/wp-content/uploads/2025/12/FederalPLGuidelines.pdf>.
[^strunk]: William Strunk Jr., *The Elements of Style* (1920), "While", public domain,
    <https://www.gutenberg.org/ebooks/37134>.
[^sw]: William Strunk Jr. and E. B. White, *The Elements of Style*, 4th ed. (Allyn & Bacon,
    2000), Rule 8.
[^wiki]: Wikipedia, "Wikipedia:Signs of AI writing", CC BY-SA 4.0,
    <https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing>. Paraphrased except the quoted
    phrase.
[^pullum]: Geoffrey K. Pullum, "50 Years of Stupid Grammar Advice", *The Chronicle of Higher
    Education*, 2009, <https://www.lel.ed.ac.uk/~gpullum/50years.pdf>.
[^pnas]: Alex Reinhart et al., "Do LLMs write like humans? Variation in grammatical and rhetorical
    styles", *PNAS* 122(8), 2025, doi:10.1073/pnas.2422455122,
    <https://pmc.ncbi.nlm.nih.gov/articles/PMC11874169/>.
