# GitHub Project Onboarding Tasks

## Status

Blocked

## Active Slice

Deliver GitHub project onboarding end to end: authenticate one user, restore their personal workspace, list every repository under the granted access, create one project for one confirmed repository, and show the resulting connection state.

## Implementation Boundary

Included:

- Application bootstrap required by this slice after architecture approval.
- GitHub sign-in, protected session restoration, and sign-out.
- Personal workspace creation and restoration.
- Complete authorized repository catalog retrieval, search, and user-facing states.
- Atomic project and repository-connection creation.
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

## Tasks

- [ ] Establish the approved application skeleton and canonical development checks.
  - Purpose: Provide only the runtime, UI, persistence, configuration, and test foundations required by this slice.
  - Proof: Setup, build, formatting, lint, static checks, and the empty test suite succeed from a clean checkout.

- [ ] Implement GitHub identity and protected session behavior.
  - Purpose: Let the user sign in, restore access, and sign out without exposing credentials.
  - Proof: Automated and browser tests cover success, restoration, sign-out, cancellation, provider failure, and rejected post-sign-out access.

- [ ] Create and restore the personal workspace.
  - Purpose: Establish the ownership boundary for projects and repository connections.
  - Proof: Tests show stable restoration, isolation between users, and no duplicate workspace under retry or concurrency.

- [ ] Implement the complete GitHub repository catalog.
  - Purpose: Let non-technical users find every repository returned under granted access.
  - Proof: Integration and browser tests cover pagination, search, empty results, personal, private, and organization repositories, authorization failures, rate limits, and provider failure.

- [ ] Implement atomic project and repository linking.
  - Purpose: Create one project for one selected canonical repository without partial or duplicate records.
  - Proof: Persistence tests cover repository uniqueness, rollback, concurrency, workspace ownership, and provider identity stability.

- [ ] Implement project display-name allocation and editing.
  - Purpose: Apply repository defaults, case-insensitive lowest-available suffixes, and safe later renames.
  - Proof: Tests cover cross-user reuse, case conflicts, concurrent creation and rename, and unchanged stable identities.

- [ ] Preserve project state when GitHub access is lost.
  - Purpose: Treat access loss as a recoverable connection state.
  - Proof: Tests show the project remains visible, becomes disconnected, exposes no stale credential, and returns to connected after revalidation.

- [ ] Build the end-to-end onboarding and project-summary experience.
  - Purpose: Complete the workflow without repository URLs or terminal commands.
  - Proof: Desktop and mobile browser scenarios cover sign-in, catalog search, selection, confirmation, naming, duplicate prevention, actionable failures, and final summary.

- [ ] Define and enforce the slice GDPR data contract.
  - Purpose: Make lawful processing, minimization, retention, rights, processors, transfers, anonymisation, and security part of implementation approval.
  - Proof: The processing inventory and automated lifecycle checks cover every field, log, cache, backup, export, processor, and allowed anonymous metric, with required privacy review recorded.

- [ ] Complete security and observability review.
  - Purpose: Diagnose failure without leaking secrets or leaving partial state.
  - Proof: Security tests and log review show no credential exposure and sufficient account-neutral diagnostics for every failure path.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Authentication, workspace, repository catalog, project-linking, naming, and connection-state tests pass.
- [ ] GitHub integration tests pass against the approved provider strategy.
- [ ] Build, formatting, lint, and static checks pass.
- [ ] Required desktop and mobile browser scenarios pass.
- [ ] Credential, session, and failure-log review passes.
- [ ] GDPR data contracts, retention rules, rights paths, processor boundaries, anonymisation proof, and required privacy review are complete.
- [ ] New decisions and invalidated proof are written back.

## Blocked Decisions

- Select the application runtime, UI approach, persistence system, deployment model, and Symphony boundary.
- Select the GitHub integration model, permission scope, repository identity, credential lifecycle, and session design.
- Approve the project-data storage-selection contract required before project creation.
- Decide how the GitHub and local entry actions are released without exposing a non-functional path.
- Approve the slice GDPR processing inventory, retention, rights, processors, transfers, analytics boundary, and required reviews.
- Define canonical build, formatting, lint, static-check, automated-test, integration-test, security-test, and browser-test commands.

## Progress Log

### 2026-07-23 - Specification split checkpoint

- Completed: Narrowed the original project-onboarding specification to the GitHub sign-in, repository discovery, project creation, naming, and disconnected-state slice.
- Remaining: Resolve the listed architecture, integration, storage, release-boundary, privacy, and verification decisions before approval.
- Failed checks: None; implementation has not started.
- Spec updates: Moved local onboarding, hosted passwordless access, identity linking, storage lifecycle, and portability into separate ordered specifications without changing accepted behavior.
