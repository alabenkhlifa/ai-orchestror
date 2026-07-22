# Project Storage Lifecycle Tasks

## Status

Blocked

## Active Slice

Deliver explicit per-project storage selection at project creation, persist one authoritative storage mode, and show that mode consistently without implementing later migration.

## Implementation Boundary

Included:

- Device and hosted storage-mode values and ownership boundaries.
- Storage choice for GitHub and local repository projects.
- Prerequisite validation for accountless device and authorized hosted modes.
- Persistence and catalog presentation of the authoritative mode.
- GDPR data contracts for the introduced records and paths.
- Automated and browser proof for selection, creation, restoration, and failure.

Excluded:

- Direct migration, soft deletion, two-year cleanup, resynchronization, and full rehydration in the first slice.
- Collaboration behavior, repository transfer, portability packages, and agent execution.

Deferred after this slice:

- Hosted-to-device and device-to-hosted migration.
- Retention enforcement, incremental synchronization, full upload, analytics, legal exceptions, and rights propagation beyond created records.

## Tasks

- [ ] Approve the device and hosted storage ownership contract.
  - Purpose: Define prerequisites, authority, persistence, privacy, and failure behavior before coding.
  - Proof: Requirements, design, data contracts, and test commands have no unresolved slice blockers.

- [ ] Implement the project-level storage-mode model.
  - Purpose: Give every project-data record one explicit authoritative boundary.
  - Proof: Schema and domain tests cover valid modes, ownership, defaults, invalid state, and workspace isolation.

- [ ] Implement storage selection for both repository sources.
  - Purpose: Keep storage independent from GitHub or local repository location.
  - Proof: Service and browser tests show both choices under their correct identity and device prerequisites.

- [ ] Integrate storage mode with atomic project creation.
  - Purpose: Prevent projects with missing, ambiguous, or partially initialized storage.
  - Proof: Transaction and fault-injection tests prove one committed mode or no project.

- [ ] Show storage mode and availability in project catalogs and summaries.
  - Purpose: Make mixed device and hosted projects understandable.
  - Proof: Desktop and mobile scenarios cover mixed modes, unavailable device data, hosted authorization, and sign-out.

- [ ] Enforce the slice GDPR data contract and security boundary.
  - Purpose: Govern every introduced record, log, backup, processor, and metric from creation.
  - Proof: Access, retention, rights, deletion, processor, transfer, anonymisation, and review checks pass.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Storage-mode domain, ownership, prerequisite, transaction, and restoration tests pass.
- [ ] GitHub and local onboarding integration tests pass for both modes.
- [ ] Mixed catalog and sign-out browser scenarios pass.
- [ ] Failure leaves no project with partial or ambiguous storage state.
- [ ] GDPR data contract, privacy review, and secret-exposure checks pass.
- [ ] Build, formatting, lint, static checks, and logs review pass.

## Blocked Decisions

- Define the device and hosted persistence and authority model.
- Define how accountless and hosted identity prerequisites integrate with project creation.
- Select transaction and failure-recovery behavior for atomic project plus storage initialization.
- Approve the slice processing purposes, lawful bases, fields, access, retention, deletion, rights, processors, transfers, analytics, and reviews.
- Select implementation architecture and canonical verification commands.
- Decide the release dependency between this slice and GitHub and local onboarding.

## Progress Log

### 2026-07-23 - Extracted from project onboarding

- Completed: Isolated per-project storage, direct migration, hosted retention, resynchronization, GDPR lifecycle, anonymous analytics, and legal-retention decisions.
- Remaining: Resolve the active storage-selection architecture and later migration, synchronization, cleanup, privacy, and analytics blockers.
- Failed checks: None; implementation has not started.
- Spec updates: Created a focused lifecycle specification and limited its first executable slice to storage selection.
