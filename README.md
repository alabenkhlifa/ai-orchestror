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

This direction is not an approved V1 specification. Product discovery is still in progress.

## Implementation Foundation

[OpenAI Symphony](https://github.com/openai/symphony) is the implementation foundation for SDD Orchestrator. Its language-independent specification and Elixir reference implementation provide a starting point for isolated workspaces, coding-agent execution, work reconciliation, retries, and operational visibility.

Symphony is a foundation, not a fixed architecture or product boundary. The project may reuse, extend, replace, or reimplement any part when approved SDD Orchestrator requirements call for different behavior. SDD Orchestrator will focus specifically on specifications, approved slices, verification gates, and decision write-back.

The implementation language and the decision to fork, extend, or reimplement the Symphony reference remain open until they are resolved through the SDD workflow.

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
- `add-spec`, `update-spec`, and `implement-spec` copied from the starter kit without project-specific adaptation.
- OpenAI Symphony selected as the implementation foundation; no reference code has been imported and no implementation language has been selected yet.
- The first draft specification covers GitHub login and linking GitHub or local repositories under `specs/01-project-onboarding/`; implementation is blocked pending specification review and technology decisions.
- No dashboard, service, worker runtime, provider integration, or application toolchain implemented yet.

## Documentation Boundaries

- `README.md` describes the project identity and current direction.
- `AGENTS.md` and `CLAUDE.md` define how coding agents work in this repository.
- Files under `specs/` define product behavior, design decisions, implementation slices, verification, and their current approval status.
- Writing and case-study notes provide book and article evidence but are not the product source of truth.

## Open Product Questions

The detailed discussion still needs to define:

- The unresolved product questions recorded in the project-onboarding specification.
- Whether to fork or extend Symphony's Elixir reference implementation or implement its specification in another runtime.
- The V1 boundary between the dashboard, control service, and workers.
- Repository discovery and connection behavior.
- Local and remote worker communication and isolation.
- User authentication and provider credential handling.
- API-key, Codex OAuth, and other provider setup paths.
- Model and agent selection rules.
- Whether Raspberry Pi support belongs in V1 or a later deployment profile.
