# Project Storage Lifecycle

## Status

Draft

## Outcome

A user can choose on-device or SDD Orchestrator-hosted storage for each project's specifications, tasks, agent runs, and generated files, change that choice later without modifying the linked repository, and rely on defined synchronization, retention, cleanup, privacy, and analytics behavior.

## Users

- Project contributors choosing where SDD specifications, tasks, agent records, and artifacts are stored.
- Authorized colleagues who may later collaborate on hosted project data.
- Privacy, operations, and support personnel enforcing approved lifecycle workflows.

## Primary Workflow

1. During GitHub or local repository onboarding, the user reaches a dedicated step that explains which project work the choice covers and that the linked repository stays where it is.
2. Both storage choices remain visible; a choice whose prerequisite is missing explains what is required and provides the relevant setup action.
3. If on-device storage requires setup, the product guides the user through device setup and returns to the same storage step with the selected repository and current onboarding state preserved.
4. The user explicitly chooses whether to save the project work on the current device or in their SDD Orchestrator account after the chosen mode's prerequisites are available.
5. The project is created with one explicit authoritative storage mode, then the new project's dashboard shows that mode with its repository and connection status.
6. The user may keep on-device and hosted projects in the same catalog.
7. The user may later request a direct storage-mode change without export and import.
8. The destination is transferred and verified before it becomes authoritative.
9. Moving hosted data on-device marks the hosted project and all related hosted copies deleted, hides them from ordinary access, and starts a two-year cleanup deadline.
10. Returning to hosted storage before cleanup synchronizes changes against the retained baseline.
11. Returning after cleanup performs a full upload while preserving stable project and repository identity.
12. Retention enforcement permanently removes project-scoped hosted data at the deadline except genuinely anonymous analytics and separately lawful minimum legal records.

## In Scope

- Per-project on-device or hosted storage selection for GitHub and local repositories.
- Storage-mode presentation on the new-project dashboard after either onboarding path succeeds.
- Mixed storage modes for one user.
- Stable project identity across storage changes.
- Direct device-to-hosted and hosted-to-device migration.
- Authoritative-copy selection, transfer verification, failure recovery, and concurrency boundaries.
- Hosted soft deletion, access isolation, two-year retention, and complete cleanup propagation.
- Incremental resynchronization from a retained hosted baseline.
- Full-upload rehydration after baseline cleanup.
- Anonymous aggregate analytics boundaries.
- GDPR data protection by design and default across schema, services, logs, caches, indexes, backups, exports, workers, agents, and processors.
- Data-subject-rights and legal-retention boundaries for project data.

## Out of Scope

- Repository onboarding mechanics, defined in `specs/01-github-project-onboarding/` and `specs/02-local-project-onboarding/`.
- Passwordless identity mechanics, defined in `specs/03-hosted-passwordless-access/`.
- Identity merging, defined in `specs/04-github-identity-linking/`.
- Export and import packages, defined in `specs/06-project-portability/`.
- Collaboration invitation, role, membership, and permission workflows.
- User-initiated project deletion unrelated to a storage-mode change.
- Repository source transfer unless a later specification explicitly includes it.

## Business Rules

- Storage mode is selected per project, not once for the user or workspace.
- The selection step must be titled `Where should your project work be saved?`.
- The selection step must explain: `Your project work includes specifications, tasks, agent runs, and generated files. Your linked repository stays where it is.`
- The on-device choice must be labeled `On this device` and explain: `Your project work stays on this device. It will not be available on another device or to collaborators unless you move or export it later.`
- The hosted choice must be labeled `In my SDD Orchestrator account` and explain: `Your project work is saved to your account so you can access it from other devices and collaborate with others.`
- Both choices must remain visible when a device or identity prerequisite is missing; an unavailable choice must identify the missing prerequisite and provide the relevant setup action instead of disappearing.
- Starting device setup must preserve the selected repository and current onboarding state.
- After device setup succeeds, is canceled, or fails, the product must return to the same storage step without losing the selected repository.
- Successful device setup must only re-evaluate availability. It must not silently select `On this device` or create a project.
- Canceled or failed device setup must leave `On this device` unavailable and must not create a project.
- Project creation requires an explicit storage choice; neither mode is silently selected for the user.
- After project creation succeeds, the new project's dashboard must show the selected authoritative storage mode with the linked repository and current connection status.
- The same user may have on-device and hosted projects simultaneously.
- Repository source does not restrict project-data storage; GitHub and local repositories may use either mode.
- Repository location, project-data storage, local worker location, and AI-agent execution location are independent boundaries.
- On-device storage must not require an account and remains under the current device and operating-system trust boundary.
- Hosted storage persists independently from the current device and requires an authorized identity before data is exposed.
- Hosted storage is the mode capable of later live collaboration with authorized colleagues.
- Every project-data record belongs to one project and one explicit storage mode.
- One copy is authoritative during and after a migration; a failed transfer must leave the prior copy and mode usable.
- A storage change must not modify the linked repository, stable project identity, or repository connection identity.
- A destination must be complete and verified before authority changes.
- Moving hosted data on-device makes the on-device copy authoritative and marks the hosted project and all related hosted data deleted.
- Deleted hosted project data is retained for two years from the storage-mode change and then permanently cleaned up.
- The cleanup covers all project-scoped primary and derived copies, including specifications, tasks, runs, artifacts, comments, memberships, collaboration records, repository metadata, synchronization baselines, operational logs, caches, indexes, backups, exports, and processor copies.
- A soft-deleted hosted copy is hidden from ordinary project lists, search, collaboration views, and APIs and cannot be opened, edited, browsed, or manually restored.
- During retention, the deleted hosted copy is accessible only to the explicitly authorized resynchronization and governed rights, security, retention, or legal workflows.
- Before cleanup, the latest retained hosted version is the resynchronization baseline.
- Returning to hosted storage before cleanup sends and applies authorized changes since the retained version instead of retransmitting unchanged data.
- Returning after cleanup performs a full upload under the same stable project identity and repository connection.
- Synchronization must define version, change, deletion, conflict, compatibility, retry, and failure semantics before implementation.
- The only cleanup exceptions are genuinely anonymous aggregate analytics and minimum records required by an applicable legal obligation.
- A legal-retention record has its own documented legal basis, purpose, minimum fields, restricted access, rights behavior, and deletion deadline; it must not retain more project content or identifiers than required.
- Analytics must be aggregate and genuinely anonymous and contain no user, device, workspace, project, repository, network, content, or stable pseudonymous identifiers.
- Pseudonymised, hashed, encrypted, or otherwise linkable data is personal data, not anonymous analytics.
- Personal data must be processed lawfully, fairly, and transparently for explicit purposes and limited to what is necessary.
- Database schemas and backend logic must enforce purpose limitation, data minimization, accuracy, storage limitation, least privilege, confidentiality, integrity, availability, and auditable deletion by design and default.
- Every personal-data category requires an approved purpose, lawful basis, access boundary, retention, deletion, rights behavior, processors, transfers, and required review before implementation.
- Personal data must not be repurposed for analytics or product improvement without an approved basis and transparent behavior.
- Applicable access, correction, erasure, restriction, objection, and portability requests must propagate through active, deleted, derived, backup, export, and processor copies under approved rules.
- High-risk processing must not ship without its required impact assessment and review.

