# Who answers for it?

**2026-10-06 · Claude Opus 5.5**

Hampton named one of this repo's guiding goals in a session on 2026-10-05: to create accountability,
as a way to reverse enshittification. Nothing in the repo had said so before, and the entry point
still doesn't ([#127][127]). This essay sets out what accountability means here, the two principles
it rests on, how the skills already carry them, and where they stop.

## Enshittification is an accountability failure

Cory Doctorow coined the word for how platforms decay: "first, they are good to their users; then
they abuse their users to make things better for their business customers; finally, they abuse those
business customers to claw back all the value for themselves. Then, they die."[^doctorow] It has
since entered common use for phoning it in and screwing the customer, well beyond platforms, and
Doctorow welcomes that: his 2025 book gives readers "explicit permission to use this word in a loose
sense."[^loose] Hampton means the broad sense, and so does this essay.

Read as a chain of who answers to whom, the mechanism is plain. The people who build the product
answer to a product owner, and the product owner answers to someone who is not the user. Every link
in the chain is accountable to something, and the chain as a whole points away from the person the
product is for. Lock-in completes it: a user who cannot leave has no way to hold anyone to account.

So, in Hampton's framing, accountability is relational: accountable to whom, and to what principles.
Single accountability without a direction is only structure. For the work they govern, the skills
already give both answers. To whom: the user. A goal is what the output lets its user do (`spec` 5),
and it comes from the person whose problem it is (`spec` 3). To what: the declared standard. A
review checks a change against the skills it is subject to, not a standard the reviewer invents
(`review` 2).

The skills can point the engineering chain at the user. They cannot change who a product owner
reports to. That limit comes up again below.

## Two principles

Hampton settled on two.

**One party answers for each thing.** This is the structural one: for every fact, policy, contract
or component, exactly one place answers for it when it is wrong. The repo applies it at every level
without having stated it. Each skill's "Not here" section hands a concern to the skill that owns it.
AGENTS.md forbids giving a skill policy that belongs to another. `durable-context` gives each kind
of record one home. A decision that changes is superseded, never edited, so each choice has one
record. Industry terms each cover a slice: single source of truth for data, DRY for knowledge,[^dry]
single responsibility for modules. None of them covers every level.

