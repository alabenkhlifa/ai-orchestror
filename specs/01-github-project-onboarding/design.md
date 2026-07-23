# GitHub Project Onboarding Design

## Context

SDD Orchestrator has no application runtime yet. OpenAI Symphony is the orchestration foundation, but the implementation language and the boundary between Symphony and the dashboard remain undecided.

This specification owns only the first GitHub-backed project-registration path. Local repositories, passwordless access, identity linking, storage lifecycle, and portability have separate specifications.

## Proposed Approach

1. Resolve the current protected session before rendering the shared entry surface.
2. Route a valid GitHub-backed session directly to the restored personal workspace and project catalog.
3. Present the shared two-action entry surface only when no valid protected session exists.
4. Authenticate the GitHub user and establish a protected application session.
5. Create or restore one personal workspace for the stable GitHub identity.
6. Route a restored non-empty workspace to its project catalog and expose an explicit `Add project` action.
7. Route an empty workspace, or an explicit `Add project` action, to repository selection.
8. Retrieve every repository available under the granted GitHub access and expose searchable loading, empty, and failure states.
9. Accept one explicit repository selection.
10. Derive and validate the project display name under workspace-scoped rules.
11. Create the project and canonical repository connection in one transaction.
12. Show the resulting project and connection state without modifying the repository or starting an agent.

Exact protocols and storage schemas remain deferred until the technology update.

## Components Affected

- Entry, GitHub sign-in, session restoration, and sign-out surfaces.
- Shared onboarding theme tokens, typography, responsive behavior, and accessible interaction states.
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
- `ClientThemePreference`: an optional current-device light or dark choice with no hosted identity, workspace, project, or analytics association.
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
- Manual theme preference remains inside the current client storage boundary and is not sent to the control plane, identity provider, analytics, or other devices.
- Every personal-data field and processing path must have an approved GDPR data contract before implementation.

## Interfaces

- Entry interface: resolve session state, expose both product paths only to unauthenticated clients, and avoid conflating repository location with later agent execution location.
- Theme interface: use the current operating-system preference when no local override exists, permit manual switching, restore only the current device's override, and preserve semantic roles and focus visibility in both themes.
- GitHub identity interface: authenticate a stable provider identity using the minimum approved permissions.
- Session interface: establish, restore, expire, revoke, and end authenticated access.
- Project-catalog interface: show existing projects after workspace restoration and expose `Add project` without mutating project or repository state.
- Repository catalog interface: paginate and search every repository returned under granted access and return stable identity plus display metadata.
- Repository-selection interface: expose one keyboard-operable selection model and distinct loading, no-match, empty, failure, and restricted-access states.
- Project registration interface: enforce repository uniqueness, allocate a workspace-scoped name, and create the project and connection atomically.
- Project naming interface: accept natural Unicode display text, validate case-insensitive workspace uniqueness, and rename without changing stable identities or deriving machine identity from the display value.
- Connection-status interface: distinguish connected and disconnected provider state without exposing secrets.
- Privacy-governance interface: block schema and backend approval until each processing activity has its required data contract and review.

## Decisions and Tradeoffs

### Two Entry Actions

- Choice: Present `Login with GitHub` and `Work without GitHub` as distinct primary actions.
- Reason: Repository location and GitHub account ownership are separate user choices.
- Consequence: Release sequencing must not expose an action whose complete path is unavailable; the local path is defined separately.

### Session-Aware Entry Routing

- Choice: Treat the two-action entry surface as the unauthenticated chooser, bypass it for a valid GitHub-backed application session, and return to it after sign-out or invalid session resolution.
- Reason: Returning users should resume their workspace without repeating provider authentication, while unauthenticated clients must not receive protected catalog data.
- Consequence: Session validation must complete before protected routing, invalid or revoked sessions must fail closed, and sign-out must preserve on-device project data while removing hosted access.

### Existing Workspace Before New Project

- Choice: Route a freshly authenticated non-empty workspace to its project catalog with an explicit `Add project` action, while an empty workspace continues directly to repository selection.
- Reason: Returning users should resume existing work instead of being forced through new-project onboarding, while a first-time user should reach the next required action without an empty intermediate page.
- Consequence: Workspace restoration must determine whether projects exist before routing, and `Add project` must be a non-mutating transition into the same repository-selection flow.

### Prototype As A Design Reference

- Choice: Preserve the generated prototype under `design-references/01-github-project-onboarding/claude-design/` as a visual and interaction reference only; do not import its generated design-canvas runtime, `support.js`, inline implementation, mock state controls, or sample data into the application.
- Reason: The prototype provides a useful UX direction before the application architecture is selected, but its runtime and shortcuts are not production decisions.
- Consequence: Implementation must recreate approved patterns in the selected application stack and prove them through the canonical browser checks. The original ZIP remains ignored and untracked; the exported reference is review evidence, not a project source of truth.

### Graphite And Teal Dual Theme

- Choice: Use `Public Sans` with a system sans-serif fallback and a graphite-neutral, teal-primary visual system with light and dark modes.
- Reason: The combination keeps operational information readable and gives primary actions a distinct identity without using a one-color dashboard.
- Consequence: If `Public Sans` is used, its delivery must follow the approved privacy and security boundary rather than copying the prototype's Google Fonts request. Theme preference is device-local and never synchronized to the hosted identity.

Core light tokens:

- Canvas `#F6F7F8`, surface `#FFFFFF`, raised surface `#EEF1F2`.
- Primary text `#182022`, secondary text `#566166`, subtle border `#D7DDDF`, control border `#7A878C`.
- Primary teal `#006D77`, on-primary `#FFFFFF`, primary tint `#D8F3F2`, focus `#0B6FDB`.

Core dark tokens:

