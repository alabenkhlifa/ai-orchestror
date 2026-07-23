# SDD Orchestrator

Status: early product discovery.

## Overview

SDD Orchestrator is a dashboard and control plane for Spec-Driven AI-Assisted Development.

It is intended to help developers move work from specifications to verified implementation while keeping agent execution, stop conditions, progress, and proof visible.

Coding agents can run locally on the user's computer or through remote workers hosted in the cloud or on user-managed hardware such as a Raspberry Pi.

This is a real personal project and the first project being built with the SDD workflow it is intended to support. The product must remain useful beyond the articles and book material produced from the experience.

## Product Direction

The current direction includes:

- A dashboard dedicated to the SDD lifecycle rather than general task management.
- Visible specifications, implementation slices, agent runs, blocked decisions, and verification results.
- Local execution on the user's current computer.
- Remote execution in cloud environments or on user-managed workers.
- OpenAI Codex as the primary coding agent.
- A clear provider setup experience for credentials and model selection.
- Support for OpenAI models with room for other providers and locally hosted models.
- GDPR data protection by design and by default across every database schema, backend path, integration, worker, agent, log, export, retention process, and deletion process.
- Aggregate analytics that are genuinely anonymous and cannot be linked to users, devices, workspaces, projects, repositories, network identifiers, or source content.

This direction is not an approved V1 specification. Product discovery is still in progress.

## Core Product Loop

In simple terms, SDD Orchestrator lets developers and non-developers use development AI agents running on their laptop or on another machine.

1. A user creates a feature on a specification-focused Kanban board.
2. The product explains the required format, identifies missing or unclear information, and shows what prevents the feature from being ready for development.
3. When the requirements are sufficient, the feature becomes development-ready and the user can explicitly start development.
4. An authorized AI coding agent works from an isolated branch, implements the feature, runs tests, and captures screenshots when the project and environment support them.
5. Progress, test results, screenshots, and other evidence are attached to the feature activity and comments.
6. If the agent needs a product decision, it marks the work blocked, tags the relevant users, asks a focused question, and preserves its current state.
7. After an accepted answer is written back to the specification, the agent resumes until the work and verification finish.
8. When supported, the branch is deployed to a preview environment and the user receives a test link. The product then notifies the user that the run has finished and shows its result and evidence.

The detailed product contract for this loop starts in `specs/07-guided-specification-delivery/`.

## Implementation Foundation

[OpenAI Symphony](https://github.com/openai/symphony) is the implementation foundation for SDD Orchestrator. Its language-independent specification and Elixir reference implementation provide a starting point for isolated workspaces, coding-agent execution, work reconciliation, retries, and operational visibility.

Symphony is a foundation, not a fixed architecture or product boundary. The project may reuse, extend, replace, or reimplement any part when approved SDD Orchestrator requirements call for different behavior. SDD Orchestrator will focus specifically on specifications, approved slices, verification gates, and decision write-back.

The first application boundary is selected in `specs/01-github-project-onboarding/`: an Elixir/Phoenix control plane with LiveView and PostgreSQL. Slice 01 does not import or fork the experimental Symphony prototype. Later agent-delivery specifications will define whether the orchestration boundary reuses or reimplements Symphony behavior behind durable control-plane commands and events.

## Additional Inspiration

[Hermes Agent](https://github.com/NousResearch/hermes-agent) is a reference for clear provider authentication and model configuration across API-key, OAuth, OpenAI-compatible, and local providers.

Hermes Agent is a product and user-experience reference, not an implementation specification.

## SDD Workflow

The initial workflow is built around three operations:

- `add-spec`: create a specification without implementing it.
- `update-spec`: change the agreement before changing implementation.
- `implement-spec`: implement and verify one approved slice.

The project expects to use `add-spec` frequently as Symphony capabilities are introduced as bounded SDD Orchestrator features. It expects to use `update-spec` whenever product discovery, implementation evidence, or an intentional departure from Symphony changes the agreement. Neither workflow continues into implementation; `implement-spec` handles an approved slice separately.

The project will adapt these workflows as its real product and operational requirements become clearer. Choosing Symphony as a foundation does not bypass the specification and approval process.

## Agent Compatibility

The canonical project skills live under `.agents/skills/` and follow the Agent Skills `SKILL.md` format.

- Codex discovers the canonical skills directly.
- Claude Code uses the same directories through `.claude/skills/` links.
- `AGENTS.md` and `CLAUDE.md` contain the same project contract.

## Current State

- Git repository initialized on `main` with the initial project bootstrap committed locally.
- Shared Codex and Claude Code instructions added.
- `add-spec`, `update-spec`, and `implement-spec` installed as shared Codex and Claude skills; `update-spec` now includes progress-log discipline learned from this project's specification work.
- OpenAI Symphony selected as the orchestration foundation; no reference code has been imported. Slice 01 selects Elixir/Phoenix, LiveView, and PostgreSQL for the product control plane.
- Project onboarding is organized as six ordered specifications under `specs/`: GitHub onboarding, local onboarding, hosted passwordless access, GitHub identity linking, project storage lifecycle, and project portability. All remain draft and blocked by their recorded outstanding decisions; Slice 01 now has a technical design and one remaining privacy-approval blocker.
- No dashboard, service, worker runtime, provider integration, or application toolchain implemented yet.

## Documentation Boundaries

- `README.md` describes the project identity and current direction.
- `AGENTS.md` and `CLAUDE.md` define how coding agents work in this repository.
- Files under `specs/` define product behavior, design decisions, implementation slices, verification, and their current approval status.
- Files under `design-references/` preserve exported visual prototypes for comparison; they are not application source or a substitute for the specifications.
- Writing and case-study notes provide book and article evidence but are not the product source of truth.

## Open Product Questions

The detailed discussion still needs to define:

- The unresolved product questions recorded across the ordered project specifications.
- The feature-specific boundary for reusing or reimplementing Symphony behavior behind the selected Phoenix control plane.
- The V1 protocol and trust boundary between the control plane and local or remote workers.
- Repository discovery and connection behavior.
- Local and remote worker communication and isolation.
- User authentication and provider credential handling.
- API-key, Codex OAuth, and other provider setup paths.
- Model and agent selection rules.
- Whether Raspberry Pi support belongs in V1 or a later deployment profile.
