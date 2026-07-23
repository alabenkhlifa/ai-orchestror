---
name: add-spec
description: Create an initial Spec-Driven Development feature specification by inspecting the project, discovering the real users and workflow, resolving consequential product questions, and writing requirements.md, design.md, and tasks.md without implementing code. Use when a user asks to define, brainstorm, specify, plan, scope, or prepare a new feature or implementation slice, including product discovery before technologies are selected.
---

# Add Spec

Activate this skill as the workflow for creating one feature specification without implementing application code.

## Workflow

1. Read the applicable `AGENTS.md` and existing specifications.
2. Inspect the code and documentation where the feature connects.
3. Establish product behavior before architecture:
   - Identify the real user roles and their expected technical knowledge.
   - Identify entry conditions and prerequisites.
   - Map the primary workflow in the order the user experiences it.
   - Define the outcome, scope, rules, acceptance criteria, and failure behavior.
4. Separate product decisions from technology decisions. When technology is intentionally deferred, describe logical responsibilities, boundaries, interfaces, risks, and the decisions that block implementation without inventing a stack.
5. Apply a decision-ownership gate before asking a question:
   - Ask the user when the answer changes observable behavior, workflow, scope, a business rule, ownership, data handling, risk acceptance, or an acceptance outcome.
   - When alternatives preserve the accepted product outcome, record the implementation mechanism as a consolidated design question or task blocker for engineering instead of asking the user to choose it.
6. Ask one consequential user-owned question at a time when the request remains ambiguous. Explain the impact and recommend a default when one is justified.
7. Stop discovery once there is enough agreement to write a useful `Draft`. Record remaining decisions under `Open Questions` instead of extending the conversation indefinitely.
8. Define the bounded feature in `requirements.md` and `design.md`, then limit `tasks.md` to the first end-to-end executable slice. Record required later behavior as deferred after the active slice, not as part of its implementation boundary.
9. For complex work, use Plan mode to produce and approve the proposal. Return to Default mode before writing files.
10. Copy the bundled templates from `assets/` into `specs/<feature>/` and replace every placeholder.
11. Set status from the actual decision state: keep requirements `Draft` while product questions remain, and mark tasks `Blocked` while implementation decisions remain unresolved.
12. Run `python3 .agents/scripts/validate_spec.py specs/<feature>` when the project validator exists, then manually confirm that requirements, design, tasks, and proof agree.
13. Report files created, assumptions, unresolved product and technology questions, active-slice boundary, and approval status.

## Discovery Rules

- Do not assume the primary user is a developer because the product concerns software or AI agents.
- Do not start from the most technically interesting capability. Follow prerequisites and the user's operational order.
- Write rules with concrete examples when naming, allocation, ownership, permissions, state transitions, or failure recovery could be interpreted more than one way.
- Distinguish stable domain identity, display labels, ownership scope, and uniqueness constraints.
- Match specificity to decision ownership. Be exact about outcomes and constraints without making requirements exhaustive about implementation mechanics.
- Use representative examples and acceptance criteria when they establish the rule. Do not expand them into a combinatorial technical test matrix.
- Consolidate related engineering unknowns into one design gate instead of asking a sequence of implementation-level questions.

## Boundaries

- Do not implement code, migrations, tests, APIs, or UI behavior.
- Do not silently decide consequential product or architecture questions.
- Do not select technologies the user intentionally deferred.
- Do not transfer engineering decision ownership to the user merely because the specification could contain more detail.
- Do not mark a specification `Approved` while blocking questions remain.
- Keep real specification files free of teaching labels or unexplained placeholders.

## Completion

Finish when all three files exist, agree on the full feature and first active slice, pass available mechanical checks, and make the next required decision visible.
