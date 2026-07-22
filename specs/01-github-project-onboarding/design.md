# GitHub Project Onboarding Design

## Context

SDD Orchestrator has no application runtime yet. OpenAI Symphony is the orchestration foundation, but the implementation language and the boundary between Symphony and the dashboard remain undecided.

This specification owns only the first GitHub-backed project-registration path. Local repositories, passwordless access, identity linking, storage lifecycle, and portability have separate specifications.

## Proposed Approach

1. Present the shared two-action entry surface.
2. Authenticate the GitHub user and establish a protected application session.
3. Create or restore one personal workspace for the stable GitHub identity.
4. Retrieve every repository available under the granted GitHub access and expose searchable loading, empty, and failure states.
5. Accept one explicit repository selection.
6. derive and validate the project display name under workspace-scoped rules.
7. Create the project and canonical repository connection in one transaction.
8. Show the resulting project and connection state without modifying the repository or starting an agent.

Exact protocols and storage schemas remain deferred until the technology update.

## Components Affected

- Entry, GitHub sign-in, session restoration, and sign-out surfaces.
- GitHub identity and authorization integration.
- Personal workspace boundary.
- Repository catalog and search.
- Project registration and naming.
- Repository connection and status presentation.
- Credential storage, audit, diagnostics, and privacy controls.
- Automated and browser verification for the end-to-end path.

## Data and Access Boundaries

The logical domain requires:

- `UserContext`: the stable authenticated GitHub user identity.
- `PersonalWorkspace`: the ownership boundary for projects and repository connections.
- `Project`: the stable SDD Orchestrator project identity and editable display name.
- `RepositoryConnection`: the provider-stable repository identity, display metadata, source type, and connection status.
- `DataProcessingRecord`: the approved purpose, lawful basis, data categories, access, retention, deletion, rights behavior, processors, transfers, and required review for each processing activity.

Required boundaries:

- Every project and repository connection belongs to one personal workspace.
- Project names are unique by case-insensitive comparison only inside that workspace.
- Repository connection identity is unique inside that workspace and independent from its mutable display metadata or remote URL.
- Project identity is independent from its display name and repository display metadata.
- GitHub credentials and application sessions remain in a protected server-side or equivalent credential boundary.
- The browser receives only the repository metadata needed for user selection and status display.
- Repository content is outside the onboarding write boundary.
- Lost provider access changes connection state without deleting project state.
- Every personal-data field and processing path must have an approved GDPR data contract before implementation.

## Interfaces

- Entry interface: expose both product paths without conflating repository location with later agent execution location.
- GitHub identity interface: authenticate a stable provider identity using the minimum approved permissions.
- Session interface: establish, restore, expire, revoke, and end authenticated access.
- Repository catalog interface: paginate and search every repository returned under granted access and return stable identity plus display metadata.
- Project registration interface: enforce repository uniqueness, allocate a workspace-scoped name, and create the project and connection atomically.
- Project naming interface: validate case-insensitive uniqueness and rename without changing stable identities.
- Connection-status interface: distinguish connected and disconnected provider state without exposing secrets.
- Privacy-governance interface: block schema and backend approval until each processing activity has its required data contract and review.

## Decisions and Tradeoffs

### Two Entry Actions

- Choice: Present `Login with GitHub` and `Work without GitHub` as distinct primary actions.
- Reason: Repository location and GitHub account ownership are separate user choices.
- Consequence: Release sequencing must not expose an action whose complete path is unavailable; the local path is defined separately.

### Complete GitHub Repository Catalog

- Choice: Show every repository returned under the user's granted access and link only the confirmed selection.
- Reason: Non-technical users should not need repository URLs or terminal commands.
- Consequence: Authorization scope, pagination, rate limits, organization policy, and large-catalog usability require explicit design.

### One Project Per Repository

- Choice: Enforce one repository per project and one project per canonical repository inside a personal workspace.
- Reason: Later specifications, runs, workers, and evidence need one unambiguous repository boundary.
- Consequence: Monorepo subprojects and multiple SDD configurations for one repository are deferred.

### Editable Workspace-Scoped Names

- Choice: Default the project name from the repository, allocate the lowest available numeric suffix case-insensitively, and allow later edits.
- Reason: The default minimizes setup while workspace scope permits independent users to organize the same repository differently.
- Consequence: Persistence must enforce concurrency-safe uniqueness while stable identities remain separate from the display name.

### Disconnected Rather Than Deleted

- Choice: Keep a project visible when GitHub access is lost.
- Reason: Authorization and provider availability are recoverable connection states, not project existence.
- Consequence: Access must be revalidated and stale credentials must not be used or exposed.

### Technology-Neutral First Specification

- Choice: Keep the product and security contracts independent from a selected stack.
- Reason: No runtime or Symphony integration strategy has been approved.
- Consequence: Implementation remains blocked until architecture and canonical verification commands are recorded through `update-spec`.

## Risks

- Broad GitHub permissions could exceed the feature's needs. Select the minimum model that still supports complete authorized discovery and disclose its scope.
- Repository identity based on names or URLs can break after renames or transfers. Use a provider-stable canonical identifier.
- Concurrent creation or rename can allocate duplicate names. Enforce uniqueness at the persistence boundary and retry suffix allocation.
- GitHub outages, rate limits, SSO, and organization policy can interrupt onboarding. Preserve consistent state and expose actionable recovery.
- Credentials can leak through browser payloads, logs, analytics, or diagnostics. Keep them in the accepted credential boundary and test every failure surface.
- A non-technical user may confuse GitHub authentication with agent-provider authentication. Keep those concepts and statuses separate.
- Personal data can escape its lifecycle through logs, backups, analytics, or processors. Include every copy and transfer in the approved data contract.
- Implementing the GitHub path before the local path may expose an unusable primary action. Coordinate release boundaries with the local onboarding specification.

## Open Questions

- Which GitHub App, OAuth, or other integration model satisfies identity, repository discovery, permission, revocation, and organization-access requirements?
- How are GitHub and application sessions protected, refreshed, revoked, and isolated from coding agents?
- Which stable repository identifier and transfer rules enforce uniqueness?
- Which storage-selection contract from `specs/05-project-storage-lifecycle/` is required before project creation commits?
- How are the two entry paths sequenced without a non-functional action?
- Which GDPR processing contracts and reviews apply to identity, repository metadata, projects, logs, support, security, and analytics?
- Which runtime, persistence, UI, deployment, and Symphony boundary should be selected?
- Which automated, integration, security, and browser commands form the verification gate?
