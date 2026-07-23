# Local Project Onboarding Design

## Context

The product must support repositories that remain on the user's computer and users who do not authenticate with GitHub. The dashboard cannot directly trust or reach a local filesystem, so a paired local worker forms the repository boundary.

## Proposed Approach

Use an accountless device workspace for on-device projects. Discover or install a local worker, pair it explicitly to that workspace, validate a user-selected path locally, and return only approved repository identity and availability metadata. Create the project through the same stable identity, naming, and repository-uniqueness contracts as the GitHub path, then open the new project's dashboard.

Hosted storage invokes the separate passwordless and storage specifications; it is not implemented implicitly by worker pairing.

Implement the local and GitHub paths as separate slices, but hold the first usable release until both paths and every shared dependency they invoke pass coordinated entry-surface verification.

## Components Affected

- Shared entry surface and local onboarding UI.
- Accountless device-workspace persistence.
- Local worker package, lifecycle, and status surface.
- Pairing and credential management.
- Local Git repository selection and validation.
- Project registration, naming, and connection state.
- Post-creation project-dashboard handoff.
- Combined project catalog boundary.
- Privacy, diagnostics, and security controls for device metadata.

## Data and Access Boundaries

- `DeviceWorkspace`: the accountless ownership boundary available to the current operating-system user.
- `LocalWorker`: an installed endpoint paired to one workspace with replaceable credentials.
- `PairingAttempt`: short-lived state binding one user-confirmed worker and workspace.
- `RepositoryConnection`: stable local repository identity, approved display metadata, and availability state.
- `Project`: stable project identity and display name created for one repository.

Required boundaries:

- The operating-system user and filesystem permission model is the trust boundary for accountless on-device data.
- Pairing grants one workspace access to one worker; credentials are not transferable between workspaces.
- Repository validation and source access run on the worker.
- Source content does not cross into hosted control-plane persistence during onboarding.
- Metadata leaving the device is minimized and covered by an approved data contract.
- Authentication changes catalog composition, not ownership or storage of accountless projects.

## Interfaces

- Worker discovery interface: report whether a compatible paired worker is available.
- Pairing interface: create, expire, confirm, revoke, and replace a workspace-bound credential.
- Local repository interface: let the user select a path, validate Git state, and return only approved canonical identity and status metadata.
- Project registration interface: enforce naming and repository uniqueness and commit project plus connection atomically.
- Connection-status interface: distinguish connected, unavailable, authorization-required, and invalid states.
- Post-creation navigation interface: after atomic creation succeeds, open the new project's dashboard with its repository, storage mode, and connection status; creation failure remains in onboarding without exposing a partial dashboard.
- Catalog interface: compose device and hosted project references without implicit upload or reassignment.

## Decisions and Tradeoffs

### Coordinated First Usable Release

- Choice: Release the first usable version only when `Login with GitHub` and `Work without GitHub` both complete their specified onboarding paths.
- Reason: The entry surface presents both choices as primary actions, so a disabled, placeholder, or dead action would misrepresent the product.
- Consequence: The two paths retain separate specification and implementation ownership, but neither can ship alone as the first usable release. Shared entry, storage-selection, and other invoked dependency boundaries require coordinated browser proof.

### Open The New Project After Creation

- Choice: Open the newly created project's dashboard immediately after local onboarding succeeds.
- Reason: The user should arrive at the project they just connected instead of navigating back through the catalog.
- Consequence: The destination dashboard must show the linked repository, selected storage mode, and current connection status. Navigation occurs only after atomic creation commits; a failure remains in onboarding.

### Explicit Local Worker

- Choice: Access local repositories through a user-installed paired worker.
- Reason: A hosted dashboard cannot safely assume direct local filesystem access.
- Consequence: Onboarding depends on packaging, installation, updates, pairing, transport, status, and revocation behavior.

### Local Means Repository Location

- Choice: Define `Work without GitHub` by repository location, not agent execution location.
- Reason: A local repository may later use a local or remote coding agent.
- Consequence: UI language and state must keep repository, project-data, worker, and agent locations distinct.

### Operating-System Trust Boundary

- Choice: Rely on the current operating-system user and filesystem permissions for accountless projects.
- Reason: Shared-device isolation is an environment responsibility for the first release.
- Consequence: Anyone with access to that boundary may access on-device project data.

### Source Stays Local

- Choice: Persist no repository source in the control plane during onboarding.
- Reason: Local repositories may be private or unavailable through a hosted provider.
- Consequence: Canonical identity, validation, and later agent operations require a durable worker contract and carefully minimized metadata.

## Risks

- Pairing compromise could grant machine access. Bind attempts and credentials to one workspace, expire incomplete attempts, and make workers visible and revocable.
- Full paths and repository metadata may reveal sensitive machine or organization information. Define and test the minimum outbound fields.
- Worker unavailability can make a project look deleted. Preserve the project and expose connection state separately.
- Different paths, worktrees, clones, and remotes can defeat naive duplicate detection. Define canonical local repository identity before implementation.
- Users may confuse worker location with later agent location. Use distinct labels and recovery messages.
- Accountless data can be accessed by another person sharing the same OS boundary. State this boundary without implying product-level isolation.
- Separate GitHub and local slices can drift at the shared entry and dependency boundaries. Verify both complete paths against the same release candidate.

## Open Questions

- Which supported platforms, packaging format, update channel, and signing model apply to the worker?
- Which pairing protocol, credential lifetime, rotation, and revocation model is approved?
- Which outbound transport works without inbound public access?
- Which canonical identity handles clones, worktrees, moved paths, and changed remotes?
- What minimum metadata leaves the device and how is its GDPR lifecycle governed?
- How is accountless device state backed up or recovered?
- How does this path depend on the storage-selection and passwordless hosted-access specifications?
- Which automated and end-to-end strategy verifies worker behavior across supported platforms?
