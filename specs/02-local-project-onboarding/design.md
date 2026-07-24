# Local Project Onboarding Design

## Context

The product must support repositories that remain on the user's computer and users who do not authenticate with GitHub. The dashboard cannot directly trust or reach a local filesystem, so a paired local worker forms the repository boundary.

## Proposed Approach

Use an accountless device workspace for on-device projects. For the first executable slice, discover or graphically install a macOS worker, pair it explicitly to that workspace, open the native folder picker, and validate the selected repository locally. Before any approved onboarding metadata leaves the device for the first time, disclose the data boundary and accountless recovery limit and require confirmation. Return only minimum connection and compatibility metadata, create the project through the same stable identity, naming, and repository-uniqueness contracts as the GitHub path, then open the new project's dashboard.

Preserve projects when the worker is reinstalled or a repository moves. Replacement workers require explicit re-pairing, and moved repositories reconnect through `Locate repository` only after canonical identity matches.

Do not represent repository reconnection as recovery of lost device-workspace history. That history can be recovered only by importing a previous export; otherwise the repository starts new project history.

Hosted storage invokes the separate passwordless and storage specifications; it is not implemented implicitly by worker pairing.

Implement the local and GitHub paths as separate slices, but hold the first usable release until both paths and every shared dependency they invoke pass coordinated entry-surface verification.

## Components Affected

- Shared entry surface and local onboarding UI.
- Accountless device-workspace persistence.
- macOS local worker package, lifecycle, and status surface.
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
- Local paths, remote URLs, filenames, Git history, and source content do not leave the device during onboarding.
- Metadata leaving the device is limited to the minimum connection and compatibility contract and covered by an approved data contract.
- First-use confirmation precedes outbound onboarding metadata. The disclosure remains accessible and requires confirmation again only when the disclosed handling changes.
- A repository connection does not contain enough information to reconstruct lost accountless project history; recovery requires a previous export.
- Authentication changes catalog composition, not ownership or storage of accountless projects.
- Catalog composition uses stable project identity, not repository similarity, to decide whether an item represents one project or separate projects.

## Interfaces

- Worker discovery interface: report whether a compatible paired worker is available.
- Pairing interface: create, expire, confirm, revoke, and replace a workspace-bound credential.
- Local repository interface: let the user select a path, validate Git state, and return only approved canonical identity and status metadata.
- Local selection interface: open the operating system's folder picker, then display the selected repository name and location without requiring manual path entry.
- Privacy disclosure interface: before the first outbound onboarding exchange, explain what remains local, what is shared, and the accountless recovery limit; record confirmation without requiring it for every unchanged connection.
- Recovery interface: pair a replacement worker explicitly and locate a moved repository without changing project identity or accepting a different repository as a replacement.
- Project-history recovery interface: direct users with a previous export to the import workflow and otherwise establish new history without presenting reconnection as recovery.
- Project registration interface: enforce naming and repository uniqueness and commit project plus connection atomically.
- Connection-status interface: distinguish connected, unavailable, authorization-required, and invalid states.
- Post-creation navigation interface: after atomic creation succeeds, open the new project's dashboard with its repository, storage mode, and connection status; creation failure remains in onboarding without exposing a partial dashboard.
- Catalog interface: show distinct project identities separately even when they share a repository, and show one entry for an explicitly migrated or resynchronized stable project using its authoritative storage mode.

## Decisions and Tradeoffs

### Coordinated First Usable Release

- Choice: Release the first usable version only when `Login with GitHub` and `Work without GitHub` both complete their specified onboarding paths.
- Reason: The entry surface presents both choices as primary actions, so a disabled, placeholder, or dead action would misrepresent the product.
- Consequence: The two paths retain separate specification and implementation ownership, but neither can ship alone as the first usable release. Shared entry, storage-selection, and other invoked dependency boundaries require coordinated browser proof.

### Open The New Project After Creation

- Choice: Open the newly created project's dashboard immediately after local onboarding succeeds.
- Reason: The user should arrive at the project they just connected instead of navigating back through the catalog.
- Consequence: The destination dashboard must show the linked repository, selected storage mode, and current connection status. Navigation occurs only after atomic creation commits; a failure remains in onboarding.

### macOS First Worker Slice

- Choice: Support macOS in the first executable local-worker slice, then add Windows and Linux in later slices.
- Reason: Packaging, signing, permissions, updates, and verification differ by operating system and would make the first worker slice too broad.
- Consequence: The worker boundary must remain portable, but the active implementation and verification gate cover only approved macOS versions.

