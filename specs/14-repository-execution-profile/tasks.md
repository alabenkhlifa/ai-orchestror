# Repository Execution Profile Tasks

## Status

In Progress

The product and technical contracts are approved. Task 7 is complete, and Task 8 is the next executable task establishing the authoritative assessment state that Task 1 presents. Slice 07 consumption remains a later explicit `update-spec` agreement change.

## Active Slice

Assess one mature repository at one exact commit through a bounded read-only worker scan, let the owner approve one execution profile and pilot specification, and publish the profile capability for managed runtime integration without changing repository files.

## Cross-Specification Dependencies

Requires:

- `capability:project-storage-authority` — provider `specs/05-project-storage-lifecycle#Task 4` — required before `Task 8`.
- `capability:workspace-bound-local-worker-authorization` — provider `specs/02-local-project-onboarding#Task 3` — required before `Task 7`.
- `capability:project-specification-store` — provider `specs/09-project-specification-storage#Task 8` — required before `Task 4`.
- `capability:project-storage-governance` — provider `specs/05-project-storage-lifecycle#Task 6` — required before `Task 5`.
- `capability:project-specification-governance` — provider `specs/09-project-specification-storage#Task 5` — required before `Task 5`.

Provides:

- `capability:repository-execution-profile` — ready after `Task 6`.

## Slice Size Gate

- Slice size: Standard

## Task Size Gate

- Every task is standard, owns one primary outcome, has at most three acceptance criteria and two entities, and has focused proof expected to run in about ten minutes.
- No exception is required.

## Proof Scope Gate

- Applies to: all tasks.

## Implementation Boundary

Included:

- One-root assessment start, disclosure, persistence, and readiness surface.
- Short-lived disclosure-confirmed repository-binding preparation that proves repository identity, normalized root, and current full commit without scanning content.
- Worker-local high-signal scanning, exact-commit cache, cancellation, and structured findings.
- Owner-reviewed immutable execution-profile approval.
- One authoritative pilot specification and revision reference.
- Hosted and device-authoritative lifecycle, privacy, and compatibility proof.

Excluded:

- Repository mutation, kit installation, empty-repository initialization, whole-source indexing or upload, backlog import, and automatic check invention.
- Slice 07 execution-manifest behavior changes.

Deferred after this slice:

- Multiple roots, monorepo subprojects, automatic backlog import, and issue-provider synchronization.
- Slice 07 `update-spec` work that consumes `capability:repository-execution-profile` before managed execution.

Release gates:

- A future approved Slice 07 consumer edge and manifest contract before a production managed run relies on the profile.
- Live configured worker smoke proof for each supported deployment profile.
- Deployment-specific controller, processor, model, worker, region, transfer, notice, retention-enforcement, incident, and accountable privacy or legal evidence.

Traceability:

- Deferred criteria: none
- Release criteria: none
- Deferred entities: none
- Release entities: none

## Parallel Implementation Ownership

- Implementation is partitioned by ownership between `specs/11-ai-runtime-governance#Task 7` and `specs/14-repository-execution-profile#Task 7`, `#Task 8`, plus `#Task 1` (Tasks 14.7, 14.8, and 14.1).
- `specs/11-ai-runtime-governance#Task 7` exclusively owns the personal AI worker transport, including its socket, channel, and any Endpoint registration.
- `specs/14-repository-execution-profile#Task 7` exclusively owns the assessment-specific repository-binding value and metadata adapter after disclosure confirmation. It must not modify the personal AI socket, channel, or Endpoint; any shared transport integration is serialized after Slice 11 Task 7.
- `specs/14-repository-execution-profile#Task 8` exclusively owns repository-assessment persistence and authorization, including its migration, hosted and device-authoritative storage contracts, owner-only start service, and focused domain and adapter proof.
- `specs/14-repository-execution-profile#Task 1` exclusively owns repository-assessment UI, including the route and project navigation, assessment LiveView, disclosure and exact-binding presentation, and focused browser test.
- Repository-wide verification is serialized after the active Slice 11 and Slice 14 task-scoped changes are reconciled. Each parallel task runs only its focused proof and must not modify the other task's owned surfaces.

