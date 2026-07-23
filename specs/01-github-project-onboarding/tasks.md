# GitHub Project Onboarding Tasks

## Status

Blocked

## Active Slice

Deliver GitHub project onboarding end to end: authenticate one user, restore their personal workspace, list every repository under the granted access, select where the project work is saved, create one project for one confirmed repository, and open its dashboard with the repository, storage, and connection state.

## Implementation Boundary

Included:

- Application bootstrap required by this slice after architecture approval.
- Session-aware entry routing, GitHub sign-in, protected session restoration, and sign-out.
- Approved onboarding visual tokens, device-local light and dark theme preference, responsive layouts, keyboard operation, and non-color status cues.
- Personal workspace creation and restoration.
- Existing-workspace catalog routing and the non-mutating `Add project` handoff.
- GitHub App repository-access checking, the dedicated grant screen, installation handoff, and validated return.
- Complete authorized repository catalog retrieval, search, and user-facing states.
- Shared plain-language project-data storage selection before final confirmation.
- Atomic project and repository-connection creation.
- Direct handoff to the new project's dashboard with repository, storage, and connection state.
- Workspace-scoped naming and post-creation rename.
- Persistent disconnected project state.
- GDPR data contracts, security controls, and proof for data introduced by the slice.
- Automated, integration, security, and browser verification.

Excluded:

- Local repository onboarding, passwordless hosted access, identity linking, storage migration, portability, collaboration, and agent execution.
- Remote, cloud, or Raspberry Pi workers.
- Repository editing or source upload.

Deferred after this slice:

- The separate feature specifications under `specs/02-` through `specs/06-`.
- Monorepo subprojects and multiple projects for one repository in a workspace.

Release boundary:

- This slice may be implemented and verified independently.
- The first usable release remains blocked until `specs/02-local-project-onboarding/` and every shared dependency invoked by both onboarding paths also pass their release gates.
- Coordinated browser proof must show that `Login with GitHub` and `Work without GitHub` are both available and complete from the same entry surface.

## Tasks

- [ ] Establish the approved application skeleton and canonical development checks.
  - Purpose: Provide only the runtime, UI, persistence, configuration, and test foundations required by this slice.
  - Proof: Setup, build, formatting, lint, static checks, and the empty test suite succeed from a clean checkout.

- [ ] Implement GitHub identity and protected session behavior.
  - Purpose: Let the user sign in, restore access, and sign out without exposing credentials.
  - Proof: Automated and browser tests cover unauthenticated entry, valid-session catalog routing, success, restoration, invalid or expired sessions, revocation, sign-out return to entry, cancellation, provider failure, and rejected post-sign-out access.

- [ ] Create and restore the personal workspace.
  - Purpose: Establish the ownership boundary for projects and repository connections.
  - Proof: Tests show stable restoration, isolation between users, no duplicate workspace under retry or concurrency, non-empty workspace routing to the catalog, empty workspace routing to repository selection, and a non-mutating `Add project` handoff.

- [ ] Implement GitHub App repository access and the complete repository catalog.
  - Purpose: Guide non-technical users through repository access when needed, then let them find every repository returned under the validated grant.
  - Proof: Integration and browser tests cover the approved `Metadata: read-only` permission boundary with no assumed write access, no accessible installation, the grant screen, GitHub handoff, pending organization approval and status refresh, valid return, rejected or invalid return, pagination, search, empty results, personal, private, and organization repositories, authorization failures, rate limits, and provider failure.

- [ ] Implement atomic project and repository linking.
  - Purpose: Create one project for one selected canonical repository and explicit storage mode without partial or duplicate records.
  - Proof: Persistence tests cover repository uniqueness, required storage selection, atomic storage initialization, rollback, concurrency, workspace ownership, and provider identity stability.

