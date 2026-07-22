# Project Instructions

## Project Purpose

This repository develops SDD Orchestrator, a dashboard and control plane for moving specifications through AI-assisted implementation with local or remote coding agents.

It is also the first real project built with those workflows. Keep the result useful as a maintained personal project. Do not change product or engineering decisions only to produce a cleaner article or demonstration.

Read `README.md` for the project identity, current direction, and unresolved product questions. Treat it as project context, not as an approved implementation specification.

## Shared Codex And Claude Contract

Codex and Claude Code work in the same repository and follow the same engineering rules.

- Keep `AGENTS.md` and `CLAUDE.md` identical.
- Update both files in the same change when a shared rule changes.
- Inspect the working tree before editing.
- Treat existing uncommitted changes as intentional work from the user or another tool.
- Do not revert, overwrite, or reformat changes outside the active task.
- Stop when another active task owns the same files or responsibility.

Canonical project skills live under `.agents/skills/` and follow the shared Agent Skills `SKILL.md` format.

- Codex discovers the canonical skill folders directly.
- Claude Code discovers the same folders through links under `.claude/skills/`.
- Do not maintain a second copy of a skill for one tool.
- Claude Code must be version `2.1.203` or newer because the project uses linked skill folders.

## Source Of Truth

`README.md` describes what the project is. Approved behavior and implementation decisions belong in feature specifications.

Before implementation, read the relevant files under `specs/<feature>/`:

- `requirements.md` defines expected behavior and product boundaries.
- `design.md` defines technical decisions and tradeoffs.
- `tasks.md` defines the active implementation slice and verification state.

Do not replace an explicit project decision with an assumption.

## SDD Workflows

The SDD skills are mandatory. Select the matching skill from the user's intent even when the user does not name the skill explicitly:

- Always use `add-spec` when defining, scoping, planning, or creating a new specification, feature, or implementation slice.
- Always use `update-spec` when changing existing requirements, scope, business rules, design decisions, implementation boundaries, acceptance criteria, or verification expectations.
- Always use `implement-spec` when implementing, continuing, or verifying one approved active slice.

Invoke or activate the matching project skill through the current tool's skill system at the start of every workflow. Do not merely read its `SKILL.md` as reference material and imitate the steps in an ad hoc process.

The active skill must execute the canonical `SKILL.md` under `.agents/skills/`. Codex and Claude Code must execute the same canonical instructions.

When one request combines a new or changed specification with implementation, complete the applicable spec workflow and stop. Begin `implement-spec` only after the specification is reviewed and its active slice is approved.

Spec-only work must stop after the specification and directly requested project guidance are updated. Do not continue into code, migrations, tests, dependencies, or runtime configuration.

## Implementation Workflow

1. Confirm that requirements and design contain no blocking open questions.
2. Work only from the active slice in `tasks.md`.
3. Keep changes inside its implementation boundary.
4. Implement one task at a time.
5. Run the proof attached to each task before marking it complete.
6. Run the full verification gate before calling the slice complete.
7. Write progress and new decisions back to the spec files as the state changes.

## Stop Conditions

Stop implementation and report the issue when:

- The requested change expands the approved scope.
- A missing product, business, or design decision affects implementation.
- The code, acceptance criteria, and existing system disagree.
- A required check fails and cannot be fixed inside the approved slice.
- Continuing would require changing an acceptance criterion to fit the code.
- Another task, Codex session, or Claude Code session owns the same files or responsibility.

Do not continue by silently choosing a new product or architecture decision.

## Write-Back Rules

- Update `requirements.md` when expected behavior, scope, or a business rule changes.
- Update `design.md` when a technical decision or tradeoff changes.
- Update `tasks.md` when progress, verification state, blocked decisions, or deferred work changes.

Keep decisions in project files, not only in the conversation.

## File And Commit Rules

- Do not create Markdown files unless the user explicitly asks for them or an invoked SDD workflow requires its defined spec files.
- Keep changes narrowly scoped to the active task.
- When the user asks for a commit, stage the intended paths and create the local commit with one shell command.
- Always use a conventional semantic prefix such as `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, or `chore:` in commit messages and titles.
- Do not add assistant, model, or tool authorship to commits or titles.
- Commit only when the user asks.

## Current Project Checks

The repository does not have an application toolchain yet.

For instruction and skill changes, run the checks that currently apply:

- Shared instructions: `cmp -s AGENTS.md CLAUDE.md`
- Claude skill links: `find -L .claude/skills -type l` must return no broken links.
- Patch integrity: `git diff --check`
- Skills: validate every changed canonical skill under `.agents/skills/` with the validator provided by the active skill-authoring environment.

When the first executable slice introduces a build, test, type-check, lint, or runtime command, record the canonical commands here and in the relevant verification gate before marking that slice `Approved`.

Do not mark a slice `Verified` while a required check is failing or unavailable without an explicit accepted exception.
