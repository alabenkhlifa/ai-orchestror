# GitHub Project Onboarding Tasks

## Status

In Progress

## Active Slice

Deliver GitHub project onboarding end to end: authenticate one user, restore their personal workspace, list every repository under the granted access, select where the project work is saved, create one project for one confirmed repository, and open its dashboard with the repository, storage, and connection state.

## Implementation Boundary

Included:

- Single Phoenix/LiveView application bootstrap, PostgreSQL persistence, local assets, OCI release, and canonical checks selected by this slice.
- Session-aware entry routing, GitHub sign-in, protected session restoration, and sign-out.
- Approved onboarding visual tokens, device-local light and dark theme preference, responsive layouts, keyboard operation, and non-color status cues.
- Personal workspace creation and restoration.
- Existing-workspace catalog routing and the non-mutating `Add project` handoff.
- GitHub App repository-access checking, the dedicated grant screen, installation handoff, and validated return.
- Complete authorized repository catalog retrieval, search, and user-facing states.
- Shared plain-language project-data storage selection before final confirmation.
- Shared `ProjectStorage` contract, hosted storage adapter, device readiness-receipt integration boundary, and atomic project and repository-connection creation.
- Direct handoff to the new project's dashboard with repository, storage, and connection state.
- Workspace-scoped naming and post-creation rename.
- Persistent disconnected project state.
- GDPR data contracts, security controls, and proof for data introduced by the slice.
- Enforcement that Slice 01 emits and retains no product analytics.
- Automated, integration, security, and browser verification.

Excluded:

- Local repository onboarding, device setup and its production storage adapter, passwordless hosted access, identity linking, storage migration, portability, collaboration, and agent execution.
- Remote, cloud, or Raspberry Pi workers.
- Repository editing or source upload.
- GitHub webhook ingestion and background repository synchronization.

Deferred after this slice:

- The separate feature specifications under `specs/02-` through `specs/06-`.
- Monorepo subprojects and multiple projects for one repository in a workspace.

Release boundary:

- This slice may be implemented and verified independently.
- Implementation and local verification may proceed under the approved development privacy contract without selecting a production hosting provider.
- A public hosted deployment remains release-blocked until its deployment privacy profile records the controller contact, processors, regions, transfer safeguards, privacy notice, incident path, retention enforcement, and required reviews.
- The first usable release remains blocked until `specs/02-local-project-onboarding/` and every shared dependency invoked by both onboarding paths also pass their release gates.
- Coordinated browser proof must show that `Login with GitHub` and `Work without GitHub` are both available and complete from the same entry surface.

## Tasks

- [x] Establish the approved application skeleton and canonical development checks.
  - Purpose: Provide only the selected Phoenix, LiveView, PostgreSQL, local-asset, release, configuration, and test foundations required by this slice.
  - Proof: A clean checkout pins the approved runtime and dependencies; `mise install`, `docker compose up -d postgres`, `mix setup`, `mix check`, `mix dialyzer`, `mix deps.audit`, `mix sobelow --config`, the Playwright setup, production asset build, and production release succeed without committed secrets.
  - Status: Complete. All listed proofs pass (see 2026-07-24 bootstrap progress entry). No committed secrets.

- [ ] Implement GitHub identity and protected session behavior.
  - Purpose: Let the user sign in, restore access, and sign out without exposing credentials.
  - Proof: Automated and browser tests cover PKCE and state success, one-time consumption, mismatch, replay, expiry, cancellation, token encryption and refresh, 24-hour idle and 30-day absolute application-session expiry, rotation, restoration, revocation, sign-out return to entry, provider failure, agent isolation, and rejected post-sign-out access.

- [ ] Create and restore the personal workspace.
  - Purpose: Establish the ownership boundary for projects and repository connections.
  - Proof: Tests show stable restoration, isolation between users, no duplicate workspace under retry or concurrency, non-empty workspace routing to the catalog, empty workspace routing to repository selection, and a non-mutating `Add project` handoff.

