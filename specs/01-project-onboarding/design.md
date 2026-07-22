# Project Onboarding Design

## Context

The repository has no application toolchain or implementation architecture yet. Product behavior must be specified before selecting technologies.

OpenAI Symphony is the orchestration foundation, but its specification treats a rich web UI and multi-tenant control plane as non-goals. Project onboarding is therefore an SDD Orchestrator capability that sits before Symphony-derived scheduling, workspace management, and agent execution.

This design defines logical responsibilities and security boundaries only. It does not select an implementation language, framework, database, hosting platform, authentication library, or worker transport.

## Proposed Approach

Use an entry page with two explicit paths:

1. Show `Login with GitHub` and `Work without GitHub` as the two primary actions.
2. For `Login with GitHub`, authenticate the user, establish their personal workspace, load every repository available under the granted GitHub access, and let the user select one.
3. For `Work without GitHub`, enter the local repository path without GitHub authentication and establish the personal workspace through the local identity boundary that remains to be approved.
4. Detect whether the local path has an available paired worker.
5. If no local worker is available, guide the user through installation and secure pairing.
6. Ask the paired worker to validate and identify the local repository selected by the user without uploading its contents.
7. Validate the one-project-per-repository rule.
8. Derive the project name from the repository name, allocate the lowest available suffix using case-insensitive comparison, and allow the user to edit the name.
9. Create the project and repository connection as one operation, including the final workspace-scoped project name.
10. Show the project with its repository source and connection status. Keep it visible as disconnected if later access is lost, and do not start specification or agent work automatically.

The current candidate implementation slice delivers the GitHub path end to end. The two-action entry decision now requires an explicit slice-boundary decision: either the local path ships in the same slice, or the entry surface and local path are delivered together in the next slice so the product does not expose a non-functional primary action.

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

- `UserContext`: the ownership identity for a personal workspace, backed by GitHub for the GitHub path and by an approved local identity boundary for the no-GitHub path.
- `PersonalWorkspace`: the ownership boundary for projects, workers, and repository links.
- `Project`: the SDD Orchestrator project created for one repository.
- `RepositoryConnection`: the canonical identity, source type, display metadata, and connection status for one GitHub or local repository.
- `LocalWorker`: a user-owned execution endpoint that can validate and later operate on local repositories.

Required boundaries:

- Every project belongs to one personal workspace.
- A project display name is unique within its personal workspace using case-insensitive comparison, not globally across users.
- Project identity is stable and independent from its editable display name.
- Every repository connection belongs to one personal workspace and one project.
- The repository connection identity must be unique within its personal workspace.
- GitHub authorization and session secrets must remain server-side or in an equivalent protected credential boundary and must not be returned to the browser after acceptance.
- Worker pairing credentials must be short-lived or replaceable and bound to the current personal workspace and pairing attempt.
- A local worker may return repository identity and connection metadata, but local source content must not be persisted by the control plane during onboarding.
- Repository access must be revalidated when the provider or worker reports that access is no longer available.
- Lost repository access changes connection state without deleting or hiding the project.

## Interfaces

- Entry-choice interface: present the GitHub and local-repository paths without conflating repository location with later agent execution location.
- GitHub identity interface: authenticate the user and return stable identity information.
- Local identity interface: establish and restore the workspace ownership boundary for a user who proceeds without GitHub; the mechanism remains an open decision.
- GitHub repository catalog interface: list every repository available under the granted account access and return a stable repository identity plus display metadata.
- Session interface: establish, restore, expire, and end authenticated access.
- Project registration interface: validate repository uniqueness, allocate a user-scoped project name, and create the project and repository link atomically.
- Project naming interface: validate case-insensitive uniqueness and rename a project without changing its stable identity or repository connection.
- Worker pairing interface: establish trust between the personal workspace and a local worker without requiring the user to edit configuration or manually manage a long-lived secret.
- Local repository interface: validate a user-selected path as a Git repository and return only the metadata needed to identify it and report availability.
- Connection-status interface: distinguish connected, unavailable, authorization-required, and invalid states without exposing secrets or local source content.

