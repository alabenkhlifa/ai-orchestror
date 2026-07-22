# Project Onboarding Design

## Context

The repository has no application toolchain or implementation architecture yet. Product behavior must be specified before selecting technologies.

OpenAI Symphony is the orchestration foundation, but its specification treats a rich web UI and multi-tenant control plane as non-goals. Project onboarding is therefore an SDD Orchestrator capability that sits before Symphony-derived scheduling, workspace management, and agent execution.

This design defines logical responsibilities and security boundaries only. It does not select an implementation language, framework, database, hosting platform, authentication library, or worker transport.

GDPR compliance is a project-wide constraint for every database schema and backend path, not a later deployment task. The design follows the processing principles, data protection by design and by default, and security obligations in the [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj), together with the [European Data Protection Board distinction between anonymisation and pseudonymisation](https://www.edpb.europa.eu/topics/ai-and-technology/anonymisation-pseudonymisation_en). Legal and privacy review remains required before production because technical verification alone cannot establish compliance.

## Proposed Approach

Use an entry page with two explicit paths:

1. Show `Login with GitHub` and `Work without GitHub` as the two primary actions.
2. For `Login with GitHub`, authenticate the user and use only the single GitHub email marked both primary and verified for automatic matching. When both verified addresses satisfy the first-release ASCII matching boundary and match under the approved normalization rules, preflight the combined hosted projects for project-name and repository conflicts before automatically attaching GitHub to the existing passwordless identity and personal workspace. Never match a secondary or internationalized address. A conflict-free merge moves every GitHub-backed project into that surviving workspace; a name conflict offers a user-confirmed lowest-available suffix; a repository conflict requires choosing which project keeps that repository and selecting a different repository for the other; any unresolved conflict makes no changes.
3. For `Work without GitHub`, enter the local repository path without GitHub authentication and let the user select a repository on their computer.
4. For either repository source, ask where this project's SDD data should be stored.
5. For on-device storage, establish a device boundary without requiring an account.
6. For hosted storage after `Work without GitHub`, collect an email address, send a passwordless magic link, and establish hosted identity only after the short-lived single-use link verifies the current attempt.
7. For a local repository only, detect whether the user has an available paired worker.
8. If the local path has no worker, guide the user through installation and secure pairing.
9. For the local path, ask the paired worker to validate and identify the selected repository without uploading its contents.
10. Validate the one-project-per-repository rule.
11. Derive the project name from the repository name, allocate the lowest available suffix using case-insensitive comparison, and allow the user to edit the name.
12. Create the project and repository connection as one operation, including the final workspace-scoped project name and selected data-storage boundary.
13. Show the project with its repository source and connection status. Keep it visible as disconnected if later access is lost, and do not start specification or agent work automatically.
14. Provide project export and import through a portable, versioned boundary that excludes credentials and other accepted secrets.
15. Allow a later direct storage-mode change with safe transfer, hosted soft deletion, retention, cleanup, and incremental resynchronization behavior.
16. When the device user authenticates, compose on-device and authorized hosted projects into one catalog without persisting device projects to the hosted account.
17. After a successful identity merge, revoke worker pairings bound to the absorbed workspace, leave each worker installed and local files unchanged, and require explicit re-pairing with new credentials for the surviving workspace.
18. Allow the merged user to unlink GitHub only after fresh passwordless proof and explicit confirmation, then remove GitHub access without changing the stable identity, workspace, projects, or stored repository connections. Preserve that explicit choice so a later GitHub sign-in requires fresh passwordless proof, confirmation, and complete conflict preflight instead of re-linking automatically.

The current candidate implementation slice delivers the GitHub path end to end. Storage selection, non-GitHub hosted identity, and portability add new boundaries that must be assigned to this slice or explicitly deferred before it can be approved. Collaboration is deferred to a separate specification.

## Components Affected

- Sign-in and session surface.
- User identity and personal workspace boundary.
- Passwordless email verification, delivery, session establishment, and recovery for non-GitHub hosted users.
- Verified-email identity matching, automatic GitHub linking, stable passwordless-workspace selection, non-destructive hosted-project consolidation, absorbed-workspace lifecycle, worker-pairing revocation and re-pairing, atomic conflict preflight, user-confirmed name and repository recovery, merge audit, unlinking, and recovery.
- Combined on-device and hosted project catalog with explicit storage and availability state.
- Workspace and project-data storage selection.
- Hosted identity and future collaboration boundary.
- GitHub repository catalog integration.
- Project registration and repository uniqueness rules.
- Repository source picker and onboarding status UI.
- Local worker installation and pairing flow.
- Local repository validation and connection-status reporting.
- Credential, session, and pairing-secret handling.
- Audit and diagnostic events for onboarding failures.
- Project export, import, version compatibility, and secret filtering.
- Storage migration, hosted soft deletion, retention cleanup, analytics separation, and incremental resynchronization.
- GDPR data inventory, processing-purpose and lawful-basis mapping, data-subject-rights workflows, processor boundaries, retention enforcement, security controls, and compliance evidence.

## Data and Access Boundaries

The logical domain needs these records regardless of the eventual persistence technology:

- `UserContext`: the ownership identity for a workspace, backed by GitHub, an accountless device boundary, or a verified email identity for non-GitHub hosted storage.
- `ExternalIdentity`: one verified GitHub or passwordless-email sign-in method attached to a stable hosted user identity.
- `IdentityMergeAttempt`: transient preflight and recovery state for matching verified identities, including conflicts and user-confirmed choices; it is not the retained post-merge audit record.
- `IdentityLinkPolicy`: minimal privacy-governed state that prevents automatic GitHub linking after a user-initiated unlink until an explicit re-link succeeds; its exact fields and lifecycle remain subject to the approved data contract.
- `WorkspaceMergeRecord`: the minimal inaccessible post-commit record containing only source workspace ID, surviving workspace ID, merge event ID, status, completion time, and approved deletion deadline.
- `PersonalWorkspace`: the stable ownership boundary for projects, workers, and repository links; the existing passwordless workspace survives an automatic merge.
- `Project`: the SDD Orchestrator project created for one repository.
- `RepositoryConnection`: the canonical identity, source type, display metadata, and connection status for one GitHub or local repository.
- `LocalWorker`: a user-owned installed execution endpoint whose pairing credentials bind it to one personal workspace and can be revoked and replaced without changing local repositories.
- `StorageMode`: the project-data boundary selected independently for each project, with `device` and `hosted` as the product-level choices.
- `WorkspaceAccess`: the ownership and authorization boundary for hosted data and future colleague collaboration.
- `ProjectPackage`: a portable, versioned representation used for export and import without accepted secrets.
- `SyncBaseline`: the latest retained hosted version used to identify changes when an on-device project returns to hosted storage.
- `DeletionSchedule`: the soft-deletion time and permanent-cleanup deadline applied to every project-scoped hosted record and derived copy.
- `AnalyticsRecord`: an aggregate record that is genuinely anonymous and contains no stable or linkable user, device, workspace, project, repository, network, or content identifier.
- `LegalRetentionRecord`: the minimum record an applicable legal obligation requires after project cleanup, separated from project content and governed by its own legal basis, purpose, access boundary, and deletion deadline.
- `DataProcessingRecord`: the approved purpose, lawful basis, data categories, recipients, transfers, security controls, retention, deletion, and data-subject-rights behavior for one processing activity.
- `RetentionPolicy`: the enforceable lifecycle for a data category across primary storage, derived records, logs, caches, indexes, backups, exports, and processors.

Required boundaries:

- Every project belongs to one personal workspace.
- Every project-data record belongs to one explicit storage mode.
- One workspace or user context may reference both on-device and hosted projects without changing either project's selected storage mode.
- Authentication changes the visible project catalogs, not the ownership or storage boundary of on-device projects.
- A combined catalog may reference device and hosted records together, but it must not copy device records into hosted storage or attach them to the authenticated identity implicitly.
- The operating-system user profile and filesystem permissions are the trust boundary for on-device project visibility; the application does not create a second local multi-user boundary.
- On-device project data remains under the current device boundary and does not require an account.
- Hosted project data is protected by an authorized identity and persists independently from the current device.
- A project display name is unique within its personal workspace using case-insensitive comparison, not globally across users.
- Project identity is stable and independent from its editable display name.
- Every repository connection belongs to one personal workspace and one project.
- The repository connection identity must be unique within its personal workspace.
- An automatic identity merge must evaluate the complete resulting project set against both workspace-scoped uniqueness rules before changing either identity or workspace.
- A conflict-free identity merge retains every hosted project and related hosted record from both identities while preserving stable project and repository identities.
- A project-name or repository conflict aborts the whole identity merge without partial reassignment, deletion, overwrite, or identity mutation.
- A project-name conflict proposal uses the same case-insensitive lowest-available numeric-suffix rule as normal project creation and remains non-mutating until the user confirms it.
- Confirmed conflict names are applied only inside a retried merge that passes a fresh complete preflight and commits atomically.
- A repository conflict remains non-mutating until the user chooses which project keeps the repository and selects a different authorized, valid, and unlinked repository for the other project.
- A confirmed replacement repository changes only that project's repository connection inside a retried atomic merge; it preserves both stable project identities and all hosted project data and does not modify either repository.
- The existing passwordless personal workspace is the target and surviving workspace for an automatic identity merge.
- GitHub-backed projects change workspace ownership only inside the successful atomic merge while preserving their stable project identities and related hosted data.
- The absorbed GitHub-backed workspace cannot remain as a second active personal workspace after success and is reduced to the approved minimal `WorkspaceMergeRecord`.
- A merge that does not commit leaves both original workspaces and their contents unchanged.
- A successful merge revokes, rather than transfers, every worker pairing bound to the absorbed workspace. The installed worker and local repositories remain unchanged.
- Re-pairing requires explicit user action and new credentials bound to the surviving workspace; affected repository connections remain recorded but unavailable until the worker and repositories are revalidated.
- A merge that does not commit leaves existing worker pairings valid and unchanged.
- After commit, the absorbed workspace is reduced immediately to a minimal `WorkspaceMergeRecord`; no full or soft-deleted workspace copy uses the two-year project-data lifecycle.
- The merge record contains no project or repository data, identity attributes, credentials, worker secrets, sessions, conflict details, membership data, or analytics linkage and is excluded from normal workspace and project access paths.
- The merge record remains personal data with a separately approved purpose, lawful basis, least-privilege access boundary, shortest necessary retention period, rights behavior, automatic deletion deadline, and required privacy or legal review.
- A GitHub `ExternalIdentity` can be removed from a merged hosted identity only after fresh passwordless magic-link authentication proves access to the verified email already attached to that same stable identity.
- Unlinking removes the GitHub sign-in method and SDD Orchestrator's accepted GitHub credentials without changing the stable user or passwordless workspace identity, project ownership, project data, or storage mode. It never recreates the absorbed workspace.
- Application sessions that depend only on the removed GitHub identity end. The fresh passwordless session becomes the continuing authorization boundary.
- Repository connections remain stored but move to disconnected when their access depended on the removed GitHub authorization; restoring provider access requires fresh GitHub authorization.
- A successful explicit unlink changes the stable identity's link policy before the unlink commits so future matching GitHub sign-ins cannot attach automatically. The policy is personal data and must not contain credentials, magic-link secrets, project data, or unnecessary provider attributes.
- Explicit re-linking requires successful authentication to GitHub and fresh passwordless authentication to the stable identity, explicit confirmation of the two identified accounts, and the same complete conflict preflight and atomic commit used by initial identity consolidation. A returned verified primary GitHub email may differ from the passwordless email because proof of both sign-in methods replaces email equivalence in this flow.
- A failed or cancelled re-link leaves the unlink policy and both identity boundaries unchanged. A successful re-link may clear or supersede the policy only inside the atomic re-link commit.
- Re-linking does not make a disconnected repository connected until the new GitHub authorization has been validated for that repository.
- Automatic identity matching uses only one GitHub email marked both primary and verified. A missing, unverified, non-matching, or ambiguous primary result prevents automatic matching.
- Secondary GitHub addresses are never match candidates and cannot be persisted, logged, audited, or sent to analytics; any provider response containing them is transient authentication data.
- First-release automatic matching is eligible only when both verified addresses contain ASCII characters and no domain label begins with `xn--`, compared case-insensitively. This eligibility check runs after surrounding-whitespace removal and structural validation but before local-part, alias, Unicode, or IDNA transformations.
- An ineligible internationalized address remains usable through a supported provider sign-in as a separate hosted identity. Matching must not normalize Unicode forms, transliterate, remove diacritics, map confusable characters, or convert between Unicode and ASCII-compatible domain forms, and the skip result cannot disclose another identity.
- Base normalization trims surrounding whitespace, lowercases the domain, rejects internal whitespace, and preserves local-part letter case.
- Provider-specific rules then apply independently in order: approved local-part case folding, period removal, and `+tag` stripping.
- Matching supports removing periods and stripping the first `+` and its following tag from the local part only for domains with explicitly approved provider semantics.
- Alias normalization never rewrites the original verified address and never applies to a custom or unknown domain merely because a known provider hosts it.
- Eligibility is exact-domain and account-type specific, and dot removal and `+tag` stripping are enabled independently only when official provider documentation supports that transformation for the same mailbox.
- An absent domain rule or a canonical form that matches multiple hosted identities prevents automatic merging.
- Onboarding and identity merging do not create, reconcile, change, or delete collaboration memberships, invitations, roles, or permissions.
- A future collaboration specification must define membership-aware identity merging before collaboration records are introduced.
- GitHub authorization and session secrets must remain server-side or in an equivalent protected credential boundary and must not be returned to the browser after acceptance.
- Worker pairing credentials must be short-lived or replaceable and bound to the current personal workspace and pairing attempt.
- A local worker may return repository identity and connection metadata, but local source content must not be persisted by the control plane during onboarding.
- Repository access must be revalidated when the provider or worker reports that access is no longer available.
- Lost repository access changes connection state without deleting or hiding the project.
- Repository location, project-data storage, and agent execution are separate boundaries.
- Exports and imports must not cross credential or secret boundaries.
- A direct storage-mode change preserves stable project and repository identity and becomes active only after the destination copy is usable.
- A hosted-to-device change makes the device copy active and moves the hosted project and related data into a soft-deleted state.
- Soft-deleted hosted project data remains isolated from active access for two years, then is permanently cleaned up except for analytics.
- Permanent cleanup cascades through specifications, tasks, agent runs, artifacts, comments, memberships, collaboration records, repository metadata, synchronization baselines, operational logs, caches, search indexes, backups, exports, and every other project-scoped copy.
- Only genuinely anonymous analytics and minimal legally required records may survive cleanup; legal records use a separate restricted schema and lifecycle and cannot preserve unnecessary project content or identifiers.
- A retained hosted version is absent from normal lists, search, collaboration views, and ordinary project APIs and may be read only by the authorized resynchronization process after explicit user action from the active on-device project.
- Resynchronization before cleanup reactivates the hosted project and transfers only changes since the retained baseline.
- Returning to hosted storage after baseline cleanup performs a full upload while preserving stable project and repository identity.
- Personal data and anonymous analytics are separate data classes with no join key or retained mapping that can re-identify analytics.
- Pseudonymised, hashed, encrypted, or otherwise reversible or linkable data remains personal data and cannot use the anonymous-analytics retention exception.
- Every personal-data field and processing path needs an approved purpose, lawful basis, necessity, access boundary, retention policy, rights behavior, processor boundary, and security classification.
- Privacy-preserving defaults, data minimization, least privilege, retention enforcement, and auditable deletion apply at both schema and service boundaries.
- Applicable data-subject requests must propagate through active, derived, soft-deleted, backed-up, exported, logged, indexed, and processor-held personal data according to the approved data contract.

## Interfaces

- Entry-choice interface: present the GitHub and local-repository paths without conflating repository location with later agent execution location.
- GitHub identity interface: authenticate the user, return stable identity information and one unambiguous verified primary email for automatic matching, and treat all secondary email data as transient and non-matchable.
- Non-GitHub identity interface: establish an accountless device boundary or authenticate and restore hosted workspace access through verified email and passwordless magic links.
- Magic-link interface: accept an email without account enumeration, issue a short-lived single-use attempt-bound token, verify it once, establish a hosted session, and reject invalid, expired, reused, or mismatched links without exposing secrets.
- Identity-linking interface: check both verified addresses against the first-release ASCII eligibility boundary, normalize eligible addresses through the approved base and domain-specific alias rules, reject ineligible addresses, absent rules, and ambiguous results safely, select the existing passwordless workspace as the stable target, preflight the complete combined project set, collect explicit conflict-recovery confirmations, rerun preflight, attach GitHub and move every GitHub-backed project into the target workspace when no conflict remains, reduce the source to the approved minimal merge record, abort without mutation when any condition fails, audit the result, and reject automatic linking when verification or matching is insufficient.
- Identity-unlinking interface: require fresh passwordless magic-link proof for the verified email on the stable identity, disclose the loss of GitHub sign-in and possible repository disconnection, collect explicit confirmation, remove the GitHub sign-in method and accepted credentials atomically, end GitHub-only sessions, preserve the passwordless identity and all project data, and make a failed attempt non-mutating and auditable.
- Identity-relinking interface: detect the prior explicit-unlink policy before automatic matching, authenticate both sign-in methods, identify both accounts for confirmation without requiring their verified emails to match, require fresh passwordless proof and explicit confirmation, rerun complete project conflict preflight, attach GitHub only through an atomic successful commit, retain the policy after any failed attempt, and revalidate each disconnected repository before restoring its connection.
- Project-catalog interface: combine projects available under the current device boundary with projects authorized for the hosted identity, expose storage and availability state, and remove hosted access on sign-out without mutating device projects.
- Storage-selection interface: let the user choose on-device or hosted project data without implying a repository or agent location.
- Hosted access interface: establish identity and authorization for hosted data and later collaboration.
- GitHub repository catalog interface: list every repository available under the granted account access and return a stable repository identity plus display metadata.
- Session interface: establish, restore, expire, and end authenticated access.
- Project registration interface: validate repository uniqueness, allocate a user-scoped project name, and create the project and repository link atomically.
- Project naming interface: validate case-insensitive uniqueness and rename a project without changing its stable identity or repository connection.
- Worker pairing interface: establish trust between one personal workspace and an installed local worker, revoke absorbed-workspace credentials after a successful identity merge, expose a pairing-required state, and issue new surviving-workspace credentials only after explicit re-pairing.
- Local repository interface: validate a user-selected path as a Git repository and return only the metadata needed to identify it and report availability.
- Connection-status interface: distinguish connected, unavailable, authorization-required, and invalid states without exposing secrets or local source content.
- Project portability interface: export and import versioned project packages, reject unsupported or unsafe packages, and resolve identity and name conflicts without exposing secrets.
- Storage-migration interface: transfer project data between modes, verify the destination, preserve stable identity, and switch the active copy without modifying the repository.
- Hosted-retention interface: soft-delete and isolate hosted project data from normal reads, enforce its two-year cleanup deadline, separate retained analytics, and allow access only when an explicitly authorized resynchronization reactivates the project.
- Resynchronization interface: compare the on-device state with a retained hosted baseline and synchronize only authorized changes, or perform a full upload under the same stable identity when no baseline remains.
- Privacy-governance interface: inventory processing activities and prevent a schema or backend path from being approved without its GDPR data contract and required review.
- Data-subject-rights interface: authenticate and execute applicable access, correction, erasure, restriction, objection, and portability requests across all governed copies.
- Retention-enforcement interface: apply approved retention and deletion behavior across primary and derived storage, processors, backups, logs, caches, indexes, and exports.
- Analytics-anonymisation interface: aggregate and irreversibly anonymise allowed metrics before retention, then test resistance to singling out, linkability, and inference.

Exact protocols and schemas remain part of the technology-selection update.

## Decisions and Tradeoffs

### Two Entry Paths

- Choice: Present `Login with GitHub` and `Work without GitHub` as the two primary entry actions.
- Reason: A user with a repository on their computer must be able to use the product without creating or connecting a GitHub account.
- Consequence: The product needs an accountless device boundary for on-device data and verified passwordless email identity for hosted data, and implementation slices must not expose a primary action before its path works.

### Device And Hosted Workspaces

- Choice: Support accountless on-device workspaces and hosted workspaces that can later authorize colleague collaboration.
- Reason: Users should control whether project data stays on their device or is available through the service for shared work.
- Consequence: Hosted identity, ownership, membership, and permission behavior must be specified before collaboration is implemented.

### Passwordless Email For Non-GitHub Hosted Access

- Choice: Authenticate users who select `Work without GitHub` and hosted storage by verifying an email address through a passwordless magic link.
- Reason: Hosted data needs a recoverable authorized identity without forcing the user to create or connect a GitHub account or manage another password.
- Consequence: The product needs secure email delivery, attempt-bound single-use tokens, expiration and resend rules, enumeration-resistant responses, session management, recovery behavior, abuse protection, and GDPR governance for email and authentication events.

### Automatic GitHub And Email Identity Merge

- Choice: Automatically merge a GitHub identity with an existing passwordless-email identity when GitHub's single verified primary email matches the verified passwordless email under approved normalization rules.
- Reason: The same person should enter one hosted account and keep the same projects regardless of which supported sign-in method they use.
- Consequence: Identity linking needs minimum-permission verified-primary retrieval, normalization, idempotency, stable user identity, user disclosure, audit evidence, unlinking and recovery rules, and protection against account takeover.

### Verified Primary GitHub Email Only

- Choice: Use only the single GitHub email marked both primary and verified for automatic identity matching; never match a secondary email.
- Reason: A narrow authoritative match reduces unintended account consolidation and avoids treating every address attached to a GitHub account as an automatic ownership key.
- Consequence: Missing, unverified, non-matching, or ambiguous primary results skip automatic merging. The GitHub integration must request the minimum email-read permission that exposes the `primary` and `verified` attributes, and secondary addresses must not be retained. GitHub's current email endpoint documents these attributes and its required email permission in the [official GitHub API documentation](https://docs.github.com/en/rest/users/emails).

### Provider-Aware Dot And Plus Alias Normalization

- Choice: Support removal of periods and stripping of `+tags` from the email local part for automatic matching.
- Reason: Some providers deliver those variations to the same mailbox, so treating documented aliases as one address avoids duplicate hosted identities.
- Consequence: The transformations use an exact-domain and account-type allowlist, are enabled independently, and do not alter the original verified email. They cannot be applied globally because SMTP assigns local-part semantics to the receiving host, as specified by [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321.html). Google documents that periods are ignored for personal Gmail addresses but matter for work, school, and other organizational domains in [Gmail Help](https://support.google.com/mail/answer/7436150?hl=en). The launch entries, collision proof, and allowlist-change governance remain blockers.

### Conservative Base Email Normalization

- Choice: For every verified email eligible for automatic matching, trim surrounding whitespace and lowercase the domain while preserving local-part letter case unless an exact provider rule documents case-insensitive mailbox behavior.
- Reason: Domains are case-insensitive, but SMTP assigns local-part semantics to the receiving host. Preserving local-part case by default avoids merging distinct mailboxes while still removing harmless input and domain variations.
- Consequence: Internal whitespace is invalid and provider-specific case folding precedes dot and `+tag` rules. This normalization runs only for addresses that pass the first-release ASCII eligibility boundary.

### ASCII-Only Automatic Matching At Launch

- Choice: Restrict first-release automatic identity matching to verified ASCII addresses whose domain labels do not use the reserved `xn--` prefix; internationalized addresses continue as separate supported sign-ins.
- Reason: Unicode equivalence, IDNA conversion, and confusable-character handling can create unsafe identity matches without a dedicated policy and verification model. IDNA also has an ASCII-compatible A-label form beginning with `xn--`, so checking only for non-ASCII code points would leave an alternate representation inside the matching boundary, as defined by [RFC 5890](https://www.rfc-editor.org/rfc/rfc5890.html).
- Consequence: Matching fails closed before Unicode or IDNA transformation, does not reveal whether another identity exists, and leaves each verified sign-in attached to its existing hosted identity. Supporting automatic matching for internationalized addresses requires a future specification update and dedicated collision, equivalence, and spoofing proof.

### Non-Destructive Hosted Project Consolidation

- Choice: Retain every hosted project from both matching identities and commit their consolidation atomically only after the resulting personal workspace passes case-insensitive project-name and repository-uniqueness checks.
- Reason: Having projects on both identities is normal account history, not a reason to discard data or reject a verified identity match.
- Consequence: A project-name or repository conflict stops the entire merge before mutation. The product needs a recovery flow that resolves the conflict and retries the preflight without deleting, overwriting, renaming, or partially reassigning projects implicitly.

### User-Confirmed Merge Name Resolution

- Choice: For each merge-time project-name conflict, suggest the lowest available numeric-suffix name under the existing case-insensitive rule and require user confirmation before retrying the merge.
- Reason: The established naming rule gives the user a predictable resolution while explicit confirmation prevents a merge from silently renaming existing work.
- Consequence: Suggestions are provisional, confirmed names are revalidated, and renames occur only inside a successful atomic merge. Cancellation or a failed retry leaves both identities and all projects unchanged.

### User-Confirmed Merge Repository Resolution

- Choice: When two projects would link the same repository after an identity merge, require the user to choose which project keeps it and select a different repository for the other project.
- Reason: This preserves both projects and their data while maintaining one project per repository in the resulting personal workspace.
- Consequence: Keeper and replacement choices are provisional until a fresh complete preflight succeeds. The replacement must be authorized, valid, and unlinked; only its project's repository connection changes, and only inside the atomic merge. Cancellation or failed validation leaves both accounts unchanged.

### Passwordless Workspace Survives Identity Merge

- Choice: Keep the existing passwordless personal workspace as the stable workspace and move every GitHub-backed hosted project into it only when the automatic merge commits.
- Reason: The passwordless account already represents the hosted identity being linked, so preserving its workspace avoids replacing an established ownership boundary while still retaining all projects.
- Consequence: Project workspace ownership changes atomically without changing stable project identities or data. The GitHub-backed workspace stops being active, its worker pairings are revoked, and only the field-limited merge record remains. That record's lawful basis and shortest retention require approval before implementation. Membership handling remains deferred to the collaboration specification.

### Fresh Passwordless Proof Before GitHub Unlink

- Choice: Let a merged user unlink GitHub only after fresh passwordless magic-link authentication for the verified email already attached to the stable hosted identity and explicit confirmation of the access consequences.
- Reason: Removing one sign-in method must not leave the account without a proven recovery path or let a GitHub-only session remove its own identity proof.
- Consequence: Unlinking revokes or deletes SDD Orchestrator's accepted GitHub credentials, ends GitHub-only sessions, and disconnects repository access that depended on those credentials. The stable passwordless identity, surviving workspace, projects, data, stored repository connections, and absorbed-workspace state do not change. Incorrect-merge challenges still require a separate recovery decision.

### Explicit Re-Link After User Unlink

- Choice: A later GitHub sign-in cannot automatically reverse an explicit unlink; re-linking requires successful GitHub authentication, fresh passwordless proof for the stable identity, explicit confirmation, and complete conflict preflight.
- Reason: Automatic re-linking would undo a deliberate security and account-access choice without renewed consent.
- Consequence: The system needs a durable, minimal `IdentityLinkPolicy` checked before automatic matching. A returned verified primary GitHub email may differ from the passwordless email because fresh proof of both methods and confirmation replace email comparison for explicit re-linking; automatic normalization and ASCII restrictions remain unchanged for automatic merges. Failed or cancelled attempts remain non-mutating, successful re-linking commits atomically, and repository connections remain disconnected until revalidated. Whether re-linking can proceed without any verified primary GitHub email, and the policy record's exact data contract and lifecycle, remain blockers.

### Re-Pair Workers After Identity Merge

- Choice: Revoke worker pairings bound to the absorbed workspace after a successful merge and require explicit re-pairing with the surviving workspace, without uninstalling the worker.
- Reason: Pairing grants machine access within one workspace trust boundary. Transferring its credential silently would extend that trust without fresh user consent.
- Consequence: The worker remains installed, local repositories and files remain unchanged, old credentials stop working only after the merge commits, and new credentials are issued through the normal pairing flow. Local repository connections remain visible but unavailable until revalidation succeeds.

### Minimal Absorbed-Workspace Merge Record

- Choice: Immediately replace the absorbed workspace with an inaccessible merge record containing only source and surviving workspace IDs, merge event ID, status, completion time, and an approved deletion deadline.
- Reason: Idempotency, security audit, and verified support may need evidence that the workspace was absorbed, but retaining its content or automatically applying the two-year project-data rule would exceed that narrow purpose.
- Consequence: Active merge details are transient; the retained record has no project, repository, identity-attribute, credential, worker-secret, session, conflict, membership, or analytics-linkage data. Its lawful basis and shortest necessary retention period require privacy or legal approval, and automatic deletion is mandatory.

### Collaboration Memberships Deferred

- Choice: Keep invitations, memberships, roles, permissions, and membership reconciliation out of project onboarding and its implementation slice.
- Reason: Collaboration has its own authorization and audit behavior and needs a separate specification rather than implicit rules inside repository onboarding.
- Consequence: The onboarding merge processes identity, personal workspaces, projects, and repository connections only. A collaboration specification must extend merge behavior before membership data exists, without widening or removing access or losing membership history.

### Combined Catalog Without Implicit Upload

- Choice: After authentication, show accountless on-device projects alongside authorized hosted projects while leaving each project in its existing storage mode.
- Reason: Signing in should not hide local work or force the user to upload it.
- Consequence: The catalog must compose device and hosted sources, label storage and availability, remove hosted access on sign-out, and avoid duplicate presentation while relying on the operating-system user and filesystem boundary for local access.

### Operating-System Boundary For On-Device Data

- Choice: Treat the current operating-system user profile and filesystem permissions as the access boundary for on-device projects.
- Reason: Protecting multiple people who share the same operating-system account or filesystem access is outside SDD Orchestrator's responsibility.
- Consequence: The product does not implement separate local profiles or promise isolation inside a shared operating-system boundary.

### User-Chosen Project-Data Storage

- Choice: Let the user choose on-device or SDD Orchestrator-hosted storage independently for each project's data.
- Reason: On-device storage supports private independent work, while hosted storage supports persistence beyond one device and future collaboration.
- Consequence: The product must make each project's data location and migration state visible.

### Direct Storage Migration

- Choice: Let the user change an existing project directly between on-device and hosted storage without export and import.
- Reason: Storage location is an operational preference that can change during the project's lifetime.
- Consequence: Migration needs destination verification, atomic activation, failure recovery, secret filtering, and stable identity across both modes.

### Hosted-To-Device Retention

- Choice: When a hosted project moves on-device, mark every project-scoped hosted record as deleted, retain it for two years, then permanently clean every copy up except for genuinely anonymous analytics and minimal legally required records.
- Reason: The hosted copy should stop acting as the active project while preserving a temporary baseline for returning to hosted storage.
- Consequence: The product needs explicit soft-deletion state, exclusion from every normal read path, resynchronization-only authorization, complete cross-store deletion propagation, analytics separation, and separately governed legal-retention records.

### Incremental Hosted Resynchronization

- Choice: When an on-device project returns to hosted storage before cleanup, synchronize changes since the latest retained hosted version.
- Reason: Reusing the retained baseline avoids retransmitting and recreating unchanged project data.
- Consequence: The system needs version tracking, change and deletion detection, compatibility rules, conflict behavior, and full-upload rehydration that preserves stable identity after the baseline is cleaned up.

### GDPR By Design And Default

- Choice: Require every database schema and backend processing path to follow GDPR principles and an approved data contract from its first design.
- Reason: Hosted identity, collaboration, repository metadata, agent activity, exports, logs, and retention can all process personal or sensitive project data.
- Consequence: Schema and backend approval require documented purpose, lawful basis, minimization, retention, rights handling, processor and transfer boundaries, security controls, and privacy review. Automated checks provide evidence but do not replace legal accountability.

### Anonymous Aggregate Analytics

- Choice: Retain analytics only when they are aggregate and genuinely anonymous, with no data that permits singling out, linkability, inference, or reconstruction of a person, project, workspace, repository, or device.
- Reason: Analytics should help evaluate the product without extending the personal-data lifecycle or preserving deleted project context.
- Consequence: Pseudonymous identifiers are not sufficient. Analytics need a separate schema, no re-identification mapping, minimum aggregation thresholds, disclosure-risk testing, and explicit metric-level retention.

### Portable Projects

- Choice: Let users export and import projects.
- Reason: Users need a way to back up, move, and exchange projects without being locked into one storage mode.
- Consequence: The package needs versioning, integrity checks, secret exclusion, conflict handling, and repository reconnection rules before implementation.

### Visible GitHub Catalog

- Choice: Show every repository returned under the user's granted GitHub access, then link only the repository the user confirms.
- Reason: Users should not need to know or paste repository URLs.
- Consequence: The GitHub authorization must support repository discovery, and the UI must remain usable for accounts with many repositories.

### One Project Per Repository

- Choice: Enforce one repository per project and one project per repository within a personal workspace.
- Reason: It gives later specifications, runs, workers, and verification evidence one unambiguous repository boundary.
- Consequence: Monorepo subprojects and multiple SDD configurations for one repository are deferred.

### Editable User-Scoped Project Names

- Choice: Default the project name to the repository name, allow it to be edited at any time, and keep names unique by case-insensitive comparison only within the owning personal workspace.
- Reason: The default requires no naming decision from a non-technical user, while user-scoped uniqueness allows different users to link the same repository independently.
- Consequence: Default-name allocation and every rename must enforce the same uniqueness boundary, while stable project identity and repository identity cannot depend on the mutable display name.

### Local Source Stays Local

- Choice: Link local repositories through a paired local worker and do not upload repository content during onboarding.
- Reason: It protects local source and supports repositories that are not hosted on GitHub.
- Consequence: Local onboarding depends on installing, pairing, and monitoring another component.

### Repository Access Loss

- Choice: Keep a project visible with a disconnected status when its linked GitHub repository becomes inaccessible.
- Reason: Temporary authorization or provider changes must not erase the user's project context.
- Consequence: Repository access is a recoverable connection state, not a condition for project existence.

### Technology-Neutral Specification

- Choice: Describe logical responsibilities and contracts before choosing technologies.
- Reason: No technology preference has been selected, so product and security behavior should determine the stack and the amount of Symphony implementation that can be reused.
- Consequence: Implementation remains blocked until the runtime, persistence, authentication, and worker communication decisions are recorded through `update-spec`.

## Risks

- Listing all accessible GitHub repositories can require broad authorization. Reduce this by making the requested access clear, protecting credentials, and documenting provider limitations before approval.
- A non-technical user may confuse GitHub authentication, local repository location, local worker pairing, agent execution location, and later AI-provider authentication. Keep them as separate concepts with distinct status and recovery messages.
- A compromised pairing flow could grant access to a user's machine. Bind pairing to the current personal workspace, expire incomplete attempts, and make paired workers visible and revocable.
- Silently transferring a worker pairing during identity merge could grant the surviving workspace machine access without explicit consent. Revoke source-workspace credentials after commit, require re-pairing, and never alter the installed worker or local files as part of revocation.
- Local paths can reveal sensitive machine information. Define the minimum metadata sent to the control plane and avoid displaying full paths unless required by the user.
- Hosted data can expose private project information to the wrong person if identity and membership rules are weak. Define ownership, authorization, revocation, and audit behavior before enabling collaboration.
- Export packages can leak credentials or sensitive repository details. Define an explicit package schema, exclude secrets, validate imports, and make included data visible to the user.
- A failed migration can leave two divergent or incomplete copies. Verify the destination before activation, keep one authoritative storage mode, and make retry or rollback behavior explicit.
- Retained soft-deleted data can remain accessible longer than the user expects. Isolate it from normal access, enforce cleanup deadlines, audit lifecycle changes, and explain the analytics exception.
- Incremental resynchronization can miss or overwrite changes when versions diverge. Define immutable baselines, change identifiers, deletion semantics, compatibility checks, and conflict handling before implementation.
- A dataset described as anonymous may remain personal data when rare attributes, stable identifiers, joins, or small groups allow re-identification. Treat uncertain data as personal, prohibit re-identification mappings, and require documented anonymisation testing.
- Magic links can be stolen, replayed, leaked through logs or referrers, or abused to enumerate accounts and send unwanted email. Use short-lived single-use attempt-bound tokens, protect every token surface, rate-limit requests, and keep responses account-neutral.
- Automatic email-based identity linking can cause account takeover or data corruption when an email is unverified, secondary, reassigned, normalized incorrectly, or already attached to conflicting hosted data. Require one unambiguous verified primary GitHub email, never match or retain secondary addresses, preflight the complete project set, keep recovery choices non-mutating until confirmation, abort atomically on unresolved conflicts, retain all projects, preserve stable project identities, notify the user, and audit every merge attempt.
- Applying dot removal or `+tag` stripping to a domain that treats those characters as significant can merge different people's accounts. Require an explicitly reviewed domain rule backed by provider documentation, fail closed for unknown domains and ambiguous matches, and version changes to the allowlist.
- Unicode and IDNA representations can create equivalent-looking or confusable identifiers and unintended account merges. Keep them outside first-release automatic matching, block both non-ASCII characters and `xn--` domain labels, and require a dedicated reviewed policy before widening eligibility.
- Unlinking GitHub without fresh independent proof could lock the user out, leave provider credentials active, or detach repository access unexpectedly. Require fresh passwordless authentication, an explicit consequence warning, atomic local credential removal, provider revocation where supported, GitHub-only session termination, and disconnected rather than deleted projects.
- Automatically re-linking GitHub after the user explicitly removed it would defeat consent and could restore provider access unexpectedly. Check a privacy-governed unlink policy before email matching, require proof of both sign-in methods and confirmation, and keep failed re-link attempts non-mutating.
- A durable unlink policy can become an unnecessary identity map if it stores provider or email history indefinitely. Minimize its fields and access, prohibit credentials and project data, and block implementation until its purpose, lawful basis, retention, deletion, rights handling, and required review are approved.
- An absorbed workspace can remain accidentally accessible or retain unnecessary personal data after merge. Make the passwordless workspace the single active target, block all source-workspace access after commit, reduce it immediately to the field-limited merge record, and enforce that record's approved deletion deadline.
- A merge audit record can become an undeclared identity map or indefinite personal-data store. Limit it to the approved fields and access paths, prohibit analytics use and joins, attach an enforced deletion deadline, and block implementation until its lawful basis and shortest retention are approved.
- A person with access to the same operating-system user profile and files can access on-device project data. This is an explicit environment boundary, while hosted authorization still must never grant or infer local filesystem ownership.
- GDPR compliance can fail outside the main schema through logs, backups, exports, local workers, agents, analytics pipelines, and subprocessors. Include every copy and transfer in the processing inventory and verification gate.
- A fixed retention rule can conflict with legal obligations or data-subject rights. Record the purpose and lawful exception for each data category and obtain privacy or legal approval before production.
- Repository renames, transfers, changed Git remotes, and lost permissions can defeat naive duplicate detection. Define canonical hosted and local repository identities before implementation.
- Concurrent project creation can allocate the same project name or numeric suffix. Enforce user-scoped name uniqueness at the persistence boundary and retry suffix allocation after a conflict.
- GitHub outages, rate limits, organization policies, or SSO requirements can make an accessible repository temporarily unavailable. Preserve consistent project state and show a recoverable connection status.
- Selecting a framework before these boundaries are resolved could make the Symphony foundation or local-worker model harder to adopt. Keep technology selection as an explicit approval gate.

## Open Questions

- Which GitHub integration model provides sign-in, complete repository discovery, acceptable permission scope, and secure long-lived access?
- What magic-link lifetime, resend and invalidation behavior, session lifetime, delivery provider, rate limits, and recovery behavior protect non-GitHub hosted access?
- Which exact domains and account types have sufficient official provider evidence for each launch allowlist transformation?
- How are allowlist evidence, security review, version changes, and removal of a previously approved rule governed?
- What lawful basis and shortest necessary retention period receive privacy or legal approval for the minimal absorbed-workspace merge record?
- How can a user challenge and recover from an incorrect automatic identity merge?
- Can explicit re-linking proceed when GitHub returns no verified primary email, provided both sign-in methods are freshly proven?
- What minimum fields, lawful basis, retention, deletion, rights behavior, and privacy review govern `IdentityLinkPolicy`?
- Which anonymous aggregate metrics are necessary, what minimum aggregation thresholds prevent singling out, and how long is each metric retained?
- Who is the controller or processor for hosted storage, local workers, coding agents, model providers, infrastructure providers, and collaboration data?
- Which purposes and lawful bases govern each personal-data processing activity?
- How are data-subject requests authenticated and propagated through active data, deleted data, processors, backups, logs, exports, caches, and indexes?
- Which retention schedules apply to each personal-data category, and which legally approved exceptions delay deletion?
- Which subprocessors, processing locations, and international transfers are allowed, and which safeguards apply?
- Which processing activities require a data protection impact assessment, data protection officer input, or other privacy review?
- Which version, change-tracking, deletion, conflict, and compatibility model supports incremental resynchronization?
- What schema, history, attachments, repository metadata, and source content belong in a project package?
- How are package compatibility, integrity, project identity, name conflicts, repository reconnection, and duplicate imports handled?
- Must the GitHub and local entry paths ship in one executable slice, or may the complete local entry surface be delivered in the immediately following slice?
- How are sessions and GitHub credentials stored, refreshed, revoked, and separated from coding-agent processes?
- Which application runtime, UI approach, persistence system, and deployment model satisfy the first slice?
- Will the project extend Symphony's Elixir implementation, run it as a separate orchestration service, or implement its specification in another runtime?
- How is the local worker packaged, installed, updated, paired, revoked, and reconnected?
- Which transport lets the control plane reach a local worker without requiring inbound network access to the user's computer?
- What canonical identity prevents duplicate links for GitHub repositories and for local repositories whose paths or remotes change?
- What is the minimum local repository metadata that may leave the user's computer?
