# Project Portability Design

## Context

Users need a controlled way to back up, move, or exchange project data independently from direct storage migration. Portable packages cross trust boundaries and can carry sensitive project content, malformed data, unsafe paths, or leaked credentials.

## Proposed Approach

Define an allowlisted, versioned package manifest with integrity metadata and explicit content sections. Export from a consistent project snapshot after secret filtering. Import into isolated temporary processing, validate every structural and safety rule, resolve permitted identity and repository conflicts, then commit the project atomically into the selected storage mode. Repository authorization is re-established separately.

## Components Affected

- Project export and snapshot service.
- Package manifest, schema versions, integrity, and compatibility registry.
- Secret and sensitive-field filtering.
- Upload or local-file intake and isolated temporary processing.
- Import validation and conflict-resolution UI.
- Project identity, naming, storage, and repository reconnection.
- Cleanup, audit, privacy, and data-subject-rights workflows.

## Data and Access Boundaries

- `ProjectPackage`: the versioned portable representation and manifest.
- `PackageSection`: one allowlisted content category with version and integrity metadata.
- `ImportAttempt`: isolated transient validation, conflict, and confirmation state.
- `PackageProvenance`: minimum approved origin and version evidence without credentials or unnecessary identity data.

Required boundaries:

- Export reads only authorized project data from one consistent snapshot.
- Secret filtering occurs before package serialization and is verified after creation.
- Imported files remain isolated until all validation and conflict checks pass.
- Validation never executes package content.
- Temporary data has an approved short lifecycle and cannot appear in ordinary project access.
- Project creation and allowed conflict resolutions commit atomically.
- Repository credentials never cross the package boundary; reconnection uses normal provider or worker flows.
- Package and temporary data remain personal or confidential project data unless proven otherwise and follow the approved lifecycle.

## Interfaces

- Export interface: select one authorized project, show package scope, snapshot it, filter secrets, serialize, and return version and integrity information.
- Package schema interface: define required and optional sections, versions, compatibility, limits, and unknown-field behavior.
- Import intake interface: isolate the package, limit resources, and begin validation without mutation.
- Validation interface: check integrity, format, versions, size, paths, attachments, content types, and forbidden secret categories.
- Conflict interface: identify project, name, repository, duplicate, and storage conflicts and collect only approved confirmations.
- Import commit interface: create the project and related data atomically in the chosen mode.
- Repository reconnection interface: require normal authorization and validation independently from package contents.
- Cleanup and rights interface: enforce temporary, package, log, backup, export, and processor lifecycles.

## Decisions and Tradeoffs

### Separate Portability From Migration

- Choice: Treat export/import as explicit package operations and storage changes as lifecycle operations on the same project.
- Reason: Packages may cross users or environments, while migration preserves one stable project boundary.
- Consequence: Import needs provenance, identity, duplicate, and conflict rules that direct migration does not.

### Allowlisted Versioned Package

- Choice: Export only documented sections under a declared schema version.
- Reason: An allowlist prevents accidental leakage and supports compatibility review.
- Consequence: New project data types require explicit package-version decisions.

### No Accepted Secrets

- Choice: Exclude all authentication, repository, session, worker, agent-provider, and encryption secrets.
- Reason: Portable files leave the normal credential boundary and may be copied or shared.
- Consequence: Imported projects require explicit repository and provider reconnection.

### Validate Before Mutation

- Choice: Isolate and fully validate a package before any persistent project change.
- Reason: Malformed or malicious packages must not create partial state or execute content.
- Consequence: Import needs resource limits, temporary storage, cleanup, and atomic commit.

## Risks

- Secret filtering can miss a new field. Use an allowlisted schema, negative secret tests, and version review.
- Archives can contain path traversal, decompression bombs, unsafe links, or executable content. Isolate parsing, enforce limits, and never execute package contents.
- Compatibility rules can silently drop important data. Make version behavior explicit and user-visible before import.
- Duplicate identity or repository links can corrupt ownership. Preflight canonical identity, name, and repository constraints.
- Temporary package copies can outlive their purpose. Enforce short retention across storage, logs, backups, and processors.
- Package provenance can become unnecessary identity tracking. Minimize it and apply an approved data contract.

## Open Questions

- Which exact package sections and history are required?
- Is repository source ever allowed, and under which separate threat model?
- Which manifest format, compression, integrity, signing, encryption, and compatibility rules apply?
- How are import identity, provenance, duplicates, names, repositories, and allowed resolutions represented?
- Which resource, file-type, attachment, path, and extraction limits are required?
- Which lifecycle, rights, processor, transfer, audit, and privacy approvals apply?
- Which golden fixtures, property tests, compatibility suites, security tests, and browser scenarios prove the package contract?