- [ ] Implement GitHub App repository access and the complete repository catalog.
  - Purpose: Guide non-technical users through repository access when needed, then let them find every repository returned under the validated grant.
  - Proof: Deterministic provider-contract, integration, and browser tests cover `Metadata: read-only`, no webhook dependency, app-JWT pending-request lookup, no accessible installation, the grant screen, state-bound GitHub handoff, untrusted return parameters, authenticated access re-read, pending organization approval and `Check again`, pagination, deduplication by numeric repository ID, search, empty results, personal, private, and organization repositories, authorization failures, rate limits, and provider failure.

- [ ] Implement atomic project and repository linking.
  - Purpose: Create one project for one selected canonical repository and explicit storage mode without partial or duplicate records.
  - Proof: Persistence and fault-injection tests cover the `(workspace, provider, repository ID)` constraint, required storage selection, hosted `Ecto.Multi` initialization, device readiness-receipt validation through the shared adapter, idempotent retry, abort, rollback, concurrency, workspace ownership, and stable identity across repository display changes.

- [ ] Implement project display-name allocation and editing.
  - Purpose: Apply repository defaults, case-insensitive lowest-available suffixes, and safe later renames.
  - Proof: Tests cover preserved natural display names, boundary whitespace, blank and control-character rejection, spaces, Unicode `NFKC` plus default case-fold comparison, no slug conversion, cross-user reuse, case-insensitive conflicts, lowest suffix allocation, concurrent creation and rename, and unchanged stable identities.

- [ ] Preserve project state when GitHub access is lost.
  - Purpose: Treat access loss as a recoverable connection state.
  - Proof: Tests show confirmed access loss disconnects the visible project, a transient provider failure preserves the last confirmed state, no stale credential is exposed, and authenticated revalidation reconnects the same project.

- [ ] Build the end-to-end onboarding and new-project dashboard handoff.
  - Purpose: Complete the workflow without repository URLs or terminal commands.
  - Proof: Desktop and mobile browser scenarios in both themes cover operating-system fallback, device-local manual persistence, no hosted synchronization, sign-in and sign-out continuity, unauthenticated entry, valid-session bypass, sign-in, existing-project catalog routing, empty-workspace continuation, `Add project`, repository-access checking, the grant screen, GitHub handoff, pending organization approval and refresh, valid return, keyboard catalog search and selection, no-match, empty, failure, restricted access, the approved storage copy, unavailable-mode setup, preserved repository and onboarding state, return after setup success, cancellation, or failure, availability refresh without implicit selection, explicit selection, confirmation, naming, duplicate prevention, actionable failures, sign-out, direct new-project dashboard routing, visible repository, storage mode, and connection status, focus visibility, status cues, and text fit.

- [ ] Define and enforce the slice GDPR data contract.
  - Purpose: Make lawful processing, minimization, retention, rights, processors, transfers, no-analytics enforcement, and security part of implementation approval.
  - Proof: The approved processing inventory and automated lifecycle checks cover every field, authorization and onboarding attempt, session, credential, log, cache, backup, export, and configured processor; network and data-store checks prove that no product analytics is emitted or retained; verified rights handling is documented and tested; release checks reject an incomplete deployment privacy profile.

- [ ] Complete security and observability review.
  - Purpose: Diagnose failure without leaking secrets or leaving partial state.
  - Proof: Security tests, browser network review, and structured-log review show no credential, repository name, project name, URL, request-body, external asset, or analytics exposure and sufficient account-neutral diagnostics for every failure path.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Entry routing, authentication, workspace, repository-access grant, repository catalog, storage selection, project-linking, naming, post-creation dashboard routing, and connection-state tests pass.
- [ ] Deterministic GitHub provider-contract tests pass in normal CI, and the tagged live GitHub App smoke test passes in the secret-backed staging environment.
- [ ] `mix format --check-formatted`, `mix compile --warnings-as-errors`, `mix credo --strict`, `mix dialyzer`, `mix deps.audit`, `mix sobelow --config`, and `mix test` pass.
- [ ] `npm --prefix assets ci`, `npm --prefix assets run test:e2e`, `MIX_ENV=prod mix assets.deploy`, and `MIX_ENV=prod mix release` pass.
- [ ] Required desktop and mobile browser scenarios pass.
- [ ] Light and dark theme, operating-system fallback, device-local preference, no-sync, keyboard-only, focus, contrast, non-color status, responsive text-fit, and layout-stability checks pass.
- [ ] PKCE, return validation, credential encryption and refresh, session rotation and expiry, provider revalidation, no-webhook behavior, and secret-isolation checks pass.
- [ ] Hosted storage transaction, device readiness-receipt contract, idempotency, rollback, abort, concurrency, and no-partial-project checks pass.
- [ ] The approved development data contract, retention cleanup, verified rights workflow, no-analytics proof, and deployment-privacy release-blocking checks pass.
- [ ] Browser network and failure-log review proves that credentials, personal display values, external optional assets, and product analytics are absent.
- [ ] New decisions and invalidated proof are written back.

