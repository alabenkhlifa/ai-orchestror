# GitHub Identity Linking Tasks

## Status

Blocked

## Active Slice

Deliver conservative automatic matching and a conflict-free atomic merge into the existing passwordless workspace, while safely aborting every ineligible, ambiguous, or conflicting case without mutation.

## Implementation Boundary

Included:

- Verified-primary retrieval and secondary-address non-retention.
- ASCII eligibility and approved automatic-match normalization.
- Zero-or-one candidate resolution and collision safety.
- Complete non-mutating merge preflight.
- Conflict-free atomic identity and hosted-project consolidation.
- Worker-pairing revocation after commit.
- Minimal merge record and user disclosure.
- Security, privacy, concurrency, and failure proof.

Excluded:

- Collaboration membership reconciliation.
- Automatic matching for internationalized addresses.
- Accountless device-project upload or identity merge.

Deferred after this slice:

- Interactive name and repository conflict recovery.
- User-initiated unlink and explicit re-link flows.
- Incorrect-merge challenge and support recovery.

## Tasks

- [ ] Approve identity matching, provider rules, merge evidence, and privacy contracts.
  - Purpose: Resolve launch allowlist, retention, recovery, transaction, and verification blockers.
  - Proof: Requirements, design, data contracts, and canonical test commands have no unresolved slice blockers.

- [ ] Implement minimum-permission verified-primary GitHub email retrieval.
  - Purpose: Produce one authoritative automatic-match candidate without retaining secondary addresses.
  - Proof: Integration and data-lifecycle tests cover primary, unverified, missing, multiple, secondary, permission, and provider-failure cases.

- [ ] Implement conservative automatic-match canonicalization.
  - Purpose: Apply ASCII eligibility and only approved exact-provider transformations.
  - Proof: Unit and property tests cover whitespace, domain case, local-part case, dot and tag rules, custom domains, Unicode, IDNA, ambiguity, and registry versions.

- [ ] Implement identity candidate resolution and complete merge preflight.
  - Purpose: Detect one valid match and every project-name or repository conflict before mutation.
  - Proof: Tests cover zero, one, multiple, retry, concurrency, name conflict, repository conflict, and unchanged state after abort.

- [ ] Implement atomic conflict-free identity and project consolidation.
  - Purpose: Preserve the passwordless identity and every hosted project exactly once.
  - Proof: Persistence and fault-injection tests prove idempotency, rollback, stable identities, complete data movement, and no partial workspace state.

- [ ] Revoke absorbed-workspace worker credentials after commit.
  - Purpose: Prevent silent transfer of machine trust.
  - Proof: Tests show successful merge revokes old credentials without changing workers or files, while failed merge preserves them.

- [ ] Reduce the absorbed workspace to the approved minimal record.
  - Purpose: Retain only lawful merge evidence with enforced deletion.
  - Proof: Schema, access, retention, rights, deletion, and negative-field tests pass with required privacy or legal approval.

- [ ] Implement disclosure, audit, security, and account-neutral failure behavior.
  - Purpose: Make linking understandable and diagnosable without exposing identities or secrets.
  - Proof: Browser, security, audit, notification, and log reviews pass for success and every failure path.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Provider retrieval and secondary-address non-retention tests pass.
- [ ] Normalization registry, collision, ambiguity, Unicode, and IDNA tests pass.
- [ ] Preflight, idempotency, concurrency, atomicity, and rollback tests pass.
- [ ] Project preservation and worker-pairing tests pass.
- [ ] Merge-record data contract, access, retention, deletion, and privacy review pass.
- [ ] Account-neutral UX, notification, audit, and secret-exposure reviews pass.
- [ ] Build, formatting, lint, static checks, integration tests, and browser scenarios pass.

## Blocked Decisions

- Approve exact launch provider rules and their governance.
- Approve the merge record's purpose, lawful basis, access, shortest retention, deletion, rights behavior, and required review.
- Define incorrect-merge recovery and the explicit re-link rule when GitHub has no verified primary email.
- Approve the unlink-policy data contract and lifecycle before its later slice.
- Select GitHub permissions, identity transaction, locking, idempotency, credential-revocation, notification, and audit mechanisms.
- Define canonical automated, property, integration, concurrency, security, and browser verification commands.

## Progress Log

### 2026-07-23 - Extracted from project onboarding

- Completed: Consolidated the accepted automatic matching, provider normalization, atomic merge, conflict recovery, worker re-pairing, minimal record, unlink, and re-link decisions into one identity specification.
- Remaining: Resolve launch provider rules, privacy approvals, recovery, no-primary re-link behavior, transaction architecture, and verification.
- Failed checks: None; implementation has not started.
- Spec updates: Replaced the prior per-answer history with current requirements, design consequences, active-slice boundaries, and blockers.
