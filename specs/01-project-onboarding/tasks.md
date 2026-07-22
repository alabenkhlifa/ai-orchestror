# Project Onboarding Tasks

## Status

Blocked

## Active Slice

The current candidate slice delivers the GitHub onboarding path end to end: a user signs in with GitHub, enters a personal workspace, sees all repositories available under their granted access, links one unlinked repository, and lands on the created project. Approval remains blocked until storage selection, the complete local entry path, and portability are assigned to this slice or explicitly deferred. Collaboration is deferred to a separate specification.

## Implementation Boundary

Included:

- Application bootstrap required for this slice after the technology decisions are approved.
- GitHub sign-in, session restoration, and sign-out.
- Personal workspace creation and restoration.
- GitHub repository catalog retrieval, search, loading, empty, and failure states.
- Project and repository-connection creation with the one-to-one repository rule and user-scoped project-name allocation.
- Case-insensitive project-name validation, editing during onboarding, and renaming after creation.
- A project summary showing the linked GitHub repository and connection status.
- Persistent project visibility with a disconnected status when GitHub access is lost.
- GDPR data contracts, privacy-preserving defaults, retention and rights behavior, anonymous analytics boundaries, and security controls for every schema and backend path introduced by this slice.
- Automated and browser-level proof for the active acceptance criteria.
- Security checks for session and GitHub credential exposure within this slice.

Excluded:

- The `Work without GitHub` entry surface, storage-mode selection, passwordless email identity for hosted data, automatic verified-email GitHub linking, explicit unlinking and re-linking, local worker installation, pairing, and local repository linking pending the slice-boundary decision.
- Project export, import, direct storage migration, hosted retention cleanup, and resynchronization pending lifecycle and slice-boundary decisions.
- Live collaboration, invitations, memberships, roles, permissions, and identity-merge membership reconciliation; these are deferred to a separate collaboration specification.
- Automatic identity matching for non-ASCII email addresses or domains containing an `xn--` label; this remains beyond the first release even when verified-email identity linking enters a later slice.
- User-initiated project deletion unrelated to storage migration, unlinking, and sharing.
- Team workspaces and collaboration.
- AI-provider setup, specification workflows, and agent execution.
- Remote workers, cloud workers, and Raspberry Pi deployment.
- Any Symphony orchestration behavior not required to complete onboarding.

## Tasks

- [ ] Establish the approved application skeleton and canonical development checks.
  - Purpose: Provide only the runtime, UI, persistence, configuration, and test foundations required by this slice.
  - Proof: The documented setup, build, static checks, and empty test suite succeed from a clean checkout.

- [ ] Implement GitHub-backed identity and session behavior.
  - Purpose: Let a user sign in, restore access, and sign out without exposing authentication credentials.
  - Proof: Automated authentication tests and a browser scenario cover successful sign-in, restored session, rejected access after sign-out, cancellation, and provider failure.

- [ ] Create and restore the user's personal workspace.
  - Purpose: Establish the ownership boundary for all projects and repository connections.
  - Proof: Automated tests show one workspace per user, stable restoration across sessions, and isolation between different users.

- [ ] Implement the GitHub repository catalog.
  - Purpose: Let non-technical users find any repository returned under their granted GitHub access without entering a URL.
  - Proof: Integration tests cover pagination, search, empty results, private and organization repositories when returned by GitHub, authorization failure, and rate-limit or provider failure.

- [ ] Implement atomic project and repository linking.
  - Purpose: Create one project for one selected repository while preventing duplicate links, duplicate user-scoped names, or partial records.
  - Proof: Domain and persistence tests cover the repository-name default, case-insensitive lowest-available numeric suffixes, reuse by different users, concurrent naming and repository conflicts, provider identity normalization, rollback on failure, and workspace ownership enforcement.

- [ ] Implement project display-name management.
  - Purpose: Let the user edit the generated name during onboarding and rename a project later without changing project or repository identity.
  - Proof: Automated and browser tests cover successful edits, case-insensitive conflicts, concurrent renames, unchanged stable identities, and actionable conflict messages.

