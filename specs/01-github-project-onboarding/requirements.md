# GitHub Project Onboarding

## Status

Draft

## Outcome

A BA, PO, PM, developer, or other project contributor can sign in with GitHub, find any repository available through their granted access, and create one SDD Orchestrator project linked to that repository without modifying it or starting an AI agent.

## Users

- Business analysts, product owners, and product managers organizing specification work.
- Developers and technical contributors linking repositories to the SDD workflow.

## Primary Workflow

1. The entry surface presents `Login with GitHub` and `Work without GitHub` as distinct primary actions.
2. The user selects `Login with GitHub` and completes GitHub authentication.
3. SDD Orchestrator creates or restores the user's personal workspace and protected session.
4. The repository picker loads every repository returned under the user's granted GitHub access and supports search.
5. The user selects and confirms one repository.
6. The product derives the default project name from the repository name, allocates the lowest available numeric suffix when needed, and allows the user to edit the name.
7. The project and repository connection are created atomically under the personal workspace.
8. The product shows the project, repository source, and connection status without changing repository content or starting an agent.

## In Scope

- The GitHub action on the two-action entry surface.
- GitHub authentication, session restoration, and sign-out.
- Personal workspace creation and restoration.
- Retrieval, search, loading, empty, and failure states for every repository returned by GitHub under the granted access.
- Explicit selection of one GitHub repository.
- Atomic project and repository-connection creation.
- One repository per project and one project per repository within a personal workspace.
- Repository-derived default names, case-insensitive workspace uniqueness, lowest-available numeric suffixes, and editing during or after onboarding.
- Persistent project visibility with a disconnected status when GitHub access is lost.
- Actionable errors for non-technical users.
- GDPR data contracts and security controls for identity, session, repository, project, log, and analytics data introduced by this feature.

## Out of Scope

- The `Work without GitHub` workflow and local worker behavior, defined in `specs/02-local-project-onboarding/`.
- Passwordless hosted access, defined in `specs/03-hosted-passwordless-access/`.
- Automatic identity merging, conflict recovery, unlinking, and re-linking, defined in `specs/04-github-identity-linking/`.
- Project storage migration, retention, resynchronization, and analytics lifecycle, defined in `specs/05-project-storage-lifecycle/`.
- Project export and import, defined in `specs/06-project-portability/`.
- Collaboration workflows, AI-provider setup, specification workflows, and agent execution.
- Linking multiple repositories to one project or creating multiple projects for the same repository in one personal workspace.
- Selecting the application language, framework, database, deployment model, or Symphony integration strategy.

## Business Rules

- The entry surface must show exactly two primary actions: `Login with GitHub` and `Work without GitHub`.
- A primary action must not be exposed as functional before its complete path can be used.
- GitHub sign-in must restore one stable personal workspace for the authenticated GitHub identity.
- The repository picker must show every repository returned by GitHub under the user's granted access; visibility must not link a repository automatically.
- A project is created only after the user explicitly selects and confirms a repository.
- A project must be linked to exactly one repository.
- A repository can be linked to at most one project in the same personal workspace.
- Different users may link the same repository independently in their separate personal workspaces.
- The default project name is the repository name.
- Project names are unique by case-insensitive comparison within one personal workspace, not globally.
- When the default name is occupied, the product appends the lowest available positive integer suffix: `-1`, then `-2`, and so on.
- A user may edit a project name during onboarding and at any later time; every saved name follows the same uniqueness rule.
- Project identity and repository identity remain stable when the display name changes.
- Repository uniqueness and project-name uniqueness are independent rules; renaming cannot allow a duplicate repository link.
- Project creation and repository linking must commit atomically or leave no partial project or connection.
- Linking must not modify repository files, branches, settings, issues, or pull requests.
- When GitHub access is lost, the project remains visible and its connection becomes disconnected.
- Authentication credentials, repository credentials, and session secrets must never be displayed after acceptance or exposed in client payloads, logs, analytics, or project data.
- Personal data introduced by this feature requires an approved purpose, lawful basis, access boundary, retention, deletion, rights behavior, processor boundary, transfer assessment, and required privacy review before implementation.
- Retained analytics must be aggregate and genuinely anonymous; pseudonymous or linkable identifiers remain personal data.

## Acceptance Criteria

- Given the entry surface loads, when the user views it, then `Login with GitHub` and `Work without GitHub` are distinct primary actions.
- Given GitHub authentication succeeds, when onboarding continues, then the user's stable personal workspace is created or restored without exposing credentials.
- Given GitHub returns accessible personal, private, or organization repositories, when the picker loads, then every returned repository is available and searchable without requiring a URL.
- Given repository retrieval is empty or fails, when the request ends, then the user sees an actionable state and no partial project is created.
- Given an unlinked repository is confirmed, when creation succeeds, then exactly one project and one repository connection are created atomically.
- Given a repository named `example` and no conflicting project name, when it is linked, then the default project name is `example`.
- Given projects named `example` and `Example-1`, when another repository named `example` is linked, then the lowest available default is `example-2`.
- Given two separate personal workspaces, when each user links the same repository or uses the same project name, then each workspace enforces uniqueness independently.
- Given a project already links the selected repository, when the same workspace tries to link it again, then creation is blocked and the existing project is identified.
- Given the user edits a project name, when the name is saved, then case-insensitive uniqueness is enforced without changing project or repository identity.
- Given repository access is lost, when the project is shown, then it remains visible with a disconnected status and no stale credential is exposed.
- Given repository access later returns, when the connection is revalidated, then the same project can return to connected.
- Given onboarding completes, when repository state is inspected, then repository content and settings are unchanged and no AI agent has started.
- Given any onboarding operation fails, when it ends, then no duplicate workspace, project, or repository connection exists.

## Open Questions

- Which GitHub integration model provides sign-in, complete repository discovery, acceptable permission scope, and secure long-lived access?
- How are sessions and GitHub credentials stored, refreshed, revoked, and separated from coding-agent processes?
- What canonical identity prevents duplicate GitHub repository links across renames, transfers, and remote URL changes?
- Which project-data storage choice must be available before final project creation, and how does this slice integrate with `specs/05-project-storage-lifecycle/`?
- Can the GitHub path ship before the local path without exposing a non-functional `Work without GitHub` action?
- Which controller and processor roles, purposes, lawful bases, retention periods, rights workflows, subprocessors, transfers, and privacy reviews apply to this slice?
- Which anonymous aggregate metrics are necessary for GitHub onboarding, what aggregation thresholds prevent singling out, and how long is each retained?
- Which application runtime, UI approach, persistence system, deployment model, and Symphony integration satisfy this slice?
- Which canonical build, formatting, lint, static-check, automated-test, integration-test, and browser-test commands prove this slice?
