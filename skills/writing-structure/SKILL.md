---
name: writing-structure
description: This skill should be used when writing or revising anything someone else will read, such as a README, a doc page, a PR description, an issue, a commit message, or a report or summary handed to a person; when outlining one; when a heading is followed by a bare list; or when reviewing how a document is organized. It governs what goes where in a document, not how its sentences read.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/writing-structure"}
---

# writing-structure

Order a document so its reader gets what they need first.

A document is an output, and its reader is its user. Decide what they will do with it before
deciding what goes in it, and the order follows. Written in the order the material was found, it
reads as notes; written in the order the reader needs it, it reads as help.

## Rules

1. **The project's own guidance comes first.** Follow the style guide, contributing guide or
   writing conventions of the project you are writing in, including what its existing docs and
   `git log` show. These rules fill what it leaves unsaid, and any of them gives way when breaking
   it makes the text clearer.[^google][^git]

2. **Begin with the reader's end.** Before outlining, name who will read it and what they will do
   once they have: approve the change, run the tool, write the next skill. Choose and order the
   content from that, not from the order you found it in.[^covey][^minto]

3. **Lead with the point, at every scale.** The document's answer, decision, request or action
   goes in its first sentence or paragraph; each paragraph's point goes in its first sentence. A
   reader who stops after any opening should already have what matters most there.[^bluf][^strunk]

4. **Order the rest by use.** What to do comes first, the material it uses next, and background
   and provenance last or behind a link.[^pyramid]

5. **Keep how-to, reference and explanation apart.** Steps carry no explanation; link to it
   instead, so each kind can be found without wading through the others.[^diataxis]

6. **Say what each section and list is before it starts.** A heading names what its section is
   for, and a complete sentence introduces each list and says how to use its items. A heading
   followed by a bare list leaves the reader to work out why they are reading it.[^lists]

7. **Give each paragraph one point.** A second point starts a new paragraph, because a new
   paragraph is how the reader knows a new point has begun. A brief subject can take a single
   paragraph.[^strunk]

8. **Name the contents by what they are to the reader,** not by how they were produced: lessons,
   not findings; steps, not results. The right name often shows the right order.

9. **Make it stand on its own.** Write for someone who was not there. Summarize a discussion
   instead of linking to it, and say what a label coined while working means. Keep findings,
   dates and sources (a person quoted as evidence is a source), and drop references to the
   conversation itself.[^git][^cl]

## Not here

How each sentence reads (plain words, defined terms, punctuation) is `writing-style`. Where a
document lives so it can be found is `durable-context`. An essay's byline and revisions are
`essays`. Writing less is `simplicity`. What a document must enable is set the way any goal is,
by `spec`.

---

Decisions affecting this skill: `docs/decisions/*-writing-structure-*.md`

[^google]: Google, *Google developer documentation style guide*, "About this guide", CC BY 4.0,
    <https://developers.google.com/style>: "Follow style guidance specific to your project or
    product." Adapted: a project's visible conventions count as its guidance.
[^git]: The Git project, *SubmittingPatches*, <https://git-scm.com/docs/SubmittingPatches>:
    check `git log` for a project's conventions, and summarize a discussion rather than link to it.
[^covey]: Stephen R. Covey, *The 7 Habits of Highly Effective People* (1989), Habit 2, "Begin
    with the end in mind", <https://www.franklincovey.com/courses/the-7-habits/habit-2/>.
[^minto]: Barbara Minto, *The Pyramid Principle*, <https://www.barbaraminto.com/>: ideas grouped
    under a single point that answers the question in the reader's mind.
[^bluf]: US Army, *Army Regulation 25-50* (10 October 2020), para. 1-38b, copy at
    <https://www.maine.gov/dvem/policies/documents/AR%2025-50%20(10%20October%202020).pdf>:
    "putting the main point at the beginning of the correspondence (bottom line up front)."
[^strunk]: William Strunk Jr., *The Elements of Style* (1920), Rules 8 and 9, public domain,
    <https://www.gutenberg.org/ebooks/37134>: "one paragraph to each topic"; "begin each
    paragraph with a topic sentence."
[^pyramid]: Purdue OWL, "The Inverted Pyramid Structure",
    <https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/the_inverted_pyramid.html>,
    paraphrased: the essential facts lead, and details and background follow in order of
    importance, least important last.
[^diataxis]: Daniele Procida, *Diátaxis*, <https://diataxis.fr/>, paraphrased (CC BY-SA 4.0).
    Adopted in part: how-to, reference and explanation kept apart, with a how-to guide linking to
    explanation rather than holding it; tutorials are left out.
[^lists]: Google, *Google developer documentation style guide*, "Lists", CC BY 4.0,
    <https://developers.google.com/style/lists>: "Introduce a list with a complete sentence."
[^cl]: Google, *Engineering Practices*, "Writing good CL descriptions", CC BY 3.0,
    <https://google.github.io/eng-practices/review/developer/cl-descriptions.html>: links "may not
    be visible to future readers"; "Phase 1." is given as a bad description.
