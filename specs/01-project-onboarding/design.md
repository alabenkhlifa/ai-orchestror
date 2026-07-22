# Project Onboarding Design

## Context

The repository has no application toolchain or implementation architecture yet. Product behavior must be specified before selecting technologies.

OpenAI Symphony is the orchestration foundation, but its specification treats a rich web UI and multi-tenant control plane as non-goals. Project onboarding is therefore an SDD Orchestrator capability that sits before Symphony-derived scheduling, workspace management, and agent execution.

This design defines logical responsibilities and security boundaries only. It does not select an implementation language, framework, database, hosting platform, authentication library, or worker transport.

## Proposed Approach

Use one guided onboarding flow with two repository-source paths:

1. Authenticate the user with GitHub and establish their personal workspace.
2. Ask the user whether the project repository is on GitHub or on their current computer.
3. For GitHub, load all repositories available under the granted GitHub access and let the user select one.
4. For a local repository, detect whether the user has an available paired worker.
5. If no local worker is available, guide the user through installation and secure pairing.
6. Ask the paired worker to validate and identify the local repository selected by the user without uploading its contents.
7. Validate the one-project-per-repository rule.
8. Derive the project name from the repository name and allocate the lowest available numeric suffix within the personal workspace when needed.
9. Create the project and repository connection as one operation, including the final user-scoped project name.
10. Show the project with its repository source and connection status. Do not start specification or agent work automatically.

The first executable implementation slice should deliver the GitHub path end to end. Local worker onboarding and local repository linking remain requirements of this feature but should be implemented as a later slice after the GitHub path proves the account, workspace, project, and repository-identity model.

## Components Affected

- Sign-in and session surface.
- User identity and personal workspace boundary.
- GitHub repository catalog integration.
- Project registration and repository uniqueness rules.
- Repository source picker and onboarding status UI.
- Local worker installation and pairing flow.
- Local repository validation and connection-status reporting.
- Credential, session, and pairing-secret handling.
- Audit and diagnostic events for onboarding failures.

## Data and Access Boundaries

The logical domain needs these records regardless of the eventual persistence technology:

- `User`: the GitHub-backed identity allowed to enter the product.
- `PersonalWorkspace`: the ownership boundary for projects, workers, and repository links.
- `Project`: the SDD Orchestrator project created for one repository.
- `RepositoryConnection`: the canonical identity, source type, display metadata, and connection status for one GitHub or local repository.
- `LocalWorker`: a user-owned execution endpoint that can validate and later operate on local repositories.

Required boundaries:

- Every project belongs to one personal workspace.
- A project display name is unique within its personal workspace, not globally across users.
- Every repository connection belongs to one personal workspace and one project.
- The repository connection identity must be unique within its personal workspace.
- GitHub authorization and session secrets must remain server-side or in an equivalent protected credential boundary and must not be returned to the browser after acceptance.
- Worker pairing credentials must be short-lived or replaceable and bound to the authenticated user and pairing attempt.
- A local worker may return repository identity and connection metadata, but local source content must not be persisted by the control plane during onboarding.
- Repository access must be revalidated when the provider or worker reports that access is no longer available.

## Interfaces

- GitHub identity interface: authenticate the user and return stable identity information.
- GitHub repository catalog interface: list every repository available under the granted account access and return a stable repository identity plus display metadata.
- Session interface: establish, restore, expire, and end authenticated access.
- Project registration interface: validate repository uniqueness, allocate a user-scoped project name, and create the project and repository link atomically.
- Worker pairing interface: establish trust between the personal workspace and a local worker without requiring the user to edit configuration or manually manage a long-lived secret.
- Local repository interface: validate a user-selected path as a Git repository and return only the metadata needed to identify it and report availability.
- Connection-status interface: distinguish connected, unavailable, authorization-required, and invalid states without exposing secrets or local source content.

Exact protocols and schemas remain part of the technology-selection update.

## Decisions and Tradeoffs

### GitHub-Only Sign-In

