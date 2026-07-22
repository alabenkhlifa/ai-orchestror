# Project Storage Lifecycle

## Status

Draft

## Outcome

A user can choose on-device or SDD Orchestrator-hosted storage for each project's SDD data, change that choice later without modifying the linked repository, and rely on defined synchronization, retention, cleanup, privacy, and analytics behavior.

## Users

- Project contributors choosing where SDD specifications, tasks, agent records, and artifacts are stored.
- Authorized colleagues who may later collaborate on hosted project data.
- Privacy, operations, and support personnel enforcing approved lifecycle workflows.

## Primary Workflow

1. During GitHub or local repository onboarding, the user chooses on-device or hosted project-data storage for that project.
2. The project is created with one explicit authoritative storage mode.
3. The user may keep on-device and hosted projects in the same catalog.
4. The user may later request a direct storage-mode change without export and import.
5. The destination is transferred and verified before it becomes authoritative.
6. Moving hosted data on-device marks the hosted project and all related hosted copies deleted, hides them from ordinary access, and starts a two-year cleanup deadline.
7. Returning to hosted storage before cleanup synchronizes changes against the retained baseline.
8. Returning after cleanup performs a full upload while preserving stable project and repository identity.
9. Retention enforcement permanently removes project-scoped hosted data at the deadline except genuinely anonymous analytics and separately lawful minimum legal records.

## In Scope

- Per-project on-device or hosted storage selection for GitHub and local repositories.
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

- Given a GitHub or local repository is selected, when project-data storage is chosen, then on-device and hosted modes are both available under their prerequisites.
- Given one user has an on-device project, when another project is created, then hosted storage can be chosen without changing the first project.
- Given on-device storage is chosen, when the project is created, then no account is required and project data remains under the device boundary.
- Given hosted storage is chosen, when creation completes, then an authorized identity protects data that persists independently from the device.
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
