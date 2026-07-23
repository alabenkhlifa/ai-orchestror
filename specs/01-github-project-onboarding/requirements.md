# GitHub Project Onboarding

## Status

Draft

## Outcome

A BA, PO, PM, developer, or other project contributor can sign in with GitHub, find any repository available through their granted access, and create one SDD Orchestrator project linked to that repository without modifying it or starting an AI agent.

## Users

- Business analysts, product owners, and product managers organizing specification work.
- Developers and technical contributors linking repositories to the SDD workflow.

## Primary Workflow

1. SDD Orchestrator evaluates whether the current client has a valid protected GitHub-backed application session.
2. A valid session restores the personal workspace and opens the project catalog without showing the entry surface or requiring GitHub authentication again.
3. Without a valid session, the entry surface presents `Login with GitHub` and `Work without GitHub` as distinct primary actions.
4. The user selects `Login with GitHub` and completes GitHub authentication.
5. SDD Orchestrator creates or restores the user's personal workspace and protected session.
6. When the restored workspace already contains projects, the product opens its project catalog and exposes an `Add project` action instead of forcing repository selection.
7. When the restored workspace is empty, or the user selects `Add project`, the repository picker loads every repository returned under the user's granted GitHub access and supports search.
8. The user selects and confirms one repository.
9. The product derives the default project name from the repository name, allocates the lowest available numeric suffix when needed, and allows the user to edit the name.
10. The project and repository connection are created atomically under the personal workspace.
11. The product shows the project, repository source, and connection status without changing repository content or starting an agent.

## In Scope

- The GitHub action on the two-action entry surface.
- Session-aware entry routing, GitHub authentication, session restoration, and sign-out.
- Personal workspace creation and restoration.
- Existing-workspace catalog routing and the `Add project` handoff to repository selection.
- Retrieval, search, loading, empty, and failure states for every repository returned by GitHub under the granted access.
- Explicit selection of one GitHub repository.
- Responsive light and dark onboarding presentation, keyboard operation, visible focus, and non-color status cues.
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
- The entry surface is the unauthenticated chooser and must not be shown when the current client has a valid protected GitHub-backed application session.
- A valid GitHub-backed application session must restore the personal workspace and route directly to the project catalog without requiring GitHub authentication again.
- An invalid, expired, or revoked session must not expose the project catalog and must return the client to the entry surface.
- Signing out must end the protected hosted session and return the client to the entry surface without deleting on-device project data.
- A primary action must not be exposed as functional before its complete path can be used.
- The onboarding experience must support light and dark themes, use the operating-system preference on first load, and provide a manual theme control.
- A manual theme choice must be stored only on the current device and must not be uploaded, synchronized, or attached to a hosted identity or workspace.
- When the current device has no stored manual choice, the product must use its current operating-system theme preference.
- Signing in or out must not replace the current device's manual theme choice.
- Theme, connection, warning, and failure meaning must never depend on color alone; meaningful states require text and an icon or equivalent non-color cue.
- GitHub sign-in must restore one stable personal workspace for the authenticated GitHub identity.
- Fresh GitHub authentication that restores a non-empty workspace must open the project catalog rather than force the user to create another project.
- Fresh GitHub authentication that creates or restores an empty workspace must continue directly to repository selection.
- The project catalog must expose an `Add project` action that opens repository selection without creating or linking anything by itself.
- The repository picker must show every repository returned by GitHub under the user's granted access; visibility must not link a repository automatically.
- The repository picker must use an accessible single-selection list that supports keyboard selection and shows the repository owner, name, visibility, and organization when that approved metadata is available.
- Search with no matches, no authorized repositories, retrieval failure, and organization-restricted access are distinct states with relevant recovery actions.
- A project is created only after the user explicitly selects and confirms a repository.
- A project must be linked to exactly one repository.
- A repository can be linked to at most one project in the same personal workspace.
- Different users may link the same repository independently in their separate personal workspaces.
- The default project name is the repository name.
- Default-name derivation must preserve the repository name's display spelling and case; case-insensitive comparison is used only to enforce uniqueness.
- A project name is human-facing display text, not a slug, URL segment, repository identifier, filesystem path, or database key.
- Project names may contain spaces and Unicode characters and must not be converted to lowercase, transliterated, or rewritten as slugs for display.
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

- Given the current client has no valid protected session, when SDD Orchestrator opens, then the entry surface shows `Login with GitHub` and `Work without GitHub` as distinct primary actions.
- Given the entry or onboarding flow is displayed, when the user changes between light and dark themes, then the current screen remains usable with the same actions, content, status meaning, focus visibility, and layout stability.
- Given the current device has no stored manual theme choice, when SDD Orchestrator opens, then it uses the current operating-system theme preference.
- Given the user manually selects a theme, when SDD Orchestrator is reopened on the same device, then that local choice is restored without reading or writing a hosted theme preference.
- Given the same user opens SDD Orchestrator on another device with no stored choice, when the application loads, then the other device uses its own operating-system preference rather than synchronizing the first device's choice.
- Given the user signs in or out, when the entry or protected surface is shown, then the current device's manual theme choice remains unchanged.
- Given the current client has a valid GitHub-backed application session, when SDD Orchestrator opens, then the personal workspace is restored and the project catalog is shown without rendering the entry surface or requiring GitHub authentication again.
- Given the current session is invalid, expired, or revoked, when a protected route is opened, then no project catalog data is exposed and the client returns to the entry surface.
- Given a GitHub-authenticated user signs out, when session termination succeeds, then the entry surface is shown and on-device project data remains unchanged.
- Given GitHub authentication succeeds, when onboarding continues, then the user's stable personal workspace is created or restored without exposing credentials.
- Given fresh GitHub authentication restores a workspace with existing projects, when routing completes, then the project catalog is shown with an `Add project` action and repository selection is not forced.
- Given fresh GitHub authentication creates or restores an empty workspace, when routing completes, then repository selection opens directly.
- Given the user selects `Add project` from the project catalog, when the action opens, then repository selection is shown and no project or repository connection has been created yet.
- Given GitHub returns accessible personal, private, or organization repositories, when the picker loads, then every returned repository is available and searchable without requiring a URL.
- Given the repository picker has focus, when the user navigates and selects with a keyboard, then exactly one repository can be selected and confirmed without pointer input.
- Given search has no matches, GitHub returns no repositories, retrieval fails, or organization policy restricts access, when the state is shown, then it is distinguishable from the other states and presents an appropriate recovery action.
- Given repository retrieval is empty or fails, when the request ends, then the user sees an actionable state and no partial project is created.
- Given an unlinked repository is confirmed, when creation succeeds, then exactly one project and one repository connection are created atomically.
- Given a repository named `example` and no conflicting project name, when it is linked, then the default project name is `example`.
- Given a repository named `Café Roadmap` and no conflicting project name, when confirmation opens, then the default project name remains `Café Roadmap` without slug conversion or character loss.
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
- Which implementation validation and comparison strategy safely enforces natural display names and case-insensitive uniqueness?
- Which controller and processor roles, purposes, lawful bases, retention periods, rights workflows, subprocessors, transfers, and privacy reviews apply to this slice?
- Which anonymous aggregate metrics are necessary for GitHub onboarding, what aggregation thresholds prevent singling out, and how long is each retained?
- Which application runtime, UI approach, persistence system, deployment model, and Symphony integration satisfy this slice?
- Which canonical build, formatting, lint, static-check, automated-test, integration-test, and browser-test commands prove this slice?