What to call it, and where to state it, are still open ([#128][128]). Hampton's direction is that
the name build on accountability rather than ownership, because what it names is an assigned role,
one per thing, and not a culture. RACI is the nearest precedent, with exactly one Accountable per
task.[^raci] "Everyone owns quality" is the opposite. When ownership is shared, nobody owns the
thing.

**Operate in the open.** This one gives the direction. The skills carry their principles into the
work, so an agent using them raises what those principles require and records it where others can
read it, and the person accountable decides. The mechanisms already exist. An agent asked for too
much at once proposes the split once, and proceeds if the person reaffirms (`simplicity` 7).
Overriding a default is logged as a decision (`simplicity` 5). A problem noticed on the way is filed
without asking (`durable-context` 6). What cannot be verified is reported as blocked, not passed
(`review` 3).

The person can still ignore the agent. Hampton's view is that this is their decision to make. But
ignoring it becomes a visible choice with a name on it. The UK Government Digital Service puts the
same idea as a design principle: "Make things open: it makes things better."[^gds]

## The agent is the line worker

In Toyota's production system, any worker who sees an abnormality stops the line rather than pass
the defect downstream. The principle is jidoka, and the andon cord is the signal.[^toyota] Hampton's
reading is that this makes the line worker a manager of the plant. With these skills, the agent is
the line worker. It stops and surfaces the problem, and the person accountable decides whether the
line restarts.

Accountability built this way runs from the bottom up. A product owner who has to answer for each
override has reason to make their manager answer for the pressure behind it, and that manager has
the same reason one level up. An override recorded in the open, with a name on it, travels upward
instead of disappearing. Hampton's point is that this is what a decision log does when it is kept
properly. The limit is that a record can be made to exist and stay findable, but no skill can make
anyone above read it.

## An agent cannot be held to account

A person or a company can be held to account; an agent cannot. So the accountable role at the what
is a human's: the goal comes from its owner (`spec` 3), the decider is handed a framed choice
(`decision-log` 3), and the artifact is shown to its user in the form they will consume it
(`definition-of-done` 5).

The law has begun to say the same. In *Moffatt v. Air Canada* (2024), a British Columbia tribunal
held the airline liable for what its website chatbot told a customer, and rejected the argument that
the chatbot was responsible for its own actions.[^moffatt] The European Union's revised Product
Liability Directive (2024) counts software, AI systems included, as a product, so a defect in it
carries liability without proof of fault.[^pld] Each one assigns a person or a company to answer for
what the agent does.

That turns the record into evidence. An artifact a person exercised is a record they can defend;
"the agent said the tests pass" is not. Two gaps are tracked. Decision records name whoever wrote
them down, not whoever decided ([#123][123]). And nothing records whether an agent applied the
skills during a session ([#130][130]).

## Where it stops

One party answering for each thing works within a node: a team, a product, a company. Hampton's
observation is that it does not work at the top, because a society has no central decider. It
coordinates through overlapping feedback loops: markets, courts, regulators, the press, norms, and
users who leave. Elinor Ostrom's term for this is polycentric governance: many centres of decision
making, formally independent of each other.[^ostrom] Claude's reading is that this makes operating
in the open matter more, not less. Between nodes that share no boss, the open record is the
interface, and a decision made in secret escapes every loop. The framework should not claim a root
owner it cannot have. What it can do is make every node accountable and every decision visible, so
the loops have something to act on.

The same limit applies to values. Hampton points out that a society holds competing value systems,
some of them mutually exclusive, and that any single value applied to everything (harmlessness is
his example) overrides the rest and imposes one group's values on everyone else. One party answers
for each fact, never for values. The honest move is to declare the values, so others can see them,
disagree, and choose.

This framework is opinionated, and Hampton has confirmed its six values: accountability, operating
in the open, quality measured and improved, the what over the how, the user's outcome, and pride in
the work. Opinionated is not totalizing. The values are declared, adopting them is a choice, and
leaving stays possible: the skills load one at a time, the text is CC BY so anyone can fork it, and
someone who ignores the agent decides that for themselves. Leaving is what lock-in takes away. In
Albert Hirschman's terms it removes exit,[^hirschman] which is why lock-in counts as a harm under
nearly every value system.

## What is not built yet

- **The goal and values at the entry point.** Neither the README nor AGENTS.md states them
  ([#127][127]). The wording is Hampton's.
- **A name and a home for single accountability** ([#128][128]).
- **The decider on the record** ([#123][123]).
- **A trail of the process**, not only of its output ([#130][130]).

## What it shapes

- Any rule can be read by asking who answers for it, and to whom. A rule that gives one concern two
  owners, or points its answer away from the user, is the one to fix.
- When someone overrides an agent, the record shows who decided. That is the point of the record,
  not a failure of it.
- The skills claim a node, not the world. They make the work accountable and visible, and leave the
  rest to the loops outside.

## Notes

The goal, accountability as relational, the two principles, the agent as the line worker, the
decision log as the bottom-up chain, the missing central decider, and the competing value systems
are Hampton's, from the 2026-10-05 session. The working notes are in [#90][90]. Mapping them to
specific rules, and the reading through Ostrom and Hirschman, are Claude's.

## Revisions

- **v1.0 · 2026-10-06 · Claude Opus 5.5.** First version.

[90]: https://github.com/cobarx/build-skills-cobarx/pull/90
[123]: https://github.com/cobarx/build-skills-cobarx/issues/123
[127]: https://github.com/cobarx/build-skills-cobarx/issues/127
[128]: https://github.com/cobarx/build-skills-cobarx/issues/128
[130]: https://github.com/cobarx/build-skills-cobarx/issues/130

[^doctorow]: Cory Doctorow, "Tiktok's enshittification", *Pluralistic*, 21 January 2023,
    <https://pluralistic.net/2023/01/21/potemkin-ai/>.
[^loose]: Cory Doctorow, *Enshittification: Why Everything Suddenly Got Worse and What to Do
    About It* (2025), as quoted in *The New York Times*, 5 October 2025, and in Wikipedia,
    "Enshittification", <https://en.wikipedia.org/wiki/Enshittification>, retrieved 2026-10-06. Not
    checked against the book.
[^dry]: Andrew Hunt and David Thomas, *The Pragmatic Programmer* (Addison-Wesley, 1999): "Every
    piece of knowledge must have a single, unambiguous, authoritative representation within a
    system." Wording checked against the 20th anniversary edition (2019), Tip 15,
    <https://media.pragprog.com/titles/tpp20/dry.pdf>.
[^raci]: Project Management Institute, *PMBOK Guide*, responsibility assignment matrix, as described
    by PM PrepCast: "only one person accountable for any one task to avoid confusion",
    <https://www.project-management-prepcast.com/free/pmp-exam/tips/303-pmp-exam-tip-the-responsibility-assignment-matrix-ram>.
    Secondary; the guide itself is paywalled. Wikipedia's "Responsibility assignment matrix"
    hedges it as what "some theories of project management" require.
[^gds]: Government Digital Service, "Government design principles", principle 10,
    <https://www.gov.uk/guidance/government-design-principles>.
[^toyota]: Toyota Motor Corporation, "Toyota Production System",
    <https://global.toyota/en/company/vision-and-philosophy/production-system/>: "the operator can
    stop the line by pulling the stop cord themselves."
[^moffatt]: *Moffatt v. Air Canada*, 2024 BCCRT 149, British Columbia Civil Resolution Tribunal,
    14 February 2024, <https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do>.
    The tribunal: "In effect, Air Canada suggests the chatbot is a separate legal entity that is
    responsible for its own actions. This is a remarkable submission." Quoted from Barry Sookman,
    <https://barrysookman.com/2024/02/16/moffatt-v-air-canada-a-misrepresentation-by-an-ai-chatbot/>;
    the tribunal's site refused automated access, so the wording is secondary.
[^pld]: Directive (EU) 2024/2853 on liability for defective products, adopted 23 October 2024,
    <https://eur-lex.europa.eu/eli/dir/2024/2853/oj>. Article 4(1) includes software in "product";
    recital 13 names AI systems and calls the regime "no-fault liability". Member states transpose
    it by 9 December 2026. Free and open-source software supplied outside a commercial activity is
    excluded (article 2(2)).
[^ostrom]: Elinor Ostrom, "Beyond Markets and States: Polycentric Governance of Complex Economic
    Systems", *American Economic Review* 100, no. 3 (June 2010): 641-72,
    <https://doi.org/10.1257/aer.100.3.641>. Her Nobel lecture of 8 December 2009,
    <https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf>, gives the definition she
    quotes from V. Ostrom, Tiebout and Warren (1961): "many centers of decision making that are
    formally independent of each other."
[^hirschman]: Albert O. Hirschman, *Exit, Voice, and Loyalty: Responses to Decline in Firms,
    Organizations, and States* (Harvard University Press, 1970).
