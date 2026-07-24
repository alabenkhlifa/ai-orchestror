# GitHub Identity Linking Tasks

## Status

Blocked

## Active Slice

Deliver conservative automatic candidate detection, fresh proof of both sign-in methods, explicit confirmation, and a conflict-free atomic merge into the existing passwordless workspace, while safely aborting every ineligible, ambiguous, unproven, unconfirmed, or conflicting case without mutation.

## Implementation Boundary

Included:

- Verified-primary retrieval and secondary-address non-retention.
- ASCII eligibility and approved automatic-match normalization.
- Zero-or-one candidate resolution and collision safety.
- Fresh proof of both sign-in methods and explicit initial-link confirmation.
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
- Confirmed-merge challenge and support recovery.

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
  - Purpose: Detect one valid candidate without account disclosure and identify every project-name or repository conflict before mutation.
  - Proof: Tests cover zero, one, multiple, retry, concurrency, name conflict, repository conflict, candidate secrecy, and unchanged state after abort.

- [ ] Implement fresh two-method proof and explicit initial-link confirmation.
  - Purpose: Prevent an email match from authorizing an irreversible account merge.
  - Proof: Security and browser tests cover successful proof, invalid, expired, mismatched, replayed, cancelled, and unconfirmed attempts; only a freshly proven and explicitly confirmed attempt may reach commit.

- [ ] Implement atomic conflict-free identity and project consolidation.
  - Purpose: Preserve the passwordless identity and every hosted project exactly once.
  - Proof: Persistence and fault-injection tests prove confirmation binding, idempotency, rollback, stable identities, complete data movement, GitHub sign-in to the surviving workspace, and no partial workspace state.

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
- [ ] Candidate secrecy, fresh two-method proof, explicit confirmation, cancellation, expiry, mismatch, and replay tests pass.
- [ ] Preflight, idempotency, concurrency, atomicity, and rollback tests pass.
- [ ] Project preservation and worker-pairing tests pass.
- [ ] Linked-GitHub access restores only the surviving workspace and cannot authorize verified-email change, unlinking, or re-linking alone.
- [ ] Merge-record data contract, access, retention, deletion, and privacy review pass.
- [ ] Account-neutral UX, notification, audit, and secret-exposure reviews pass.
- [ ] Build, formatting, lint, static checks, integration tests, and browser scenarios pass.

## Blocked Decisions

- Technical design: Approve exact launch provider rules and their governance.
- Active-slice implementation: Approve the merge record's purpose, lawful basis, access, shortest retention, deletion, rights behavior, and required review.
- Product requirements: Define recovery when a user challenges a merge they explicitly confirmed.
- Product requirements: Define the explicit re-link rule when GitHub has no verified primary email.
- Active-slice implementation: Approve the unlink-policy data contract and lifecycle before its later slice.
- Technical design: Select GitHub permissions, candidate expiry, proof binding, identity transaction, locking, idempotency, credential-revocation, notification, and audit mechanisms.
- Required verification: Define canonical automated, property, integration, concurrency, security, and browser commands.

## Progress Log

### 2026-07-23 - Extracted from project onboarding

- Completed: Kept automatic matching as non-mutating candidate detection and required fresh proof of both sign-in methods, complete preflight, and explicit confirmation before the initial atomic merge.
- Remaining: Resolve confirmed-merge recovery, no-primary re-link behavior, launch provider rules, privacy approvals, transaction architecture, and verification.
- Failed checks: None; implementation has not started.
- Spec updates: Replaced automatic merge with explicit proven linking across workflow, boundaries, proof, tasks, and blockers while preserving the minimal post-merge record.
