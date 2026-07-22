# Local Project Onboarding

## Status

Draft

## Outcome

A user can choose `Work without GitHub`, connect a Git repository on their computer through a paired local worker, and create a project without requiring a GitHub account or uploading repository source.

## Users

- BA, PO, and PM users working with a repository available on their computer.
- Developers and technical contributors using local or non-GitHub repositories.

## Primary Workflow

1. The user selects `Work without GitHub` from the shared entry surface.
2. The product explains the available project-data storage modes defined by `specs/05-project-storage-lifecycle/`.
3. The product detects whether a local worker is paired to the current personal or device workspace.
4. If no worker is available, the product guides the user through installation and secure pairing.
5. The paired worker lets the user select a local path and validates that it is a Git repository.
6. The worker returns only the approved repository identity and connection metadata.
7. The product applies the shared repository-uniqueness and project-naming rules.
8. The project and local repository connection are created atomically and shown without starting an agent.

## In Scope

- The `Work without GitHub` entry action.
- Accountless on-device project onboarding.
- Local worker discovery, installation guidance, pairing, revocation, and reconnect states needed for onboarding.
- Local Git repository selection and validation.
- Minimum repository identity and connection metadata exchange.
- Project creation using the shared naming and repository-uniqueness rules.
- Persistent project visibility when the worker or repository becomes unavailable.
- Integration boundaries for hosted passwordless access and project storage selection.
- Actionable failure states for non-technical users.

## Out of Scope

- GitHub repository onboarding, defined in `specs/01-github-project-onboarding/`.
- Passwordless hosted identity internals, defined in `specs/03-hosted-passwordless-access/`.
- Identity merging, defined in `specs/04-github-identity-linking/`.
- Storage migration and retention internals, defined in `specs/05-project-storage-lifecycle/`.
- Project export and import, defined in `specs/06-project-portability/`.
- Remote workers hosted in the cloud or on devices such as a Raspberry Pi.
- Agent installation, model-provider setup, or deciding where an AI agent executes.
- Uploading, browsing, editing, or executing repository source from the control plane during onboarding.
- Additional isolation between people sharing the same operating-system user profile and filesystem permissions.

## Business Rules

- Selecting `Work without GitHub` means the repository is local to the user's computer; it does not require the AI agent to run locally.
- A GitHub account is not required for the local path.
- Accountless on-device projects are owned by the current operating-system user and filesystem permission boundary.
- SDD Orchestrator does not add a second local multi-user isolation layer inside that boundary.
- A local worker must be explicitly paired to the current personal or device workspace before it can register a repository.
- Pairing credentials must be attempt-bound, replaceable, revocable, and protected from client payloads, logs, analytics, and project data.
- A worker paired to one workspace cannot register or operate on a project owned by another workspace.
- A selected path must be validated as a Git repository before project creation.
- Local source files remain on the user's computer and must not be persisted by the control plane during onboarding.
- The control plane may receive only the approved metadata needed to establish canonical repository identity and connection state.
- Linking must not modify repository files, branches, remotes, hooks, or Git configuration.
- Local projects use the same workspace-scoped, case-insensitive naming and one-project-per-repository rules as GitHub projects.
- A worker or repository becoming unavailable changes connection state without deleting or hiding the project.
- Authentication later may combine on-device and authorized hosted projects in one catalog, but must not upload, reassign, duplicate, or change the storage mode of on-device projects.
- Every project in a combined catalog must show its storage mode and current device availability.
- Signing out removes hosted access but leaves on-device projects available through `Work without GitHub`.
- Personal metadata that leaves the device requires an approved GDPR purpose, lawful basis, minimum fields, access boundary, retention, deletion, rights behavior, processors, transfers, and review.

## Acceptance Criteria

- Given a user selects `Work without GitHub`, when onboarding starts, then no GitHub authentication is requested.
- Given no worker is paired, when the local path continues, then the user receives actionable installation and pairing guidance rather than a terminal-only dead end.
- Given a valid pairing attempt, when pairing succeeds, then the worker is bound only to the current workspace with protected replaceable credentials.
- Given a path is not a Git repository, when validation runs, then project creation is blocked and no source content is uploaded.
- Given a valid local Git repository, when the user confirms it, then the worker returns only approved identity and connection metadata.
- Given an unlinked local repository and an available project name, when creation succeeds, then one project and one repository connection are created atomically.
- Given the same canonical local repository is already linked in the workspace, when creation is attempted again, then it is blocked without creating a duplicate.
- Given linking completes, when local repository state is inspected, then files, branches, remotes, hooks, and Git configuration are unchanged.
- Given the worker later becomes unavailable, when the catalog is shown, then the project remains visible with an unavailable or authorization-required connection state.
- Given an accountless device user later authenticates, when the combined catalog is shown, then on-device projects remain local and identify their storage and availability state.
- Given the authenticated user signs out, when `Work without GitHub` is opened under the same operating-system boundary, then on-device projects remain available.
- Given pairing or repository validation fails, when the operation ends, then no partial project, connection, credential, or source upload remains.

## Open Questions

- How is the local worker packaged, installed, updated, paired, revoked, and reconnected on supported operating systems?
- Which transport reaches a local worker without requiring inbound public network access to the user's computer?
- What canonical identity prevents duplicate local links when paths, worktrees, or remotes change?
- What exact repository and device metadata may leave the computer, and how is consent or notice presented?
- How are accountless device-workspace records persisted and recovered without an account?
- How does local onboarding integrate with hosted passwordless access when the user selects hosted storage?
- How are local and hosted catalog entries deduplicated without implicitly linking or uploading them?
- Which architecture, security, privacy, and verification choices block the first local-worker slice?