## Tasks

- [x] Task 7 — Prepare a trusted repository binding after disclosure confirmation.
  - Size: Standard
  - Proof scope: Focused
  - Depends on: none
  - Purpose: Supply Task 1 with one fresh worker-verified repository identity, normalized root, and current full commit without scanning content or trusting owner-entered repository values.
  - Owned surfaces: `RepositoryBindingPreparation` value contract, owner and hosted/device authority, explicit paired-worker selection, processing-boundary confirmation prerequisite, assessment-specific metadata adapter and deterministic double, canonical repository identity proof, one-root selection, repository-relative root normalization and containment, full exact-commit resolution, short expiry, single-use consumption and unchanged revalidation, unknown, malformed, mismatch, stale, replay, unavailable, cross-project and cross-workspace refusal, no absolute path or raw diagnostic return, no durable hosted copy, no scan command, and repository non-mutation fixture.
  - Owns: entity:RepositoryBindingPreparation
  - Proof: Focused domain, authorization, adapter-contract, expiry, replay, stale, identity-mismatch, root-containment, exact-commit, cross-project, cross-workspace, no-hosted-copy, no-scan-command, and unchanged-repository tests pass without modifying the personal AI socket, channel, or Endpoint.

- [ ] Task 8 — Establish authoritative repository-assessment state and storage parity.
  - Size: Standard
  - Proof scope: Focused
  - Depends on: Task 7
  - Purpose: Consume one unchanged trusted binding through an owner-only service and persist one pending assessment in exactly the project's authoritative storage destination without issuing a scan command.
  - Owned surfaces: `RepositoryAssessment` value and state transition, hosted schema and migration, hosted and device-authoritative assessment-store adapters, device-store contract, owner and device authority, project and exact-binding isolation, changed-boundary confirmation record, pending-scan creation, stale and replay refusal, no durable hosted copy for device projects, and no-command or repository-mutation contract.
  - Owns: entity:RepositoryAssessment
  - Proof: Focused domain, migration, owner and device authorization, hosted/device adapter-contract, restart persistence, cross-project, cross-workspace, stale, replay, no-hosted-copy, no-command, and unchanged-repository tests pass.

- [ ] Task 1 — Establish assessment state and owner-controlled start.
  - Size: Standard
  - Proof scope: Focused
  - Depends on: Task 8
  - Purpose: Let the owner review the processing boundary and one verified repository binding, then explicitly create the pending assessment through the authoritative Task 8 service.
  - Owned surfaces: Assessment entry and one-root selection LiveView, hosted and device routes, project navigation, inspected-surface, local-data, transfer, processor, retention, purpose and limit disclosure, first or changed-boundary confirmation interaction, verified repository, normalized-root and full-commit presentation, owner-only start action, and focused desktop/mobile browser scenario.
  - Owns: AC-01, AC-02
  - Proof: Focused LiveView authorization and interaction tests plus one desktop/mobile browser file prove only the owner can confirm and start, every required disclosure and exact-binding field is visible, and no metadata or scan command is issued before confirmation.

- [ ] Task 2 — Implement bounded worker-local repository assessment.
  - Size: Standard
  - Proof scope: Focused
  - Depends on: Task 1
  - Purpose: Gather the smallest reliable repository evidence without executing content or uploading a whole-repository index.
  - Owned surfaces: Read-only worker command, root-containment and exact-commit guards, high-signal allowlist, ignored and prohibited paths, byte/file/time limits, progress, cancellation, structured findings, and no repository mutation enforcement.
  - Owns: AC-03, AC-04
  - Proof: Focused worker protocol, malicious-content, path-escape, ignored-secret, binary, limit, cancellation, mutation-negative, and structured-result tests pass.