### Native Repository Selection

- Choice: Select repositories through the operating system's folder picker and show the accepted repository name and location after selection.
- Reason: BA, PO, PM, and other non-technical users should not need to understand or enter filesystem paths.
- Consequence: Path access remains inside the worker and local UI boundary; outbound metadata still requires a separate approved contract.

### Explicit Recovery Without Project Loss

- Choice: Preserve projects across worker replacement and repository moves. Require explicit re-pairing for a replacement worker and canonical-identity confirmation before reconnecting a relocated repository.
- Reason: A missing worker or moved path is a recoverable connection problem, not project deletion or permission to substitute another repository.
- Consequence: The UI needs visible pairing and `Locate repository` recovery states, while the technical design must define durable workspace and repository identities.

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

- Choice: Keep local paths, remote URLs, filenames, Git history, and source code on the device during onboarding; share only minimum connection and compatibility metadata.
- Reason: Local repositories may be private or unavailable through a hosted provider.
- Consequence: The technical data contract and canonical identity mechanism must operate within this boundary. Later agent operations require their own explicit data contract.

### First-Connection Disclosure

- Choice: Explain what remains local, what is shared, and the accountless data-loss limit before the first outbound onboarding exchange. Require confirmation once and again only if the disclosed handling changes.
- Reason: Users need an informed choice without being interrupted by the same confirmation on every connection.
- Consequence: Declining confirmation stops the exchange, while the accepted disclosure remains accessible for later review.

### Export-Only Project-History Recovery

- Choice: Recover lost accountless project history only from a previous export. Reconnecting the repository without an export starts new project history.
- Reason: Repository contents cannot reconstruct SDD decisions and project data that existed only in the lost device workspace.
- Consequence: The product must warn users about this limit and integrate recovery with the import workflow instead of implying that repository reconnection restores history.

### Stable Project Identity In The Combined Catalog

- Choice: Keep different stable projects as separate entries even when they link to the same repository. Show an explicitly migrated or resynchronized stable project once with its authoritative storage mode.
- Reason: Repository similarity does not prove that two independently owned project histories are the same project.
- Consequence: Catalog composition must use stable project identity and remain non-mutating. Exact labels and visual grouping are design decisions, but storage mode and device availability remain visible.

## Risks

- Pairing compromise could grant machine access. Bind attempts and credentials to one workspace, expire incomplete attempts, and make workers visible and revocable.
- Full paths and repository metadata may reveal sensitive machine or organization information. Define and test the minimum outbound fields.
- A vague disclosure could create false expectations about locality or recovery. State the approved boundary and loss consequence before first connection and keep it available afterward.
- Users may mistake repository reconnection for project-history recovery. Distinguish connection recovery, export import, and new project history.
- Worker unavailability can make a project look deleted. Preserve the project and expose connection state separately.
- Different paths, worktrees, clones, and remotes can defeat naive duplicate detection. Define canonical local repository identity before implementation.
- A replacement worker or moved path could be accepted too broadly. Require explicit pairing and canonical-identity confirmation before access or reconnection.
- macOS-only delivery limits the first slice's reach. Keep the worker contract portable and specify Windows and Linux in later slices.
- Users may confuse worker location with later agent location. Use distinct labels and recovery messages.
- Accountless data can be accessed by another person sharing the same OS boundary. State this boundary without implying product-level isolation.
- Repository-based deduplication can hide an independent project or imply an unsafe merge. Use stable project identity and preserve separate entries when identities differ.
- Separate GitHub and local slices can drift at the shared entry and dependency boundaries. Verify both complete paths against the same release candidate.

## Open Questions

- Technical design: Which exact fields and internal identifiers satisfy the minimum connection and compatibility contract without exposing prohibited onboarding data?
- Technical design: Which macOS versions, packaging format, update channel, and signing model apply to the first worker?
- Technical design: Which pairing protocol, credential lifetime, rotation, and revocation model is approved?
- Technical design: Which outbound transport works without inbound public access?
- Technical design: Which canonical identity handles clones, worktrees, moved paths, changed remotes, and replacement workers?
- Technical design: How does this path depend on the storage-selection, passwordless hosted-access, and project-portability specifications?
- Technical design: How does catalog composition prove stable project identity and present separate same-repository projects clearly without mutating either boundary?
- Required verification: Which automated, integration, security, and browser strategy verifies worker behavior on the supported macOS versions?