- [ ] Preserve projects when GitHub access is lost.
  - Purpose: Keep project context visible while representing repository access as a recoverable connection state.
  - Proof: Integration and browser tests show that an inaccessible repository changes to disconnected, remains visible, exposes no stale credentials, and can return to connected when access is restored.

- [ ] Build the GitHub onboarding and project-summary experience.
  - Purpose: Provide a guided path usable by a BA, PO, PM, or developer without requiring repository URLs or terminal commands.
  - Proof: Browser verification covers sign-in, repository search and selection, confirmation, duplicate prevention, actionable failures, and the resulting project summary at supported desktop and mobile sizes.

- [ ] Define and enforce the slice's GDPR data contract.
  - Purpose: Make privacy, lawful processing, data minimization, retention, rights handling, anonymisation, processor boundaries, and security part of the schema and backend design rather than a release-time review.
  - Proof: The processing inventory maps every personal-data field and processing path to its approved purpose, lawful basis, access, retention, deletion, rights behavior, processors, and transfers; schema and service tests enforce those rules; analytics tests reject identifiers and linkable data; required privacy or legal review is recorded.

- [ ] Complete the slice security and observability review.
  - Purpose: Ensure credentials do not leak and failures can be diagnosed without exposing secrets.
  - Proof: Logs and client-visible payloads contain no session or GitHub secrets, security-focused tests pass, and failed onboarding attempts leave no partial project or repository connection.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Authentication, workspace, repository catalog, project-linking, naming, and connection-state automated tests pass.
- [ ] GitHub integration tests pass against the approved test strategy.
- [ ] Build, formatting, lint, and type or static checks pass.
- [ ] Required desktop and mobile browser scenarios pass.
- [ ] Credential and session exposure review passes.
- [ ] GDPR processing inventory, data contracts, retention rules, data-subject-rights paths, processor boundaries, and required privacy or legal review are complete for this slice.
- [ ] Analytics retained by this slice pass documented anonymisation checks for singling out, linkability, and inference; pseudonymised data is handled as personal data.
- [ ] Schema, service, integration, and lifecycle tests prove privacy defaults, least privilege, retention enforcement, deletion propagation, export boundaries, and applicable rights behavior.
- [ ] Failure-path logs are sufficient and contain no secrets.
- [ ] New product and technical decisions are written back to the specification.
- [ ] The approved boundary for the two entry paths is reflected in the entry surface and deferred work.

## Blocked Decisions

- Select the application runtime, UI approach, persistence system, and deployment model.
- Decide how the Symphony foundation participates in the first application architecture.
- Select and configure the GitHub integration model and required permissions.
- Define session, GitHub credential, and application-secret storage and revocation.
- Define the test strategy and canonical build, format, lint, static-check, and browser commands.
- Define atomic direct storage migration, active-copy authority, failure recovery, and stable identity across modes.
- Define complete hosted soft-delete and two-year cleanup propagation across project records, derived data, logs, caches, indexes, backups, exports, and processors; enforce exclusion from normal reads and resynchronization-only authorization; separate anonymous analytics and minimal legally required records under independent lifecycles.
- Define incremental resynchronization versions, change and deletion detection, conflicts, compatibility, and full-upload rehydration after cleanup while preserving stable identity.
- Define controller and processor roles, processing purposes and lawful bases, personal-data categories, data-subject-rights workflows, retention schedules, deletion exceptions, subprocessors, international transfers, breach handling, and required impact or legal reviews.
- Define anonymous analytics metrics, aggregation thresholds, disclosure-risk tests, retention periods, and the technical boundary that prevents re-identification or linkage.
- Define passwordless email delivery, magic-link generation and protected storage, attempt binding, lifetime, single-use consumption, resend invalidation, enumeration resistance, rate limits, hosted session lifetime, recovery, and GDPR lifecycle behavior.
- Define export contents, package compatibility and integrity, secret exclusion, import conflicts, and repository reconnection.
- Define verified-primary GitHub email retrieval with minimum permission and no secondary-email retention, implementation of the approved whitespace, domain-case, and local-part-case base normalization, implementation of the ASCII-only matching eligibility check and internationalized-address skip, exact-domain and account-type launch entries for independently approved case folding, dot removal, and `+tag` stripping, collision-safe matching and allowlist governance, automatic GitHub and passwordless identity linking, implementation of the approved stable passwordless workspace, all-project preservation and atomic conflict preflight, user-confirmed name and repository recovery, post-commit worker-pairing revocation and explicit re-pairing, immediate reduction to the approved minimal absorbed-workspace merge record, its lawful basis and shortest retention, user disclosure, implementation of the approved fresh-passwordless-proof GitHub unlink with credential revocation and repository disconnection, implementation of explicit re-link suppression, dual authentication, differing-email confirmation, conflict preflight, and repository revalidation, incorrect-merge recovery, the explicit re-link rule when GitHub has no verified primary email, the unlink-policy data contract and lifecycle, and a combined catalog that never uploads or reassigns on-device projects implicitly.
- Decide whether the GitHub path, local path, storage choice, and portability ship together or as approved consecutive slices without exposing non-functional actions.