- Canvas `#101415`, surface `#181D1F`, raised surface `#22282A`.
- Primary text `#F2F5F4`, secondary text `#AAB5B2`, subtle border `#343C3F`, control border `#6F7D80`.
- Primary teal `#55D6D2`, on-primary `#082021`, primary tint `#143638`, focus `#75B8FF`.

Semantic tokens:

- Connected: light `#1F7A4C` on `#E8F5ED`; dark `#66D28F` on `#153524`.
- Information: light `#1769AA` on `#EAF3FB`; dark `#78B9F2` on `#173149`.
- Blocked or attention: light `#8A5000` on `#FFF2D6`; dark `#FFC266` on `#3B2A12`.
- Failure: light `#B42318` on `#FDECEA`; dark `#FF8A82` on `#421F1D`.

### Device-Local Theme Preference

- Choice: Store a manual light or dark choice only on the current device and use the current operating-system preference when no local choice exists.
- Reason: Theme is a client presentation preference that should work before authentication and does not need hosted identity processing or cross-device synchronization.
- Consequence: Sign-in and sign-out preserve the local choice, a different device follows its own local or operating-system state, and the exact client storage mechanism remains an implementation decision.

### Compact Stateful Onboarding

- Choice: Use a focused entry surface, compact authentication state, dense single-selection repository list, explicit confirmation, concise creation summary, and visible disconnected recovery across desktop and mobile.
- Reason: Non-technical and technical users need to scan repository choices and recovery actions without decorative dashboard noise.
- Consequence: Loading skeletons, search no-match, empty catalog, retrieval failure, restricted organization access, naming feedback, connected state, and disconnected state require stable responsive layouts and keyboard proof.

### Complete GitHub Repository Catalog

- Choice: Show every repository returned under the user's granted access and link only the confirmed selection.
- Reason: Non-technical users should not need repository URLs or terminal commands.
- Consequence: Authorization scope, pagination, rate limits, organization policy, and large-catalog usability require explicit design.

### Registered Public GitHub App

- Choice: Use the registered public GitHub App `Orchestra-workflow` at `https://github.com/apps/orchestra-workflow` for GitHub user authorization and repository installation access.
- Reason: One public app identity gives users a GitHub-hosted authorization and installation surface for personal and organization repositories.
- Consequence: The App ID and client ID will be supplied through runtime configuration when the application skeleton exists. Their values, along with the client secret, private key, webhook secret, user tokens, and installation tokens, must not be committed. Permission scope, token lifecycle, session handling, webhook delivery, and organization approval behavior remain implementation blockers.

### One Project Per Repository

- Choice: Enforce one repository per project and one project per canonical repository inside a personal workspace.
- Reason: Later specifications, runs, workers, and evidence need one unambiguous repository boundary.
- Consequence: Monorepo subprojects and multiple SDD configurations for one repository are deferred.

### Editable Workspace-Scoped Names

- Choice: Default the project name from the repository, allocate the lowest available numeric suffix case-insensitively, and allow later edits.
- Reason: The default minimizes setup while workspace scope permits independent users to organize the same repository differently.
- Consequence: Persistence must enforce concurrency-safe uniqueness while stable identities remain separate from the display name.

### Natural Display Names, Not Slugs

- Choice: Allow spaces and Unicode in project display names and preserve the user's display text instead of forcing lowercase or slug conversion.
- Reason: BA, PO, PM, and international users should be able to name projects in familiar language, while stable project and repository identities already serve machine requirements.
- Consequence: Project names cannot be used directly as identifiers, paths, or URLs. Technical design must choose a safe validation and comparison strategy without changing the accepted display behavior.

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
- Name comparison can differ across runtimes or storage systems. Select and test one canonical strategy without rewriting accepted display text.
- GitHub outages, rate limits, SSO, and organization policy can interrupt onboarding. Preserve consistent state and expose actionable recovery.
- Credentials can leak through browser payloads, logs, analytics, or diagnostics. Keep them in the accepted credential boundary and test every failure surface.
- Stale, expired, or revoked sessions can expose catalog data or create redirect loops. Resolve session state before protected rendering and test direct navigation, expiry, revocation, and sign-out transitions.
- A non-technical user may confuse GitHub authentication with agent-provider authentication. Keep those concepts and statuses separate.
- Prototype behavior can silently become product behavior. Do not adopt its forced lowercase default names, letters-and-numbers-only validation, always-new-project routing, non-functional local-path toast, or prototype-only controls without an accepted specification update.
- Loading `Public Sans` from Google Fonts would create an external browser request and potential personal-data processing. Select an approved self-hosted or otherwise governed delivery path before implementation.
- Theme and responsive variants can drift into different behavior. Test the same actions, state meaning, keyboard order, focus, and text fit across both themes and target viewports.
- Personal data can escape its lifecycle through logs, backups, analytics, or processors. Include every copy and transfer in the approved data contract.
- Implementing the GitHub path before the local path may expose an unusable primary action. Coordinate release boundaries with the local onboarding specification.

## Open Questions

- Which user-authorization, installation, permission, revocation, webhook, and organization-approval configuration completes the registered `Orchestra-workflow` GitHub App integration?
- How are GitHub and application sessions protected, refreshed, revoked, and isolated from coding agents?
- Which stable repository identifier and transfer rules enforce uniqueness?
- Which storage-selection contract from `specs/05-project-storage-lifecycle/` is required before project creation commits?
- How are the two entry paths sequenced without a non-functional action?
- Which validation and canonical comparison strategy safely implements natural display names and case-insensitive uniqueness?
- Which GDPR processing contracts and reviews apply to identity, repository metadata, projects, logs, support, security, and analytics?
- Which runtime, persistence, UI, deployment, and Symphony boundary should be selected?
- Which automated, integration, security, and browser commands form the verification gate?
