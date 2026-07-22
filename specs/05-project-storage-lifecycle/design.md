# Project Storage Lifecycle Design

## Context

Repository location does not determine where SDD project data should live. Users need per-project device or hosted storage, direct migration, and a predictable privacy lifecycle. Hosted-to-device migration also creates a retained hosted baseline whose access and cleanup must be strictly limited.

## Proposed Approach

Represent storage mode as an explicit project-level boundary. Migrate through a staged destination, verify completeness and compatibility, then atomically switch authority. Treat hosted-to-device movement as activation of the device copy plus isolated hosted soft deletion with an enforced two-year deadline. Reuse the retained version for incremental return to hosted storage, or perform a full upload after cleanup.

Apply one processing inventory and enforceable retention contract across primary and derived storage, processors, logs, backups, exports, analytics, and legal exceptions.

## Components Affected

- Project creation and storage selection.
- Device and hosted project-data persistence.
- Storage migration and authority switching.
- Versioning, change tracking, conflict resolution, and resynchronization.
- Soft deletion, access isolation, cleanup scheduling, backup and processor propagation.
- Project catalog storage and availability state.
- Analytics anonymisation and legal-retention boundaries.
- GDPR processing inventory, rights workflows, security controls, and audit evidence.

## Data and Access Boundaries

- `StorageMode`: `device` or `hosted` for one project.
- `ProjectDataCopy`: one versioned device or hosted representation with explicit authority state.
- `SyncBaseline`: the latest retained hosted version used for authorized resynchronization.
- `DeletionSchedule`: deletion time and permanent-cleanup deadline for every project-scoped hosted copy.
- `RetentionPolicy`: enforceable lifecycle across primary and derived storage and processors.
- `AnalyticsRecord`: aggregate genuinely anonymous data with no stable or linkable identifiers.
- `LegalRetentionRecord`: independently lawful minimum record with its own deadline.
- `DataProcessingRecord`: approved processing purpose, basis, fields, access, lifecycle, rights, processors, transfers, and review.

Required boundaries:

- Every project-data record has one project and one storage mode.
- Exactly one copy is authoritative after a completed migration.
- The repository and its stable connection are never migration payload side effects.
- Soft-deleted hosted data is isolated from ordinary reads and available only to approved lifecycle workflows.
- Anonymous analytics has no join path back to personal or project data.
- Legal-retention records are separated from project content and ordinary product access.
- Rights, retention, and deletion propagate across every copy and processor under the approved contract.

## Interfaces

- Storage-selection interface: present device and hosted choices without implying repository or agent location.
- Migration interface: stage, validate, activate, fail safely, retry, and report one authoritative copy.
- Retention interface: mark all hosted project data deleted, isolate it, schedule cleanup, and enforce propagation.
- Resynchronization interface: compare against a retained baseline or perform full rehydration while preserving stable identity.
- Conflict interface: detect incompatible versions and require approved resolution before authority changes.
- Rights interface: authenticate and execute applicable data-subject requests across all governed copies.
- Analytics interface: aggregate and irreversibly anonymise permitted metrics before retention and test disclosure risk.
- Legal-retention interface: create only separately approved minimum records and enforce their deadlines.

## Decisions and Tradeoffs

### Per-Project Storage Choice

- Choice: Let each project independently use device or hosted storage regardless of repository source.
- Reason: Storage, repository, and agent locations solve different user needs.
- Consequence: Catalog, authorization, migration, backup, and collaboration logic must preserve explicit storage state.

### Direct Migration

- Choice: Change storage mode directly rather than requiring export and import.
- Reason: A mode change is a lifecycle operation on the same stable project.
- Consequence: The system needs staged transfer, verification, atomic authority change, and failure recovery.

### Two-Year Hosted Retention

- Choice: Retain an isolated deleted hosted copy for two years after moving on-device, then clean it up completely.
- Reason: The retained version supports incremental resynchronization during the agreed period.
- Consequence: Every derived copy and processor requires an enforceable deadline; ordinary access and manual restore remain prohibited.

### Full Upload After Cleanup

- Choice: Use incremental synchronization while a baseline exists and full upload after it is deleted.
- Reason: No legitimate baseline remains after permanent cleanup.
- Consequence: Stable project identity must survive both paths and compatibility must be validated before hosted activation.

### GDPR By Design And Default

- Choice: Require an approved processing and lifecycle contract before schema or backend approval.
- Reason: Project data, identities, agents, logs, exports, and processors can contain personal or sensitive information.
- Consequence: Technical checks provide evidence but do not replace accountable privacy or legal approval.

### Anonymous Aggregate Analytics Only

- Choice: Retain analytics only after aggregation and genuine anonymisation prevent singling out, linkability, inference, and reconstruction.
- Reason: Analytics must not extend deleted project or identity lifecycles.
- Consequence: Pseudonyms and hashes remain personal data; metrics need thresholds, disclosure testing, and independent retention.

## Risks

- Migration failure can create divergent or incomplete copies. Verify before activation and preserve the prior authority on failure.
- Incremental synchronization can miss deletes or overwrite concurrent changes. Define immutable versions, conflict rules, and compatibility checks.
- Soft-deleted data can remain accessible longer than expected. Isolate it from product reads and enforce the deadline across every copy.
- Backups and processors can outlive primary deletion. Contract and verify propagation and documented exceptions.
- Analytics can remain identifiable through rare values or joins. Prohibit stable identifiers and require disclosure-risk testing.
- Fixed retention can conflict with rights or law. Record category-specific purpose, basis, exceptions, and deadlines with required review.
- Full upload after cleanup can duplicate identity or repository links. Preserve stable IDs and validate destination uniqueness before activation.

## Open Questions

- Which version, transaction, and authority model supports migration and resynchronization?
- Which conflict, deletion, retry, and compatibility rules apply?
- How are cleanup deadlines propagated and evidenced across backups, exports, logs, indexes, caches, and processors?
- Which data requires a separate legal-retention record and for how long?
- Which analytics metrics, thresholds, tests, and retention are approved?
- Which controller, processor, purpose, basis, rights, transfer, breach, and impact-review decisions apply?
- Which persistence, worker, hosted-service, and verification architecture implements these contracts?
