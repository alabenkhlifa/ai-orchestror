# Project Portability Tasks

## Status

Blocked

## Active Slice

Deliver export and re-import of one minimal project package containing approved project metadata and current specifications, with version, integrity, secret exclusion, validation, and atomic import.

## Implementation Boundary

Included:

- Initial allowlisted package schema and version.
- Consistent export snapshot for approved metadata and specification files.
- Integrity information and negative secret filtering.
- Isolated import validation and temporary cleanup.
- Atomic import into an available storage mode.
- Name and duplicate conflict detection.
- Privacy, security, compatibility, and browser proof.

Excluded:

- Repository source, credentials, sessions, worker or agent data, collaboration memberships, and arbitrary executable artifacts.
- Direct storage migration and automatic repository reconnection.

Deferred after this slice:

- Additional history, run artifacts, comments, attachments, richer provenance, encryption, signing, and cross-version migrations.
- Explicit repository reconnection after import.

## Tasks

- [ ] Approve the initial package schema, lifecycle, and compatibility contract.
  - Purpose: Define exactly what crosses the portability boundary and how it is governed.
  - Proof: Requirements, design, schema, threat model, data contract, and canonical test commands have no slice blockers.

- [ ] Implement consistent export snapshot and allowlisted serialization.
  - Purpose: Produce one deterministic package from authorized current project data.
  - Proof: Golden and authorization tests cover the approved fields, versions, ordering, and concurrent project updates.

- [ ] Implement secret exclusion and package integrity.
  - Purpose: Prevent credential leakage and detect corruption or tampering.
  - Proof: Negative secret scans, mutation tests, and integrity fixtures pass for every forbidden category.

- [ ] Implement isolated package intake and validation.
  - Purpose: Reject unsafe or incompatible content before persistence.
  - Proof: Security tests cover format, version, size, path traversal, archive bombs, links, unknown fields, malformed sections, and cleanup.

- [ ] Implement conflict preflight and atomic import.
  - Purpose: Create one project without silent overwrite, duplicate repository identity, or partial state.
  - Proof: Tests cover names, duplicates, storage prerequisites, confirmation, concurrency, rollback, and unchanged repositories.

- [ ] Build export and import UX.
  - Purpose: Show included data, validation results, conflicts, and actionable recovery.
  - Proof: Desktop and mobile browser scenarios cover export, compatible import, rejection, confirmation, cancellation, and success.

- [ ] Enforce package GDPR lifecycle and security review.
  - Purpose: Govern exports, temporary files, logs, backups, processors, transfers, rights, and deletion.
  - Proof: Lifecycle, access, deletion, rights, processor, transfer, audit, and required privacy checks pass.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Golden export and round-trip compatibility fixtures pass.
- [ ] Secret-exclusion and integrity tests pass.
- [ ] Malformed, unsafe, oversized, path, archive, and resource-limit tests pass.
- [ ] Name, duplicate, storage, atomicity, concurrency, and rollback tests pass.
- [ ] Temporary-data cleanup and GDPR lifecycle review pass.
- [ ] Required desktop and mobile browser scenarios pass.
- [ ] Build, formatting, lint, static checks, and failure-log review pass.

## Blocked Decisions

- Approve the initial package fields, history, attachments, and explicit source exclusion.
- Select package format, versioning, integrity, compression, resource limits, and compatibility behavior.
- Define project identity, provenance, duplicate, name, repository, and storage conflict rules.
- Define temporary-data, package, log, backup, processor, transfer, rights, retention, and deletion contracts.
- Select implementation architecture and canonical compatibility, security, automated, and browser commands.

## Progress Log

### 2026-07-23 - Extracted from project onboarding

- Completed: Isolated the accepted export/import, secret exclusion, compatibility, conflict, repository reconnection, and privacy boundaries.
- Remaining: Approve the initial package scope, identity rules, format, threat model, lifecycle, architecture, and verification strategy.
- Failed checks: None; implementation has not started.
- Spec updates: Created a focused portability specification and limited its first executable slice to a minimal safe round trip.