## Progress Log

### 2026-07-22

- Completed: Captured the first product-onboarding requirements, logical design, first executable slice, and technology-selection gate.
- Remaining: Review the product questions, select technologies, update the design, and approve the slice before implementation.
- Failed checks: None; implementation has not started.
- Spec updates: Created the initial project-onboarding specification from the user discovery conversation.

### 2026-07-22 - Project naming decision

- Completed: Defined repository-derived project names, user-scoped uniqueness, cross-user reuse, and lowest-available numeric suffix allocation.
- Remaining: Resolve whether names are editable, whether uniqueness ignores letter case, and how inaccessible linked GitHub repositories appear.
- Failed checks: None; implementation has not started.
- Spec updates: Aligned requirements, design boundaries, implementation proof, and blocked decisions through `update-spec`.

### 2026-07-22 - Entry, naming, and disconnected repository decisions

- Completed: Defined the two entry-page actions, GitHub-free local path, editable project names, case-insensitive name uniqueness, and persistent visibility for disconnected GitHub repositories.
- Remaining: Define local workspace identity and persistence, decide later GitHub attachment behavior, settle the entry-path slice boundary, select technologies, and approve the active slice.
- Failed checks: None; implementation has not started.
- Spec updates: Replaced GitHub-only entry assumptions, removed the resolved naming and access questions, added acceptance proof, and recorded the newly exposed local identity decisions through `update-spec`.

### 2026-07-22 - Storage choice and project portability

- Completed: Defined user-selected on-device or hosted project-data storage, accountless device storage, hosted storage as the collaboration-capable path, and project export and import.
- Remaining: Decide the storage-selection scope, non-GitHub hosted identity, movement between modes, package contents and conflicts, executable-slice boundary, and technologies.
- Failed checks: None; implementation has not started.
- Spec updates: Replaced the single local-workspace assumption with explicit storage modes, added portability and security requirements, and recorded the newly exposed identity, collaboration, and package decisions through `update-spec`.

### 2026-07-22 - Per-project storage mode

- Completed: Defined storage mode as a per-project choice and allowed one user to have on-device and hosted projects at the same time.
- Remaining: Decide whether GitHub-linked projects have the same storage choice, how projects move between modes, and the other hosted identity, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated workflow, business rules, acceptance proof, logical ownership, tradeoffs, and blockers through `update-spec`.

### 2026-07-22 - Storage independent from repository source

- Completed: Allowed both GitHub-linked and local-repository projects to select either on-device or hosted project-data storage.
- Remaining: Decide how existing projects move between modes and resolve the hosted identity, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated both onboarding paths, storage rules, acceptance proof, design consequences, open questions, and blockers through `update-spec`.

### 2026-07-22 - Direct storage migration and hosted retention

- Completed: Defined direct storage-mode changes, hosted soft deletion when moving on-device, two-year hosted data cleanup with an analytics exception, and incremental resynchronization from the latest retained hosted version.
- Remaining: Define the deleted data inventory, analytics retention, visibility and recovery during retention, synchronization conflicts and versions, post-cleanup behavior, and the other identity, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Added lifecycle rules, acceptance proof, logical records, interfaces, tradeoffs, risks, blockers, and deferred implementation work through `update-spec`.