Exact protocols and schemas remain part of the technology-selection update.

## Decisions and Tradeoffs

### Two Entry Paths

- Choice: Present `Login with GitHub` and `Work without GitHub` as the two primary entry actions.
- Reason: A user with a repository on their computer must be able to use the product without creating or connecting a GitHub account.
- Consequence: The product needs a non-GitHub identity and persistence boundary for local workspaces, and the implementation slices must not expose a primary action before its path works.

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

### Editable User-Scoped Project Names

- Choice: Default the project name to the repository name, allow it to be edited at any time, and keep names unique by case-insensitive comparison only within the owning personal workspace.
- Reason: The default requires no naming decision from a non-technical user, while user-scoped uniqueness allows different users to link the same repository independently.
- Consequence: Default-name allocation and every rename must enforce the same uniqueness boundary, while stable project identity and repository identity cannot depend on the mutable display name.

### Local Source Stays Local

- Choice: Link local repositories through a paired local worker and do not upload repository content during onboarding.
- Reason: It protects local source and supports repositories that are not hosted on GitHub.
- Consequence: Local onboarding depends on installing, pairing, and monitoring another component.

### Repository Access Loss

- Choice: Keep a project visible with a disconnected status when its linked GitHub repository becomes inaccessible.
- Reason: Temporary authorization or provider changes must not erase the user's project context.
- Consequence: Repository access is a recoverable connection state, not a condition for project existence.

### Technology-Neutral Specification

- Choice: Describe logical responsibilities and contracts before choosing technologies.
- Reason: No technology preference has been selected, so product and security behavior should determine the stack and the amount of Symphony implementation that can be reused.
- Consequence: Implementation remains blocked until the runtime, persistence, authentication, and worker communication decisions are recorded through `update-spec`.

## Risks

- Listing all accessible GitHub repositories can require broad authorization. Reduce this by making the requested access clear, protecting credentials, and documenting provider limitations before approval.
- A non-technical user may confuse GitHub authentication, local repository location, local worker pairing, agent execution location, and later AI-provider authentication. Keep them as separate concepts with distinct status and recovery messages.
- A compromised pairing flow could grant access to a user's machine. Bind pairing to the current personal workspace, expire incomplete attempts, and make paired workers visible and revocable.
- Local paths can reveal sensitive machine information. Define the minimum metadata sent to the control plane and avoid displaying full paths unless required by the user.
- Repository renames, transfers, changed Git remotes, and lost permissions can defeat naive duplicate detection. Define canonical hosted and local repository identities before implementation.
- Concurrent project creation can allocate the same project name or numeric suffix. Enforce user-scoped name uniqueness at the persistence boundary and retry suffix allocation after a conflict.
- GitHub outages, rate limits, organization policies, or SSO requirements can make an accessible repository temporarily unavailable. Preserve consistent project state and show a recoverable connection status.
- Selecting a framework before these boundaries are resolved could make the Symphony foundation or local-worker model harder to adopt. Keep technology selection as an explicit approval gate.

## Open Questions

- Which GitHub integration model provides sign-in, complete repository discovery, acceptable permission scope, and secure long-lived access?
- What identity, persistence, recovery, and access boundary establishes a personal workspace for `Work without GitHub`?
- If a local workspace later connects to GitHub, is it attached, merged, or kept separate?
- Must the GitHub and local entry paths ship in one executable slice, or may the complete local entry surface be delivered in the immediately following slice?
- How are sessions and GitHub credentials stored, refreshed, revoked, and separated from coding-agent processes?
- Which application runtime, UI approach, persistence system, and deployment model satisfy the first slice?
- Will the project extend Symphony's Elixir implementation, run it as a separate orchestration service, or implement its specification in another runtime?
- How is the local worker packaged, installed, updated, paired, revoked, and reconnected?
- Which transport lets the control plane reach a local worker without requiring inbound network access to the user's computer?
- What canonical identity prevents duplicate links for GitHub repositories and for local repositories whose paths or remotes change?
- What is the minimum local repository metadata that may leave the user's computer?