## Acceptance Criteria

- Given a GitHub or local repository is selected, when the storage step opens, then it is titled `Where should your project work be saved?`, explains what project work includes and that the linked repository stays where it is, and presents `On this device` and `In my SDD Orchestrator account` with their availability and collaboration consequences.
- Given one storage mode is missing a required device or identity prerequisite, when the storage step opens, then both modes remain visible and the unavailable mode explains the missing prerequisite with a relevant setup action.
- Given `On this device` requires setup, when the user starts device setup, then the selected repository and current onboarding state are preserved.
- Given device setup succeeds, is canceled, or fails, when the user returns, then the same storage step and selected repository are restored; success refreshes availability without selecting a mode, while cancellation or failure leaves `On this device` unavailable and creates no project.
- Given the user has not selected a storage mode, when project creation is evaluated, then creation is blocked without silently choosing a mode.
- Given one user has an on-device project, when another project is created, then hosted storage can be chosen without changing the first project.
- Given on-device storage is chosen, when the project is created, then no account is required and project data remains under the device boundary.
- Given hosted storage is chosen, when creation completes, then an authorized identity protects data that persists independently from the device.
- Given either storage mode is chosen and project creation commits, when the new project's dashboard opens, then it shows the linked repository, selected authoritative storage mode, and current connection status.
- Given a project changes storage mode, when migration succeeds, then stable project and repository identities remain unchanged and exactly one copy is authoritative.
- Given migration fails, when failure is reported, then the prior active copy and mode remain usable and no repository content changes.
- Given a hosted project moves on-device, when the transition commits, then the hosted project and every related hosted copy are marked deleted, hidden from ordinary access, and assigned a two-year cleanup deadline.
- Given a soft-deleted hosted copy exists, when normal lists, search, collaboration views, or APIs are used, then the copy is absent and cannot be manually opened or restored.
- Given resynchronization starts before cleanup, when versions are compatible and conflicts are resolved under the approved rules, then only authorized changes since the retained baseline are synchronized.
- Given resynchronization starts after cleanup, when hosted storage is reactivated, then a full upload preserves the stable project and repository connection identities.
- Given cleanup reaches the deadline, when retention enforcement runs, then every project-scoped primary, derived, backup, export, and processor copy is permanently deleted except approved anonymous analytics and legal records.
- Given analytics contain an identifier or allow singling out, linkability, inference, or reconstruction, when retention is evaluated, then the data is rejected as anonymous and governed as personal data.
- Given a legal exception delays deletion, when the retained record is reviewed, then its legal basis, minimum fields, access, rights behavior, and deletion deadline are explicit.
- Given a data-subject request applies, when it is verified and executed, then every governed copy and processor follows the approved response and lifecycle.

## Open Questions

- Which data model and transaction protocol maintain one authoritative copy during migration?
- How are versions, changes, deletions, conflicts, retries, and compatibility represented for incremental synchronization?
- How is full-upload rehydration verified after baseline cleanup?
- Which project records and processors require special cleanup propagation or lawful retention?
- Which anonymous aggregate metrics are necessary, what minimum thresholds and disclosure tests apply, and how long is each retained?
- Which entity is controller or processor for hosted storage, local workers, agents, infrastructure, analytics, and future collaboration?
- Which purposes, lawful bases, retention schedules, rights workflows, subprocessors, transfers, breach processes, and impact reviews apply?
- How are backup and processor deletion deadlines enforced and evidenced?
- Which storage architecture and verification commands satisfy the lifecycle contract?