### 2026-07-22 - GDPR and anonymous analytics

- Completed: Made GDPR a project-wide schema and backend constraint and limited retained analytics to genuinely anonymous aggregate data with no user, project, workspace, repository, device, network, or content identifiers.
- Remaining: Define the processing inventory, controller and processor roles, lawful bases, rights workflows, category-specific retention, processors and transfers, impact reviews, anonymous metrics, aggregation thresholds, and the other lifecycle, identity, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Added GDPR business rules, acceptance proof, data boundaries, interfaces, design decisions, risks, verification gates, blockers, and official EU references through `update-spec`.

### 2026-07-22 - Resynchronization after baseline cleanup

- Completed: Defined a full upload after the two-year hosted baseline is permanently cleaned up while preserving stable project identity and the repository connection.
- Remaining: Define incremental synchronization conflicts and compatibility, retained-copy visibility and recovery, and the other GDPR, identity, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated lifecycle rules, acceptance proof, data boundaries, resynchronization interfaces, tradeoffs, open questions, and blockers through `update-spec`.

### 2026-07-22 - Soft-deleted hosted copy visibility

- Completed: Hid retained hosted copies from normal project lists, search, collaboration views, and ordinary APIs and limited access to explicit authorized resynchronization from the active on-device project.
- Remaining: Define the deleted data inventory, lifecycle audit behavior, synchronization conflicts and compatibility, and the other GDPR, identity, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated access rules, acceptance proof, retention interfaces, design consequences, open questions, and blockers through `update-spec`.

### 2026-07-22 - Complete hosted project-data cleanup

- Completed: Applied permanent cleanup to every project-scoped hosted record and derived copy, with exceptions only for genuinely anonymous analytics and minimal records explicitly required by law.
- Remaining: Define legal-retention records and deadlines, lifecycle audit behavior, synchronization conflicts and compatibility, and the other GDPR, identity, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated cleanup scope, acceptance proof, logical records, data boundaries, retention tradeoffs, open questions, and blockers through `update-spec`.

### 2026-07-22 - Passwordless hosted email identity

- Completed: Selected verified email and passwordless magic links for users who enter without GitHub and choose hosted storage, while keeping on-device storage accountless.
- Remaining: Define magic-link timing, resend, delivery, rate limits, sessions, recovery, GitHub account linking, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated the workflow, identity rules, acceptance proof, logical identity, interfaces, security tradeoffs, open questions, deferred boundary, and blockers through `update-spec`.

### 2026-07-22 - Automatic verified-email identity merge

- Completed: Automatically linked GitHub and passwordless-email identities when GitHub's verified primary email matches the verified passwordless email, while preserving one stable hosted user identity and excluding accountless device boundaries from automatic merge or upload.
- Remaining: Approve the alias-normalization launch allowlist and allowlist governance; approve the absorbed-workspace merge record's lawful basis and shortest retention; define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, authenticated presentation of accountless projects, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated identity workflow, business rules, acceptance proof, logical records, interfaces, tradeoffs, risks, open questions, and blockers through `update-spec`.

### 2026-07-22 - Combined local and hosted project catalog

- Completed: Kept accountless projects on-device after authentication and showed them alongside authorized hosted projects without implicit upload, synchronization, reassignment, or storage-mode changes.
- Remaining: Define catalog deduplication, incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated workflow, catalog behavior, sign-out behavior, acceptance proof, data boundaries, interfaces, tradeoffs, risks, open questions, and blockers through `update-spec`.

### 2026-07-22 - Shared-device boundary

- Completed: Placed on-device project access under the operating-system user profile and filesystem permission boundary and excluded additional shared-device or local-profile isolation from the product.
- Remaining: Approve the absorbed-workspace merge record's lawful basis and shortest retention, define catalog deduplication, incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated scope, access rules, design boundaries, tradeoffs, risks, open questions, and blockers through `update-spec`.

