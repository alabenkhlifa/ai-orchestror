# Local Project Onboarding Tasks

## Status

Blocked

## Active Slice

Deliver accountless on-device onboarding for one local Git repository through one paired worker, ending with a visible project and repository connection without source upload.

## Implementation Boundary

Included:

- Accountless device workspace required by the local path.
- Worker discovery, installation guidance, secure pairing, and status.
- Local Git repository selection and validation.
- Approved metadata exchange and atomic project registration.
- Shared naming and repository-uniqueness rules.
- Connection-state and failure UX.
- Privacy and security proof for device metadata and pairing credentials.

Excluded:

- Hosted storage and passwordless authentication.
- Remote or cloud workers and agent execution.
- Source upload, browsing, editing, or execution from the control plane.
- Shared-operating-system-user isolation.

Deferred after this slice:

- Hosted local-repository projects through `specs/03-hosted-passwordless-access/` and `specs/05-project-storage-lifecycle/`.
- Combined local and hosted catalog deduplication beyond non-mutating composition.

## Tasks

- [ ] Establish the accountless device-workspace boundary.
  - Purpose: Persist local project ownership without requiring an account.
  - Proof: Tests show stable access under the same OS boundary and isolation from hosted authorization.

- [ ] Implement worker discovery and installation guidance.
  - Purpose: Give non-technical users an actionable path when no worker is available.
  - Proof: Browser scenarios cover detected, missing, incompatible, and unavailable worker states.

- [ ] Implement secure workspace-bound pairing.
  - Purpose: Authorize one worker for one workspace without transferable credentials.
  - Proof: Security tests cover attempt expiry, confirmation, replay rejection, revocation, rotation, and cross-workspace denial.

- [ ] Implement local repository selection and validation.
  - Purpose: Validate one user-selected Git repository entirely on the worker.
  - Proof: Integration tests cover valid, invalid, inaccessible, moved, and unavailable repositories without source upload.

- [ ] Define and enforce minimum outbound metadata.
  - Purpose: Establish repository identity and status without leaking paths or source content unnecessarily.
  - Proof: Contract and privacy tests reject fields outside the approved schema and lifecycle.

- [ ] Create the project and local repository connection atomically.
  - Purpose: Apply shared naming and uniqueness rules without partial records.
  - Proof: Tests cover concurrency, duplicate identity, suffix allocation, rollback, and unchanged repository state.

- [ ] Build local onboarding and connection-state UX.
  - Purpose: Complete the path without requiring terminal interaction beyond any approved installer step.
  - Proof: Desktop and mobile scenarios cover pairing, selection, confirmation, success, and actionable recovery.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Pairing security and cross-workspace isolation tests pass.
- [ ] Worker and repository integration tests pass on supported platforms.
- [ ] Source-upload and metadata-minimization checks pass.
- [ ] Project naming, uniqueness, atomicity, and connection-state tests pass.
- [ ] Required browser scenarios pass.
- [ ] GDPR data contract and privacy review for device metadata and credentials are complete.
- [ ] Build, formatting, lint, static checks, and logs review pass.

## Blocked Decisions

- Select worker packaging, supported platforms, update and signing model.
- Select pairing protocol, credential lifecycle, transport, and revocation behavior.
- Define canonical local repository identity and minimum outbound metadata.
- Define accountless device-workspace persistence and recovery.
- Select the application-to-worker test strategy and canonical commands.
- Approve the relevant GDPR data contract, retention, processor, transfer, rights, and review decisions.
- Approve integration boundaries with project storage selection and hosted passwordless access.

## Progress Log

### 2026-07-23 - Extracted from project onboarding

- Completed: Isolated the accepted local-repository, accountless-device, worker-pairing, source-locality, and connection-state behavior.
- Remaining: Resolve worker architecture, repository identity, metadata, privacy, integration, and verification decisions.
- Failed checks: None; implementation has not started.
- Spec updates: Created a focused local onboarding specification without changing accepted product behavior.