- [ ] Implement project display-name allocation and editing.
  - Purpose: Apply repository defaults, case-insensitive lowest-available suffixes, and safe later renames.
  - Proof: Tests cover preserved natural display names, spaces, Unicode, no slug conversion, cross-user reuse, case-insensitive conflicts, concurrent creation and rename, and unchanged stable identities.

- [ ] Preserve project state when GitHub access is lost.
  - Purpose: Treat access loss as a recoverable connection state.
  - Proof: Tests show the project remains visible, becomes disconnected, exposes no stale credential, and returns to connected after revalidation.

- [ ] Build the end-to-end onboarding and new-project dashboard handoff.
  - Purpose: Complete the workflow without repository URLs or terminal commands.
  - Proof: Desktop and mobile browser scenarios in both themes cover operating-system fallback, device-local manual persistence, no hosted synchronization, sign-in and sign-out continuity, unauthenticated entry, valid-session bypass, sign-in, existing-project catalog routing, empty-workspace continuation, `Add project`, repository-access checking, the grant screen, GitHub handoff, pending organization approval and refresh, valid return, keyboard catalog search and selection, no-match, empty, failure, restricted access, the approved storage copy, unavailable-mode setup, preserved repository and onboarding state, return after setup success, cancellation, or failure, availability refresh without implicit selection, explicit selection, confirmation, naming, duplicate prevention, actionable failures, sign-out, direct new-project dashboard routing, visible repository, storage mode, and connection status, focus visibility, status cues, and text fit.

- [ ] Define and enforce the slice GDPR data contract.
  - Purpose: Make lawful processing, minimization, retention, rights, processors, transfers, anonymisation, and security part of implementation approval.
  - Proof: The processing inventory and automated lifecycle checks cover every field, log, cache, backup, export, processor, and allowed anonymous metric, with required privacy review recorded.

- [ ] Complete security and observability review.
  - Purpose: Diagnose failure without leaking secrets or leaving partial state.
  - Proof: Security tests and log review show no credential exposure and sufficient account-neutral diagnostics for every failure path.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Entry routing, authentication, workspace, repository-access grant, repository catalog, storage selection, project-linking, naming, post-creation dashboard routing, and connection-state tests pass.
- [ ] GitHub integration and permission-boundary tests pass against the approved provider strategy.
- [ ] Build, formatting, lint, and static checks pass.
- [ ] Required desktop and mobile browser scenarios pass.
- [ ] Light and dark theme, operating-system fallback, device-local preference, no-sync, keyboard-only, focus, contrast, non-color status, responsive text-fit, and layout-stability checks pass.
- [ ] Credential, session, and failure-log review passes.
- [ ] GDPR data contracts, retention rules, rights paths, processor boundaries, anonymisation proof, and required privacy review are complete.
- [ ] New decisions and invalidated proof are written back.

## Blocked Decisions

- Select the application runtime, UI approach, persistence system, deployment model, and Symphony boundary.
- Define the registered `Orchestra-workflow` GitHub App technical integration within the approved `Metadata: read-only` permission boundary: repository identity, credential lifecycle, webhook behavior, return validation, organization-approval status detection, and session design.
- Complete the device and hosted prerequisites and atomic project-storage initialization contract from `specs/05-project-storage-lifecycle/`.
- Select a safe project-name validation and case-insensitive comparison strategy without changing the accepted display behavior.
- Approve the slice GDPR processing inventory, retention, rights, processors, transfers, analytics boundary, and required reviews.
- Define canonical build, formatting, lint, static-check, automated-test, integration-test, security-test, and browser-test commands.

## Progress Log

### 2026-07-23 - Specification split checkpoint

- Completed: Narrowed the original project-onboarding specification to the GitHub sign-in, repository discovery, project creation, naming, and disconnected-state slice.
- Remaining: Resolve the listed architecture, integration, storage, privacy, and verification decisions before approval.
- Failed checks: None; implementation has not started.
- Spec updates: Moved local onboarding, hosted passwordless access, identity linking, storage lifecycle, and portability into separate ordered specifications without changing accepted behavior.