### 2026-07-22 - Non-destructive hosted project merge

- Completed: Required an automatic identity merge to retain every hosted project from both identities, preflight the complete project set, and commit atomically only when the resulting workspace has no case-insensitive project-name or repository conflict.
- Remaining: Approve the absorbed-workspace merge record's lawful basis and shortest retention, define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated the identity workflow, business rules, acceptance proof, data boundaries, interface, tradeoff, risk, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - User-confirmed merge name resolution

- Completed: Required merge-time project-name conflicts to suggest the lowest available numeric suffix, remain non-mutating until user confirmation, and apply the confirmed rename only inside a freshly preflighted atomic merge.
- Remaining: Approve the absorbed-workspace merge record's lawful basis and shortest retention, define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated merge recovery behavior, acceptance proof, identity data, access boundaries, interface, tradeoff, risk, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - User-confirmed merge repository resolution

- Completed: Required a repository conflict to remain non-mutating until the user chooses which project keeps the repository and selects a different authorized, valid, unlinked repository for the other project, with both choices applied only inside a freshly preflighted atomic merge.
- Remaining: Approve the absorbed-workspace merge record's lawful basis and shortest retention, define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated merge recovery scope, business rules, acceptance proof, identity data, access boundaries, interface, tradeoff, risk, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - Stable passwordless workspace merge target

- Completed: Made the existing passwordless personal workspace the surviving workspace and required every GitHub-backed hosted project to move into it only inside the successful atomic merge while preserving project identity and data.
- Remaining: Approve the absorbed-workspace merge record's lawful basis and shortest retention, define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated merge workflow, scope, workspace ownership rules, acceptance proof, logical identity, access boundaries, interface, tradeoff, risk, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - Collaboration membership deferral

- Completed: Deferred invitations, memberships, roles, permissions, and identity-merge membership reconciliation to a separate collaboration specification and excluded membership behavior from onboarding and its current slice.
- Remaining: Approve the absorbed-workspace merge record's lawful basis and shortest retention, define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated onboarding scope, identity-merge boundaries, acceptance proof, design consequences, open questions, active-slice boundary, blockers, and progress through `update-spec`.

### 2026-07-22 - Worker re-pairing after identity merge

- Completed: Required a successful identity merge to revoke absorbed-workspace pairing credentials without uninstalling workers or changing local files, then require explicit re-pairing with new credentials for the surviving workspace; failed merges leave pairings unchanged.
- Remaining: Approve the absorbed-workspace merge record's lawful basis and shortest retention, define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated scope, worker and workspace rules, acceptance proof, logical worker identity, access boundaries, pairing interface, tradeoff, risk, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - Minimal absorbed-workspace merge record

- Completed: Required the absorbed workspace to be reduced immediately after commit to an inaccessible record containing only source and surviving workspace IDs, merge event ID, status, completion time, and deletion deadline, with all workspace content and secrets excluded.
- Remaining: Obtain privacy or legal approval for the record's lawful basis and shortest necessary retention, then define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, the unlink-policy data contract and lifecycle, and the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated cleanup scope, business rules, acceptance proof, logical records, access boundaries, identity interface, tradeoff, risk, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - Verified primary GitHub email matching

- Completed: Limited automatic identity matching to one GitHub email marked both primary and verified, excluded every secondary address from matching and retention, and made missing, unverified, non-matching, or ambiguous primary results skip automatic merging.
- Remaining: Approve the alias-normalization launch allowlist and allowlist governance; obtain privacy or legal approval for the merge record's lawful basis and retention; define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, and the unlink-policy data contract and lifecycle; and resolve the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated the identity workflow, business rules, acceptance proof, data boundaries, GitHub identity interface, tradeoff, risk, open questions, blockers, source reference, and progress through `update-spec`.

### 2026-07-22 - Dot and plus-tag email normalization direction

