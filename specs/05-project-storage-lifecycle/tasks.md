# Project Storage Lifecycle Tasks

## Status

Blocked

## Active Slice

Deliver explicit per-project storage selection at project creation, persist one authoritative storage mode, and show that mode consistently without implementing later migration.

## Implementation Boundary

Included:

- Device and hosted storage-mode values and ownership boundaries.
- Plain-language, explicit storage choice for GitHub and local repository projects.
- Prerequisite validation for accountless device and authorized hosted modes.
- Persistence and presentation of the authoritative mode in project catalogs and on the new-project dashboard.
- GDPR data contracts for the introduced records and paths.
- Automated and browser proof for selection, creation, restoration, and failure.

Excluded:

- Direct migration, soft deletion, two-year cleanup, resynchronization, and full rehydration in the first slice.
- Collaboration behavior, repository transfer, portability packages, and agent execution.

Deferred after this slice:

- Hosted-to-device and device-to-hosted migration.
- Retention enforcement, incremental synchronization, full upload, analytics, legal exceptions, and rights propagation beyond created records.

Release boundary:

- This active storage-selection slice is a shared dependency of the GitHub and local onboarding paths and must pass for both before the first usable release.

## Tasks

- [ ] Approve the device and hosted storage ownership contract.
  - Purpose: Define prerequisites, authority, persistence, privacy, and failure behavior before coding.
  - Proof: Requirements, design, data contracts, and test commands have no unresolved slice blockers.

- [ ] Implement the project-level storage-mode model.
  - Purpose: Give every project-data record one explicit authoritative boundary.
  - Proof: Schema and domain tests cover valid modes, ownership, missing-selection rejection, invalid state, and workspace isolation.

- [ ] Implement storage selection for both repository sources.
  - Purpose: Let users understand and explicitly choose where project work is saved without confusing it with repository or agent location.
  - Proof: Service and browser tests show the approved title, project-work explanation, `On this device` and `In my SDD Orchestrator account` consequences, both modes visible when a prerequisite is missing, relevant setup actions, preserved repository and onboarding state across device setup, return after success, cancellation, or failure, availability refresh without implicit selection, and no silent default.

- [ ] Integrate storage mode with atomic project creation.
  - Purpose: Prevent projects with missing, ambiguous, or partially initialized storage.
  - Proof: Transaction and fault-injection tests prove one committed mode or no project.

- [ ] Show storage mode and availability in project catalogs and on the new-project dashboard.
  - Purpose: Make mixed device and hosted projects understandable.
  - Proof: Desktop and mobile scenarios cover mixed modes, unavailable device data, hosted authorization, sign-out, and post-creation dashboard presentation with repository, storage mode, and connection status.

- [ ] Enforce the slice GDPR data contract and security boundary.
  - Purpose: Govern every introduced record, log, backup, processor, and metric from creation.
  - Proof: Access, retention, rights, deletion, processor, transfer, anonymisation, and review checks pass.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Storage-mode domain, ownership, prerequisite, transaction, and restoration tests pass.
- [ ] GitHub and local onboarding integration tests pass for both modes.
- [ ] Storage selection shows the approved labels and explanation, keeps unavailable modes visible with setup actions, preserves repository and onboarding state across device setup, returns to the same step without an implicit choice, and requires an explicit selection.
- [ ] Mixed catalog, post-creation dashboard, and sign-out browser scenarios pass.
- [ ] Failure leaves no project with partial or ambiguous storage state.
- [ ] GDPR data contract, privacy review, and secret-exposure checks pass.
- [ ] Build, formatting, lint, static checks, and logs review pass.

## Blocked Decisions

- Define the device and hosted persistence and authority model.
- Define how accountless and hosted identity prerequisites integrate with project creation.
- Select transaction and failure-recovery behavior for atomic project plus storage initialization.
- Approve the slice processing purposes, lawful bases, fields, access, retention, deletion, rights, processors, transfers, analytics, and reviews.
- Select implementation architecture and canonical verification commands.

## Progress Log

### 2026-07-23 - Extracted from project onboarding

- Completed: Isolated per-project storage, direct migration, hosted retention, resynchronization, GDPR lifecycle, anonymous analytics, and legal-retention decisions.
- Remaining: Resolve the active storage-selection architecture and later migration, synchronization, cleanup, privacy, and analytics blockers.
- Failed checks: None; implementation has not started.
- Spec updates: Created a focused lifecycle specification and limited its first executable slice to storage selection.
