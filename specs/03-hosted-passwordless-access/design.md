# Hosted Passwordless Access Design

## Context

Hosted project data requires a recoverable authorization boundary for users who do not use GitHub. Passwordless email access avoids a second password system but creates token-delivery, replay, enumeration, session, recovery, and privacy responsibilities.

## Proposed Approach

Accept an email through an account-neutral endpoint, create a protected authentication attempt, deliver a short-lived single-use token, consume it exactly once for the intended attempt, and establish a protected hosted session for one stable identity and workspace. Compose hosted and local catalog references without changing local ownership or storage.

Exact token format, delivery provider, storage representation, and session mechanism remain deferred.

## Components Affected

- Hosted-storage authentication entry.
- Magic-link request, delivery, verification, resend, and recovery surfaces.
- Hosted identity and personal workspace service.
- Protected session and sign-out behavior.
- Email delivery integration and abuse controls.
- Combined project catalog.
- Audit, security logs, privacy governance, and data-subject-rights workflows.

## Data and Access Boundaries

- `HostedIdentity`: the stable passwordless identity for one verified email boundary.
- `ExternalIdentity`: the verified email sign-in method attached to that stable identity.
- `MagicLinkAttempt`: short-lived attempt state with a protected token representation, intended email, expiry, consumption state, and approved diagnostic metadata.
- `HostedSession`: revocable authorization to hosted workspace data.
- `PersonalWorkspace`: the hosted ownership boundary restored after authentication.

Required boundaries:

- No hosted data is exposed before successful verification and session establishment.
- Token secrets remain inside the accepted credential boundary and are never available to analytics or ordinary logs.
- Request and failure responses are account-neutral.
- Verification consumption is atomic and replay-safe.
- Sessions are separated from coding-agent credentials and capabilities.
- Device project references can be composed into the catalog but are not attached to the hosted identity or copied to hosted storage.
- Delivery providers and logs are included in the personal-data processing and retention inventory.

## Interfaces

- Magic-link request interface: accept an email, create a protected attempt, apply abuse controls, and return an account-neutral acknowledgement.
- Delivery interface: send the one-time link through an approved processor without exposing token secrets to unrelated systems.
- Verification interface: validate attempt binding, expiry, single use, and integrity before consuming the token atomically.
- Hosted identity interface: create or restore the stable passwordless identity and workspace.
- Session interface: establish, restore, renew, revoke, and end hosted authorization.
- Catalog interface: combine authorized hosted and locally available device projects while preserving ownership and storage boundaries.
- Recovery interface: restore access through an approved identity-verified process once defined.

## Decisions and Tradeoffs

### Passwordless Verified Email

- Choice: Use a verified email and magic link for non-GitHub hosted access.
- Reason: Users can access hosted projects without a GitHub account or another password.
- Consequence: Email delivery becomes an authentication dependency and requires explicit token, abuse, session, recovery, and privacy controls.

### Account-Neutral Responses

- Choice: Return the same acknowledgement and safe failure shape regardless of account existence.
- Reason: Authentication must not become an account-enumeration interface.
- Consequence: Diagnostics must remain useful internally without leaking identity state to the requester.

### Combined Catalog Without Implicit Upload

- Choice: Show authorized hosted and current-device projects together after authentication without changing either boundary.
- Reason: Users need one working catalog while retaining deliberate storage choices.
- Consequence: Catalog composition cannot be treated as identity merge, migration, or synchronization.

## Risks

- Magic links can be stolen, replayed, leaked through referrers, or logged. Use protected token storage, short lifetime, single-use atomic consumption, and surface reviews.
- Request endpoints can enumerate accounts or send unwanted email. Keep responses account-neutral and apply approved abuse controls.
- Email compromise can grant hosted access. Define session visibility, revocation, notifications, and recovery safeguards.
- Delivery outages can block access. Define provider failure behavior and recovery without weakening verification.
- Long-lived authentication records can exceed their purpose. Apply field-level retention and deletion across primary and derived storage and processors.
- Catalog composition can accidentally upload local projects. Enforce explicit ownership and storage boundaries in service and integration tests.

## Open Questions

- Which token generation, protected storage, expiry, resend, and single-use mechanism is approved?
- Which delivery provider and processor contract is acceptable?
- Which abuse controls and rate limits preserve account-neutral behavior?
- Which session architecture, lifetime, renewal, revocation, and device controls are required?
- Which recovery and verified-email-change flow prevents account takeover?
- How is combined catalog composition implemented without implicit identity or storage mutation?
- Which GDPR data contract and privacy review apply to email, delivery, authentication, sessions, logs, and support?
- Which automated, integration, security, and browser tests form the verification gate?