- [ ] Task 3 — Add exact-commit caching and owner-approved profiles.
  - Size: Standard
  - Proof scope: Focused
  - Depends on: Task 2
  - Purpose: Reuse only complete unchanged evidence and convert findings into one explicit immutable managed-runtime contract.
  - Owned surfaces: Complete cache key and terminal-state rules, source-relative finding anchors, profile proposal and review UI, immutable `RepositoryExecutionProfile` versions, stale-commit rejection, instruction precedence, command and check normalization, conflict and multi-root blockers, and owner approval.
  - Owns: AC-05, AC-06, AC-07, entity:RepositoryExecutionProfile
  - Proof: Focused cache hit and invalidation, incomplete-result, stale-commit, source-anchor, conflict, profile-version, owner-approval, LiveView, and browser tests pass.

- [ ] Task 4 — Select one pilot and present independent readiness.
  - Size: Standard
  - Proof scope: Focused
  - Depends on: Task 3
  - Purpose: Bound adoption to one authoritative feature and explain what each available workflow may safely do.
  - Owned surfaces: Shared-store specification and revision selector, pilot reference, no-backlog-import guard, assistant/specification/agent-execution/release readiness model and UI, conflict behavior, and missing-check verification blocker.
  - Owns: AC-08, AC-09, AC-10
  - Proof: Focused specification-store consumer, stale-revision, no-copy, no-import, readiness independence, missing-check, LiveView, and browser tests pass.

- [ ] Task 5 — Enforce verification, privacy, lifecycle, and storage parity.
  - Size: Standard
  - Proof scope: Focused
  - Depends on: Task 4
  - Purpose: Prevent unverified delivery claims and keep assessment data inside its approved project and worker boundaries.
  - Owned surfaces: Required-check reliability gate, `Ready for review` compatibility rule, hosted and device authority parity, raw-index locality, minimized result allowlist, role access, changed-boundary records, retention and deletion, redacted logs, processor controls, no analytics, and no secondary use.
  - Owns: AC-11, AC-12
  - Proof: Focused verification-gate, hosted/device parity, project isolation, raw-content negative scan, access, deletion, retention, log-redaction, processor, and no-analytics tests pass.

- [ ] Task 6 — Publish the execution-profile capability.
  - Size: Standard
  - Proof scope: Focused
  - Depends on: Task 5
  - Purpose: Prove an approved profile is deterministic, allowlisted, and ready for a separately approved managed-runtime consumer.
  - Owned surfaces: Managed-runtime profile value, deterministic digest and serialization, authoritative specification-reference compatibility fixture, no-repository-mutation fixture, `capability:repository-execution-profile` readiness write-back, and future Slice 07 `update-spec` handoff.
  - Owns: AC-13
  - Proof: Profile serialization, digest, compatibility, no-specification-copy, and no-repository-write tests pass; capability readiness is recorded; the handoff names the exact Slice 07 agreement change required before consumption.

## Verification Gate

- [ ] Acceptance criteria pass.
- [ ] Hosted and device-authoritative adapter contracts pass.
- [ ] Worker scanner safety, cancellation, cache, and no-mutation suites pass.
- [ ] Authorization, privacy, lifecycle, and no-analytics suites pass.
- [ ] Desktop and mobile assessment, profile approval, pilot, conflict, and readiness browser scenarios pass.
- [ ] `mix check` and all explicit project code-quality commands pass.
- [ ] `npm --prefix assets ci` and `npm --prefix assets run test:e2e` pass.
- [ ] `MIX_ENV=prod mix assets.deploy` and `MIX_ENV=prod mix release` pass.
- [ ] Specification validator and global capability graph pass.
- [ ] Slice 07 consumption remains unimplemented until its explicit `update-spec` change is approved.

## Blocked Decisions

- None.

## Progress Log

### 2026-08-02 - Task 1 boundary refined after implementation preflight

- Completed: Task 1 preflight confirmed `capability:project-storage-authority` is ready but found that the unfinished standard task combined the `RepositoryAssessment` entity and migration, hosted and device persistence adapters, authorization, LiveView/navigation, and browser proof. Split that work without changing product behavior: Task 8 now owns the authoritative assessment state, storage parity, and owner-only start service; Task 1 owns the user-visible disclosure, exact-binding review, confirmation, and start workflow.
- Remaining: Implement Task 8, then Task 1 and Tasks 2–6. Task 7 remains complete and unchanged.
- Failed checks: None. Preflight stopped before Task 1 application changes as required by the Task Size Gate.
- Spec updates: Moved the ready project-storage-authority prerequisite to Task 8, made Task 1 depend on Task 8, reassigned `RepositoryAssessment` entity ownership to Task 8, preserved AC-01 and AC-02 under Task 1, and kept every task focused. The slice remains standard with eight tasks and a longest dependency path of eight.