- Choice: Use GitHub as the only sign-in provider for the first version.
- Reason: Every first-version project is Git-based, and GitHub identity provides a direct path to hosted repository discovery.
- Consequence: Users without a GitHub account cannot use the first version, including users who only need a local repository.

### Personal Workspaces First

- Choice: Give each user one personal workspace and defer collaboration.
- Reason: It avoids introducing invitations, memberships, roles, and shared credential ownership before the core workflow is proven.
- Consequence: A BA, PO, PM, and developer cannot yet collaborate inside one shared SDD Orchestrator workspace.

### Visible GitHub Catalog

- Choice: Show every repository returned under the user's granted GitHub access, then link only the repository the user confirms.
- Reason: Users should not need to know or paste repository URLs.
- Consequence: The GitHub authorization must support repository discovery, and the UI must remain usable for accounts with many repositories.

### One Project Per Repository

- Choice: Enforce one repository per project and one project per repository within a personal workspace.
- Reason: It gives later specifications, runs, workers, and verification evidence one unambiguous repository boundary.
- Consequence: Monorepo subprojects and multiple SDD configurations for one repository are deferred.

### User-Scoped Project Names

- Choice: Default the project name to the repository name and keep names unique only within the owning personal workspace.
- Reason: The default requires no naming decision from a non-technical user, while user-scoped uniqueness allows different users to link the same repository independently.
- Consequence: When the base name is already used, project creation must atomically allocate the lowest available suffix, starting with `-1`, without weakening repository-identity uniqueness.

### Local Source Stays Local

- Choice: Link local repositories through a paired local worker and do not upload repository content during onboarding.
- Reason: It protects local source, supports offline ownership, and matches the project's local-agent direction.
- Consequence: Local onboarding depends on installing, pairing, and monitoring another component.

### Technology-Neutral Specification

- Choice: Describe logical responsibilities and contracts before choosing technologies.
- Reason: Product and security behavior should determine the stack and the amount of Symphony implementation that can be reused.
- Consequence: Implementation remains blocked until the runtime, persistence, authentication, and worker communication decisions are recorded through `update-spec`.

## Risks

- Listing all accessible GitHub repositories can require broad authorization. Reduce this by making the requested access clear, protecting credentials, and documenting provider limitations before approval.
- A non-technical user may confuse GitHub authentication, repository access, local worker pairing, and later AI-provider authentication. Keep them as separate steps with distinct status and recovery messages.
- A compromised pairing flow could grant access to a user's machine. Bind pairing to the authenticated user, expire incomplete attempts, and make paired workers visible and revocable.
- Local paths can reveal sensitive machine information. Define the minimum metadata sent to the control plane and avoid displaying full paths unless required by the user.
- Repository renames, transfers, changed Git remotes, and lost permissions can defeat naive duplicate detection. Define canonical hosted and local repository identities before implementation.
- Concurrent project creation can allocate the same project name or numeric suffix. Enforce user-scoped name uniqueness at the persistence boundary and retry suffix allocation after a conflict.
- GitHub outages, rate limits, organization policies, or SSO requirements can make an accessible repository temporarily unavailable. Preserve consistent project state and show a recoverable connection status.
- Selecting a framework before these boundaries are resolved could make the Symphony foundation or local-worker model harder to adopt. Keep technology selection as an explicit approval gate.

## Open Questions

- Which GitHub integration model provides sign-in, complete repository discovery, acceptable permission scope, and secure long-lived access?
- How are sessions and GitHub credentials stored, refreshed, revoked, and separated from coding-agent processes?
- Which application runtime, UI approach, persistence system, and deployment model satisfy the first slice?
- Will the project extend Symphony's Elixir implementation, run it as a separate orchestration service, or implement its specification in another runtime?
- How is the local worker packaged, installed, updated, paired, revoked, and reconnected?
- Which transport lets the control plane reach a local worker without requiring inbound network access to the user's computer?
- What canonical identity prevents duplicate links for GitHub repositories and for local repositories whose paths or remotes change?
- How will project-name comparison handle letter case, and when can a user rename a generated project name?
- What is the minimum local repository metadata that may leave the user's computer?