## Blocked Decisions

- None.

## Progress Log

### 2026-07-23 - Specification split checkpoint

- Completed: Narrowed the original project-onboarding specification to the GitHub sign-in, repository discovery, project creation, naming, and disconnected-state slice.
- Remaining: Resolve the listed architecture, integration, storage, privacy, and verification decisions before approval.
- Failed checks: None; implementation has not started.
- Spec updates: Moved local onboarding, hosted passwordless access, identity linking, storage lifecycle, and portability into separate ordered specifications without changing accepted behavior.

### 2026-07-23 - Technical design checkpoint

- Completed: Selected the Phoenix application foundation, GitHub App authorization and installation contract, protected session and credential boundaries, stable repository identity, storage adapter, Unicode name comparison, provider-neutral deployment, and canonical verification toolchain.
- Remaining at this checkpoint: Approve the Slice 01 privacy contract; resolved by the 2026-07-24 checkpoint below.
- Failed checks: None; implementation has not started.
- Spec updates: Removed the resolved engineering questions and identified the then-remaining privacy and legal blocker.

### 2026-07-24 - Privacy contract approval

- Completed: Approved the development-time controller, purposes, lawful bases, data minimization, retention, access, rights, processor role, no-analytics, and cleanup contract.
- Remaining: No active-slice decision blocks implementation. Each public hosted deployment must still complete its deployment-specific privacy release gate.
- Failed checks: None; implementation has not started.
- Spec updates: Separated stable implementation requirements from controller contact, vendor, region, transfer, notice, incident, and final-review evidence that depends on the production deployment.

### 2026-07-24 - Application skeleton bootstrap complete

- Completed: Bootstrapped the single Phoenix application at the repository root and established every canonical development check. Task 1 is done.
- Toolchain (pinned in `mise.toml`): Erlang/OTP 29.0.3, Elixir 1.20.2-otp-29, Node 22.13.1. Phoenix 1.8.9, Phoenix LiveView 1.2.7, Ecto SQL 3.14.0, Bandit 1.12.0 (locked in `mix.lock`).
- Passing proofs: `mise install`; `docker compose up -d postgres` (Postgres 17, healthy); `mix setup`; `mix check` (format-check, compile `--warnings-as-errors`, `credo --strict`, `mix test` = 5 passed) as the standard alias; `mix dialyzer` (0 errors); `mix deps.audit` (no vulnerabilities); `mix sobelow --config`; `npm --prefix assets ci`; `npm --prefix assets run test:e2e` (Playwright/Chromium smoke = 1 passed); `MIX_ENV=prod mix assets.deploy`; `MIX_ENV=prod mix release`.
- Failed checks: None. Secrets remain runtime-only; none committed.
- Deferred: Content-Security-Policy is intentionally not yet enforced. Sobelow's `Config.CSP` is the only ignored check (`.sobelow-conf`, documented). A correct strict CSP needs a nonce/hash for the device-local pre-paint inline theme script, so it is owned by the theme interface and the "Complete security and observability review" task, not the skeleton.
- Local engineering decisions (implementation mechanisms, non-behavioral): the dev/test Postgres publishes host port `5433` (localhost-only) to avoid clashing with an existing local Postgres on 5432; `mix assets.deploy` compiles first so Phoenix 1.8 colocated CSS/JS is generated before Tailwind/esbuild; `mix check` runs under `MIX_ENV=test`; `Credo.Check.Design.AliasUsage` is disabled for Phoenix-generated code.
- Note: Only the skeleton task is complete. The remaining slice tasks are not started; the slice is not `Verified`.