### 2026-08-02 - Task 7 complete: trusted repository-binding preparation

- Completed: Added the transient `RepositoryBindingPreparation`, owner and device-authority checks, explicit active workspace-worker selection, exact confirmed-disclosure digest gate, metadata-only adapter with unavailable default, worker-local Git reference, dynamically supervised single-use store, expiry and replay refusal, unchanged revalidation, strict result allowlists, identity and root containment, exact full-commit resolution, and no-durable-copy or repository-mutation proof. `application.ex`, `endpoint.ex`, sockets, channels, personal-AI transport, assessment persistence, routes, and UI remain untouched.
- Proof receipt: `Task 7` — scope `Focused` — command `MIX_TEST_PARTITION=141 mix test test/sdd_orchestrator/repository_assessments/repository_binding_preparation_test.exs` — exit `0`.
- Proof receipt: `Task 7` — scope `Focused` — command `mix format --check-formatted lib/sdd_orchestrator/repository_assessments.ex lib/sdd_orchestrator/repository_assessments/binding_store.ex lib/sdd_orchestrator/repository_assessments/repository_binding_preparation.ex lib/sdd_orchestrator/repository_assessments/repository_metadata_adapter.ex lib/sdd_orchestrator/repository_assessments/worker_repository_metadata.ex test/sdd_orchestrator/repository_assessments/repository_binding_preparation_test.exs` — exit `0`.
- Remaining: Implement Task 8, then Task 1 and Tasks 2–6 plus the slice verification gate. Repository-wide verification remains serialized until the completed Slice 11 transport work and this Slice 14 work are reconciled.
- Failed checks: The first focused run exposed an invalid remote call in a guard; the next exposed a test fixture comparing status before its own symlink setup. Both were corrected, and the final receipts above pass.
- Spec updates: Marked only Task 7 complete and made Task 1 the next executable task. Requirements, design, acceptance criteria, ownership, capability edges, and release gates are unchanged.

### 2026-08-02 - Task 7 implementation started

- Completed: `implement-spec` preflight confirmed the Slice 02 workspace-bound worker authorization capability is ready, the seven-task standard slice and seven-task dependency path satisfy their gates, Task 7 has one focused entity boundary, the Slice 11 transport ownership remains isolated, and the specification plus global graph validators pass.
- Remaining: Implement and prove the transient repository-binding value, authorization, worker metadata adapter, expiry, single-use revalidation, fail-closed cases, and repository non-mutation contract.
- Failed checks: None. The shared PostgreSQL container is healthy; this worktree's Elixir dependencies were installed during environment setup before task proof.
- Spec updates: Status changed from `Not Started` to `In Progress`; Task 7 is the active task.

### 2026-08-02 - Trusted repository-binding preparation approved

- Completed: Resolved the Task 1 execution-order gap with a short-lived, disclosure-confirmed `RepositoryBindingPreparation`. Task 7 now owns the worker-verified canonical repository identity, normalized root, current full commit, expiry, single-use revalidation, and fail-closed metadata boundary without scanning content or modifying Slice 11 personal-worker transport.
- Remaining: Implement Task 7, then Task 1 through Task 6 and complete the verification gate.
- Failed checks: None.
- Spec updates: Restored the slice to `Not Started`; made the ready workspace-bound worker capability required before Task 7; made Task 1 depend on Task 7; added the slice-size and proof-scope gates; and kept repository-wide verification serialized with Slice 11.

### 2026-07-31

- Completed: Approved the mature-repository assessment, owner-approved profile, one-pilot, source-locality, readiness, privacy, capability, and future Slice 07 handoff contracts.
- Remaining: Implement Tasks 7 and 1–6 and complete the verification gate.
- Failed checks: None.
- Spec updates: Created the initial approved specification and first executable slice.
