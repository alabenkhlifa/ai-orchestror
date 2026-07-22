# Project Portability

## Status

Draft

## Outcome

A user can export a versioned SDD Orchestrator project package and import a compatible package into an available storage mode without exposing accepted secrets, silently overwriting another project, weakening repository uniqueness, or modifying repository content.

## Users

- Project owners backing up or moving a project between environments.
- Colleagues exchanging an approved project package.
- Support and operations personnel diagnosing compatible package failures without accessing secrets.

## Primary Workflow

1. The user selects a project and requests export.
2. The product shows the approved package scope and excludes credentials and secrets.
3. The product creates a versioned integrity-protected package.
4. A user selects a package for import and chooses an available project-data storage mode.
5. The product validates format, version, integrity, size, content safety, and compatibility before mutation.
6. The product identifies project, name, repository, and duplicate conflicts and requires explicit resolution where allowed.
7. The project is imported atomically without modifying a repository, and any required repository reconnection remains explicit.

## In Scope

- Explicit export of one project through a documented versioned package.
- Package integrity, compatibility, size, and content validation.
- Secret and credential exclusion.
- Import into an available on-device or hosted storage mode under its normal prerequisites.
- Stable or newly allocated project identity rules.
- Project-name, repository, duplicate, and existing-project conflict handling.
- Explicit repository reconnection without repository mutation.
- GDPR export, import, retention, deletion, processor, and audit boundaries.
- Actionable validation and compatibility failures.

## Out of Scope

- Direct storage-mode migration, defined in `specs/05-project-storage-lifecycle/`.
- Repository hosting migration or Git source transfer unless explicitly approved in this specification.
- Authentication, repository, session, worker, or agent credentials.
- Silent replacement or merge of an existing project.
- Collaboration membership or permission transfer.
- Executing imported artifacts or repository code during validation.

## Business Rules

- Export and import are explicit user actions and are not required for a direct storage-mode change.
- Every package has a declared schema version and integrity protection.
- Exported content must follow a documented allowlist; data absent from the allowlist is excluded.
- Packages must not contain authentication credentials, GitHub or repository credentials, session secrets, magic-link material, worker pairing credentials, agent-provider secrets, encryption keys, or other accepted secrets.
- Collaboration memberships, roles, invitations, and permissions are excluded until a collaboration specification defines safe transfer behavior.
- The package must disclose whether repository source files are included; source inclusion remains blocked until explicitly approved.
- Import validates format, version, integrity, size, path safety, attachment types, and content limits before creating or changing records.
- Package validation must not execute imported code, scripts, hooks, or artifacts.
- Unsupported, corrupt, tampered, oversized, or unsafe packages are rejected without partial records.
- Import must not silently overwrite, merge with, or mutate an existing project.
- Project-name conflicts use the workspace's case-insensitive uniqueness rules and require an approved explicit resolution.
- Repository uniqueness remains enforced; an imported package cannot create a second project for the same canonical repository in one workspace.
- Repository connections and authorization are not assumed transferable; reconnection requires explicit user selection and normal provider or worker validation.
- Importing or reconnecting must not modify repository files, branches, remotes, settings, or Git configuration.
- The selected storage mode must satisfy the normal device or hosted identity prerequisites before import commits.
- Import commits atomically or leaves no partial project, package record, attachment, or repository connection.
- Package files, temporary extraction data, validation logs, and imports follow approved retention and cleanup rules.
- Export and import personal data require approved purposes, lawful bases, access, rights behavior, processors, transfers, retention, deletion, audit, and privacy review.

## Acceptance Criteria

- Given an export is requested, when the package is created, then it has a declared version, integrity data, and the approved project content only.
- Given exported package contents are inspected, when secret categories are searched, then no accepted credential, token, session secret, pairing secret, or provider key is present.
- Given a package includes a field outside the approved schema, when validation runs, then it is rejected or ignored only according to the explicit compatibility rule.
- Given a package is corrupt, tampered, unsupported, oversized, or unsafe, when import is attempted, then no project or partial data is created.
- Given a compatible package and valid storage prerequisites, when import has no conflict, then one project is created atomically in the chosen mode.
- Given the imported name conflicts case-insensitively, when import continues, then no silent rename occurs and the approved user-confirmed resolution is required.
- Given the package references a repository already linked in the workspace, when import is evaluated, then duplicate linking is blocked.
- Given repository authorization is absent, when project data is imported, then the project remains unconnected or requires explicit reconnection without exposing stale credentials.
- Given explicit reconnection succeeds, when repository state is inspected, then repository content and settings remain unchanged.
- Given an import fails after temporary extraction, when cleanup runs, then temporary files and partial processing records follow the approved deletion contract.
- Given a data-subject request applies to exported or imported data, when verified, then the approved rights and lifecycle behavior covers packages, temporary files, logs, backups, and processors.

## Open Questions

- Which project fields, specification history, tasks, run history, artifacts, comments, attachments, repository metadata, and audit evidence belong in the package?
- Does any package ever include repository source files, and what security model would govern them?
- How are stable project identity, copy identity, duplicate imports, and provenance represented?
- Which name and repository conflict resolutions are permitted during import?
- Which package format, schema versioning, integrity, encryption, signing, size, attachment, and path-safety rules apply?
- How are repository reconnection and authorization represented without exporting credentials?
- Which retention, deletion, rights, processor, transfer, audit, and privacy rules apply to packages and temporary data?
- Which interoperability and verification strategy proves backward and forward compatibility?
