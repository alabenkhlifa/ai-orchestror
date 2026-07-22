# Hosted Passwordless Access Tasks

## Status

Blocked

## Active Slice

Deliver passwordless hosted sign-in from magic-link request through verified session and stable workspace restoration, with account-neutral failure behavior.

## Implementation Boundary

Included:

- Magic-link request, delivery, verification, and single-use consumption.
- Stable hosted identity and workspace creation or restoration.
- Protected session establishment and sign-out.
- Enumeration resistance, abuse controls, audit, and security logging.
- GDPR data contracts for the introduced processing.
- Browser and automated proof for success and failure paths.

Excluded:

- GitHub identity linking, local worker implementation, storage migration, portability, and collaboration.
- Password authentication and unrelated account-management features.

Deferred after this slice:

- Combined catalog integration beyond the interfaces needed for hosted session restoration.
- Email change and account recovery beyond the approved minimum needed for release.

## Tasks

- [ ] Define the approved passwordless authentication and session contracts.
  - Purpose: Resolve token, attempt, delivery, abuse, session, recovery, and privacy behavior before coding.
  - Proof: Requirements, design, data contracts, schemas, failure states, and test commands are approved with no blocking questions.

- [ ] Implement account-neutral magic-link requests and delivery.
  - Purpose: Send a one-time credential without exposing account existence or secrets.
  - Proof: Integration and security tests cover new and existing emails, provider failure, rate limits, redaction, and equivalent responses.

- [ ] Implement atomic magic-link verification and consumption.
  - Purpose: Establish identity only from a valid attempt-bound unused token.
  - Proof: Tests cover success, expiry, replay, mismatch, tampering, concurrency, and no partial identity creation.

- [ ] Create or restore stable hosted identity and workspace.
  - Purpose: Give the verified user one durable hosted ownership boundary.
  - Proof: Tests cover new identity, restoration, retry, concurrency, and cross-user isolation.

- [ ] Implement protected hosted sessions and sign-out.
  - Purpose: Authorize hosted access independently from token delivery and coding agents.
  - Proof: Session tests cover restoration, expiry, renewal, revocation, sign-out, and rejected access.

- [ ] Build passwordless authentication UX and recovery states.
  - Purpose: Make success, waiting, resend, expiry, and failure actionable for non-technical users.
  - Proof: Desktop and mobile browser scenarios cover the complete flow without account disclosure.

- [ ] Enforce the feature GDPR data contract and security review.
  - Purpose: Govern email, tokens, sessions, logs, processors, retention, rights, and allowed anonymous metrics.
  - Proof: Lifecycle, access, redaction, deletion, processor, transfer, and anonymisation checks pass with required review recorded.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Request, delivery, verification, replay, concurrency, and session tests pass.
- [ ] Account-enumeration and abuse-control review passes.
- [ ] Token, credential, client-payload, analytics, and log exposure review passes.
- [ ] Required desktop and mobile browser scenarios pass.
- [ ] GDPR data contract, retention, rights, processor, transfer, and privacy-review gates are complete.
- [ ] Build, formatting, lint, static checks, and failure diagnostics pass.

## Blocked Decisions

- Define magic-link lifetime, resend invalidation, protected storage, attempt binding, and consumption behavior.
- Select email delivery, sender, bounce, availability, and processor strategy.
- Define account-neutral abuse controls and rate limits.
- Define hosted session, device, sign-out, renewal, and revocation behavior.
- Define release-blocking recovery and email-change behavior.
- Approve the GDPR data contract, retention, rights, processor, transfer, anonymisation, and review decisions.
- Select implementation architecture and canonical verification commands.

## Progress Log

### 2026-07-23 - Extracted from project onboarding

- Completed: Isolated the accepted verified-email, passwordless magic-link, account-neutral response, hosted-session, and combined-catalog boundaries.
- Remaining: Resolve token, delivery, abuse, session, recovery, privacy, architecture, and verification decisions.
- Failed checks: None; implementation has not started.
- Spec updates: Created a focused hosted passwordless access specification without changing accepted behavior.
