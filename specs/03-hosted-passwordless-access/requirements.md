# Hosted Passwordless Access

## Status

Draft

## Outcome

A user who does not use GitHub can choose hosted project-data storage, verify an email address through a passwordless magic link, and securely create or restore hosted workspace access without managing a password.

## Users

- BA, PO, and PM users who need hosted projects or later collaboration without a GitHub account.
- Developers and contributors using local repositories with hosted SDD project data.

## Primary Workflow

1. A user enters through `Work without GitHub` and selects hosted project-data storage.
2. The product requests an email address and returns an account-neutral acknowledgement.
3. The product sends a short-lived, single-use magic link bound to the current authentication attempt.
4. The user opens the valid link before expiry.
5. The product verifies the email, consumes the link once, and establishes a protected hosted session.
6. The product creates or restores the stable hosted identity and personal workspace.
7. Authorized hosted projects are shown alongside on-device projects available to the current device without uploading or reassigning them.

## In Scope

- Verified email as the non-GitHub hosted identity.
- Passwordless magic-link request, delivery, verification, consumption, resend, abuse protection, and recovery boundaries.
- Hosted session creation, restoration, expiry, revocation, and sign-out.
- Stable hosted identity and personal workspace creation or restoration.
- Account-enumeration resistance.
- Combined presentation of authorized hosted and locally available on-device projects without implicit migration.
- GDPR data contracts for email, authentication events, sessions, delivery processors, logs, support, and security data.

## Out of Scope

- GitHub sign-in and repository discovery, defined in `specs/01-github-project-onboarding/`.
- Local worker and repository validation, defined in `specs/02-local-project-onboarding/`.
- GitHub and passwordless identity merging, defined in `specs/04-github-identity-linking/`.
- Storage migration, retention, and resynchronization, defined in `specs/05-project-storage-lifecycle/`.
- Password-based accounts.
- Collaboration invitations, memberships, roles, or permissions.
- Shared-device isolation beyond the current operating-system boundary.

## Business Rules

- Hosted storage must establish an authorized identity before hosted project data is created or exposed.
- The non-GitHub hosted path uses a verified email and must not require or store a password.
- A magic link must be short-lived, single-use, bound to the intended authentication attempt, and invalid after successful use.
- Magic-link tokens and equivalent secrets must not appear in persisted application data beyond the approved protected representation, client-visible payloads, analytics, or logs.
- Requesting a magic link must return the same user-facing response whether or not the email already has an account.
- Invalid, expired, used, replayed, or mismatched links must not establish a session or expose whether an account exists.
- Resend behavior must not leave multiple uncontrolled valid links; the approved invalidation rule must be enforced.
- Delivery and verification endpoints require approved rate limits and abuse controls without creating account-enumeration signals.
- A successful verification creates or restores one stable hosted identity and personal workspace for the verified email under the approved identity rules.
- Hosted sessions must be protected, revocable, and unavailable to coding-agent processes unless a later specification grants a narrow capability.
- Signing out removes access to hosted projects from the current client.
- On-device projects remain available under the device boundary after authentication and sign-out; authentication must not upload, synchronize, duplicate, reassign, or change their storage mode.
- A combined catalog must identify each project's storage mode and current availability.
- The verified email, authentication events, delivery records, sessions, and security logs are personal data with approved purposes, lawful bases, access, retention, deletion, rights behavior, processors, transfers, and required review.
- Analytics may retain only aggregate genuinely anonymous metrics; email hashes, stable pseudonyms, IP addresses, and linkable delivery or session identifiers are personal data, not anonymous analytics.

## Acceptance Criteria

- Given a non-GitHub user selects hosted storage, when they continue, then email verification is required before hosted data is created or exposed.
- Given any email is submitted, when the request is acknowledged, then the response does not reveal whether an account exists.
- Given a valid unused magic link for the current attempt, when it is opened before expiry, then the email is verified and a protected hosted session is established without a password.
- Given a link is invalid, expired, already used, replayed, or bound to another attempt, when it is opened, then no session or hosted access is created and the response remains account-neutral.
- Given resend is requested, when a new link is issued, then the approved invalidation and rate-limit rules prevent uncontrolled concurrent credentials.
- Given verification succeeds for an existing identity, when the session starts, then the same stable hosted workspace and projects are restored.
- Given verification succeeds for a new identity, when workspace creation completes, then exactly one stable hosted workspace exists.
- Given a signed-in user has on-device projects on the current device, when the catalog loads, then those projects appear with hosted projects without upload, reassignment, duplication, or storage-mode change.
- Given the user signs out, when protected views are revisited, then hosted projects require authentication while on-device projects remain available under the local OS boundary.
- Given a token, delivery, session, or provider failure occurs, when the flow ends, then no secret is exposed and no partial identity or workspace is created.

## Open Questions

- What magic-link lifetime, resend invalidation, attempt lifetime, and retry behavior should apply?
- Which email delivery provider, sender identity, bounce handling, and availability strategy should be used?
- Which request, address, device, and network rate limits prevent abuse without exposing account existence?
- What hosted session lifetime, renewal, revocation, and device-management behavior is required?
- What recovery path applies when the user loses access to the verified email?
- How are email changes verified without enabling account takeover or breaking later identity linking?
- How are combined catalog entries deduplicated without linking accountless and hosted identities implicitly?
- Which GDPR roles, purposes, lawful bases, retention, rights workflows, processors, transfers, impact reviews, and security controls apply?
- Which implementation and verification technologies satisfy this feature?