- Completed: Required automatic matching to support local-part dot removal and `+tag` stripping while prohibiting global application, original-address rewriting, and ambiguous automatic matches.
- Remaining: Approve the exact launch allowlist and allowlist-change governance; obtain privacy or legal approval for the merge record; define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, and the unlink-policy data contract and lifecycle; and resolve the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated matching rules, conditional acceptance proof, data boundaries, identity interface, tradeoff, risk, open questions, blockers, official source references, and progress through `update-spec`.

### 2026-07-22 - Provider-documented alias-normalization scope

- Completed: Limited dot removal and `+tag` stripping to exact domains and account types backed by official provider documentation, approved each transformation independently, and prohibited personal-provider rules from being inherited by custom domains.
- Remaining: Approve the launch allowlist and allowlist-change governance; obtain privacy or legal approval for the merge record; define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, and the unlink-policy data contract and lifecycle; and resolve the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated matching policy, conditional acceptance proof, domain boundaries, tradeoff consequences, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - Conservative base email normalization

- Completed: Required surrounding-whitespace trimming, domain lowercasing, internal-whitespace rejection, and local-part case preservation unless an exact provider rule documents case-insensitive mailbox behavior; provider rules run in a fixed order.
- Remaining: Approve the launch provider allowlist and allowlist-change governance; obtain privacy or legal approval for the merge record; define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, and the unlink-policy data contract and lifecycle; and resolve the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated base matching rules, normalization order, acceptance proof, data boundaries, tradeoff, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - ASCII-only automatic identity matching

- Completed: Limited first-release automatic matching to verified ASCII addresses without `xn--` domain labels, kept supported internationalized-address sign-ins separate, and prohibited Unicode, IDNA, transliteration, diacritic, and confusable-character transformations from manufacturing a match.
- Remaining: Approve the launch provider allowlist and allowlist-change governance; obtain privacy or legal approval for the merge record; define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, and the unlink-policy data contract and lifecycle; and resolve the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated matching eligibility, separate-sign-in behavior, acceptance proof, design boundary, tradeoff, risk, deferred scope, blockers, and progress through `update-spec`.

### 2026-07-22 - Passwordless proof before GitHub unlink

- Completed: Allowed a merged user to unlink GitHub only after fresh passwordless magic-link proof for the stable identity and explicit confirmation, while preserving the passwordless workspace and projects, removing accepted GitHub credentials, ending GitHub-only sessions, and disconnecting rather than deleting affected repository connections.
- Remaining: Define incorrect-merge recovery, explicit re-link behavior without a verified primary GitHub email, and the unlink-policy data contract and lifecycle; approve the launch provider allowlist and governance; obtain privacy or legal approval for the merge record; and resolve the other GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated unlink workflow, scope, authentication rules, credential and session behavior, repository connection state, acceptance proof, design boundaries, interface, tradeoff, risk, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - Explicit GitHub re-link after unlink

- Completed: Prevented a later matching GitHub sign-in from reversing an explicit unlink automatically and required successful GitHub authentication, fresh passwordless proof, explicit confirmation, complete conflict preflight, atomic commit, and repository revalidation for re-linking.
- Remaining: Decide whether explicit re-linking can proceed without a verified primary GitHub email; approve the unlink-policy data contract and lifecycle; define incorrect-merge recovery; and resolve the launch allowlist, merge-record privacy, GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated re-link workflow, scope, business rules, acceptance proof, logical records, access boundaries, interface, tradeoff, risks, open questions, blockers, and progress through `update-spec`.

### 2026-07-22 - Explicit re-link permits different emails

- Completed: Allowed explicit GitHub re-linking after unlink when the verified primary GitHub email differs from the passwordless email, using fresh proof of both sign-in methods and confirmation of the identified accounts instead of automatic email equality or normalization.
- Remaining: Decide whether explicit re-linking can proceed without any verified primary GitHub email; approve the unlink-policy data contract and lifecycle; define incorrect-merge recovery; and resolve the launch allowlist, merge-record privacy, GDPR, synchronization, portability, slice, and technology questions.
- Failed checks: None; implementation has not started.
- Spec updates: Updated explicit re-link eligibility, confirmation behavior, acceptance proof, access boundaries, interface, tradeoff, open questions, blockers, and progress through `update-spec` without changing automatic-merge rules.
