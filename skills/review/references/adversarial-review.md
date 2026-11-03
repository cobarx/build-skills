# Adversarial review

An adversarial review tries to break a change before its author blesses it. It is an explicitly
invoked mode of `review`, not a separate skill. The critic is not the author and does not see the
author's framing before writing findings.

## When to run it

Run the mode when the owner asks for an adversarial review, or when a change adds or changes a
skill, changes a public contract, makes a one-way-door decision, or touches security-sensitive
code. A one-way door is a decision that is expensive to reverse.

Skip the mode for typos, formatting, renames, mechanical refactors, and docs-only edits. Ordinary
review covers those changes.

One critic is enough for a normal change. Use a second critic with a disjoint lens only when the
change is irreversible or wide, and run the two critics in isolation. Two generalists duplicate
each other.

## The design pass

Before the build, run a premortem. Assume the change shipped and failed. Write the concrete failure
story: who is hurt, what breaks, and why the goal was missed. Then answer these questions:

- What would make this the wrong thing to build?
- Which assumption would have to be false?
- What fails even if the implementation is perfect?
- What would a critic build instead, and why?

The output is proceed, reshape, or stop, with the strongest failure story and what would change the
decision. A short written premortem is enough for a small change. The design pass is mandatory when
the change is a one-way door.

## The diff pass

After the build, and before the author's self-review is shared, give the critic these inputs:

- the artifact: a diff, PR, skill, or design document;
- the goal: the spec, or the unit's own goal;
- the standards: the skills and project conventions the change claims to meet;
- how to run it: commands, fixtures, and environment.

Do not give the critic the author's summary, plan narrative, or self-review. The critic writes
findings before reading them.

For each lens, name what it tries to disprove, then try it. Use correctness, simplicity, and the
user's purpose by default. Add the others only when the change touches them.

- **correctness:** an input, state, or sequence where the claimed behavior fails.
- **simplicity:** a second thing the change does, or a reader who must hold unrelated things.
- **user's purpose:** a real use where the output does not serve the goal.
- **contract:** a caller that must know an internal detail.
- **evidence:** a check that passes while the goal is missed.
- **environment:** a supported platform or version where it behaves differently.

A lens with no attempted disproof is not a pass. A review that reports no findings must list what
it tried.

## Evidence and verdicts

Every finding has a reproduction: an input, command, line, or state that shows the failure. A claim
without one is a preference, not a finding.

A check the critic cannot run is `blocked`. The review names what would unblock it. Do not pass a
blocked check.

## The review of record

Keep one comment and edit it each pass. Put the verdict first, then the findings, then the attempted
disproofs.

```markdown
## Adversarial review

Artifact: <commit or PR>
Goal: <link>
Standards: <skills>

| Lens | Verdict | Evidence |
|---|---|---|
| correctness | pass | <what was tried> |
| simplicity | pass | <what was tried> |

Findings:

1. [blocker|major|minor] <claim>. Reproduce: <command, input, or state>. Expected: <...>. Actual:
   <...>.

Attempted disproofs: <what each lens tried>.

Critic: <fresh context, model>. The author's summary and self-review were not seen before the
findings were written.
```

The author fixes or rebuts with evidence. The critic rechecks the same finding against the same
reproduction and updates the one record. A finding closes when the reproduction no longer fails, or
when the author shows the standard does not apply. The critic does not edit the artifact. A critic
that fixes the work is the author again.

## Independence

The critic is a fresh agent session with no shared context with the author. A different model is
better where one is available; a fresh context on the same model is the minimum. The critic writes
findings before seeing the author's response. A human takes any check that needs physical use or a
capability the agent lacks.

The critic reports; the author fixes.
