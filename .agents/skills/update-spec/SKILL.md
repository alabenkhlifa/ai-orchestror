---
name: update-spec
description: Update an existing Spec-Driven Development specification when a user clarifies or resolves an open question, or when requirements, scope, business rules, architecture decisions, implementation boundaries, acceptance criteria, or verification expectations change. Use during discovery, review, implementation feedback, or failed verification when the agreement must change before coding continues. Do not implement the change.
---

# Update Spec

Activate this skill as the workflow for restoring agreement between requirements, design, tasks, and proof without implementing the change.

## Workflow

1. Read the applicable `AGENTS.md` and the feature's `requirements.md`, `design.md`, and `tasks.md`.
2. Inspect the code, discovery, or failed check that triggered the update.
3. Classify the affected decision, such as user, workflow, scope, business rule, identity, ownership, state, acceptance criterion, architecture, task boundary, or proof. Explain the cross-file impact before editing.
4. Ask one consequential question at a time when the requested change is ambiguous. Do not fill a material gap with an implementation assumption.
5. For consequential or complex changes, use Plan mode to approve an update proposal. Return to Default mode before writing files.
6. Trace the decision through every affected surface:
   - `requirements.md`: workflow, scope, rules, acceptance criteria, and open questions.
   - `design.md`: logical approach, domain and access boundaries, interfaces, decisions, tradeoffs, risks, and technical questions.
   - `tasks.md`: active-slice boundary, implementation steps, proof, verification gate, blockers, deferred work, and progress log.
7. Remove or replace resolved questions, stale blockers, contradicted wording, and invalid proof. Preserve a replaced tradeoff by recording the new choice and consequence.
8. Keep technologies deferred when the decision is still product-level. Add technical consequences as open questions instead of selecting a stack implicitly.
9. Set status from the resulting state. Move requirements to `Draft` or tasks to `Blocked` when decisions remain, and remove `Verified` whenever existing proof no longer covers the changed behavior.
10. Run `python3 .agents/scripts/validate_spec.py specs/<feature>` when the project validator exists, then manually confirm that every changed decision agrees across files.
11. Report the changed decisions, newly exposed questions, invalidated or deferred work, status changes, and whether implementation can resume.

## Decision Rules

- Distinguish stable domain identity, display labels, ownership scope, and uniqueness constraints.
- Add concrete examples when rules involve naming, allocation, permissions, state transitions, ordering, or recovery.
- Add concurrency, security, or failure implications only when they follow from the decision; keep unselected implementation details open.

## Boundaries

- Do not implement application changes.
- Do not rewrite unrelated specification sections.
- Do not erase a tradeoff without recording its replacement.
- Do not weaken acceptance criteria to make failing code pass.
- Do not mark implementation as resumable while product, architecture, or verification blockers remain.

## Completion

Finish when the changed decision and its proof are visible, affected files agree, stale questions and blockers are removed, available mechanical checks pass, and implementation state is accurate.
