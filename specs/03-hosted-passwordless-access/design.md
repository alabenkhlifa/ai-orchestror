# Hosted Passwordless Access Design

## Context

Hosted project data requires a recoverable authorization boundary for users who do not use GitHub. Passwordless email access avoids a second password system but creates token-delivery, replay, enumeration, session, recovery, and privacy responsibilities.

## Proposed Approach

Explain the verified-email access and recovery boundary, accept an email through an account-neutral endpoint, create a protected authentication attempt, deliver a short-lived single-use token, consume it exactly once for the intended attempt, and establish an independently revocable hosted device session for one stable identity and workspace. Preserve valid sessions across browser restarts, support multiple devices, and provide current-device, individual-session, and all-session revocation. A sign-in method linked before email access is lost may restore the same identity, but it cannot change the verified email. Compose hosted and local catalog references without changing local ownership or storage.

Exact token format, delivery provider, storage representation, and session mechanism remain deferred.

## Components Affected

- Hosted-storage authentication entry.
- Magic-link request, delivery, verification, resend, and recovery surfaces.
- Hosted identity and personal workspace service.
- Protected session and sign-out behavior.
- Active-device session management.
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
- Each device session is independently revocable and may coexist with other sessions for the same hosted identity.
- Browser restart does not end a valid session; sign-out, explicit revocation, and approved security expiration do.
- Active-session device details are personal data and require an approved minimum-field, access, retention, deletion, and rights contract.
- A sign-in method linked before email loss may authenticate the same hosted identity but does not authorize verified-email replacement.
- Without proof of the verified email or another previously linked sign-in method, neither self-service nor support can bypass the authentication boundary in the first release.
- Device project references can be composed into the catalog but are not attached to the hosted identity or copied to hosted storage.
- Catalog composition uses stable project identity, not repository similarity, to distinguish one migrated or resynchronized project from separate projects linked to the same repository.
- Delivery providers and logs are included in the personal-data processing and retention inventory.

## Interfaces

- Magic-link request interface: accept an email, create a protected attempt, apply abuse controls, and return an account-neutral acknowledgement.
- Delivery interface: send the one-time link through an approved processor without exposing token secrets to unrelated systems.
- Verification interface: validate attempt binding, expiry, single use, and integrity before consuming the token atomically.
- Hosted identity interface: create or restore the stable passwordless identity and workspace.
- Session interface: establish and restore a persistent device session, enforce approved expiry, revoke the current session on normal sign-out, and deny expired or revoked sessions before exposing hosted data.
- Session-management interface: list active device sessions and revoke one session or all sessions without affecting on-device projects.
- Catalog interface: combine authorized hosted and locally available device projects, preserve separate project identities even when repositories match, and show one authoritative entry for an explicitly migrated or resynchronized stable project.
- Lost-email access interface: restore the same hosted identity through a sign-in method linked before the loss, or fail without a support override when none exists.
- Future verified-email change interface: require fresh proof of the current email and verification of the new email; do not accept an existing session or another linked method as a substitute.

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

- Choice: Show authorized hosted and current-device projects together after authentication without changing either boundary. Keep different stable projects separate even when they share a repository, and show an explicitly migrated or resynchronized stable project once with its authoritative storage mode.
- Reason: Users need one working catalog while retaining deliberate storage choices.
- Consequence: Catalog composition uses stable project identity and cannot be treated as identity merge, migration, or synchronization. Every entry shows storage mode and current availability; exact labels and visual grouping remain a design decision.

### Pre-Linked Sign-In Recovery Only

- Choice: After verified-email access is lost, allow account access only through another sign-in method linked to the same identity before the loss. Do not provide a first-release support override.
- Reason: A newly asserted recovery identity would create an account-takeover path without an approved proof model.
- Consequence: The first hosted-access slice must explain the limitation and restore the same workspace through a valid pre-linked method without changing the verified email.

### Two-Proof Email Change After The First Slice

- Choice: Defer verified-email change UI and require future changes to prove the current email and verify the new email.
- Reason: An existing session or linked provider may be compromised and must not replace independent control of the current email.
- Consequence: Linked-provider access preserves account use but cannot change the email. A future recovery method for users who cannot prove the current email requires a separate specification update.

### Persistent Independent Device Sessions

- Choice: Keep valid sessions across browser restarts and allow independent sessions on multiple devices.
- Reason: Requiring a new magic link after every browser restart would make normal use unnecessarily disruptive.
- Consequence: Every session needs independent protection, expiry, visibility, and revocation. Exact lifetimes and renewal mechanisms remain technical decisions.

### Current-Device And All-Device Sign-Out

- Choice: Normal sign-out revokes only the current device session. Account settings allow revoking one active session or selecting `Sign out all devices`.
- Reason: Users need predictable daily sign-out and a separate recovery action for lost or unknown devices.
- Consequence: Session management must clearly identify the affected scope, revoke atomically, and leave on-device projects unchanged.

## Risks

- Magic links can be stolen, replayed, leaked through referrers, or logged. Use protected token storage, short lifetime, single-use atomic consumption, and surface reviews.
- Request endpoints can enumerate accounts or send unwanted email. Keep responses account-neutral and apply approved abuse controls.
- Email compromise can grant hosted access. Define session visibility, revocation, notifications, and recovery safeguards.
- A session, linked provider, or support process could be misused to replace the verified email. Enforce the two-proof boundary and provide no first-release override.
- Users can permanently lose access if they lose their only sign-in method. Explain that limitation before hosted account creation without implying unavailable recovery.
- Persistent sessions increase exposure when a device is lost or shared. Make active sessions visible and independently revocable, and enforce the approved security expiration.
- Device descriptions can be inaccurate or reveal excessive personal data. Treat them as hints and approve only the minimum fields needed for recognition and revocation.
- Delivery outages can block access. Define provider failure behavior and recovery without weakening verification.
- Long-lived authentication records can exceed their purpose. Apply field-level retention and deletion across primary and derived storage and processors.
- Catalog composition can accidentally upload local projects. Enforce explicit ownership and storage boundaries in service and integration tests.
- Repository-based deduplication can hide an independent project or imply an unsafe merge. Use stable project identity and preserve separate entries when identities differ.

## Open Questions

- Technical design: Which token generation, protected storage, expiry, resend, and single-use mechanism is approved?
- Technical design: Which delivery provider and processor contract is acceptable?
- Technical design: Which abuse controls and rate limits preserve account-neutral behavior?
- Technical design: Which session lifetime, inactivity limit, renewal, protected storage, device-identification, and revocation mechanisms satisfy the approved observable behavior?
- Technical design: How does hosted access integrate a pre-linked sign-in method without allowing it, an existing session, or support to authorize verified-email changes?
- Technical design: How does catalog composition prove stable project identity and present separate same-repository projects clearly without implicit identity or storage mutation?
- Active-slice implementation: Which GDPR data contract and privacy review apply to email, delivery, authentication, device-session details, logs, and support?
- Technical design: Which application architecture implements the approved authentication and session boundaries?
- Required verification: Which automated, integration, security, and browser tests form the verification gate?
