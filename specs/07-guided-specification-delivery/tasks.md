# Guided Specification And Delivery Tasks

## Status

Blocked

## Active Slice

Deliver one project feature across the `Draft`, `Ready for development`, `In development`, `Ready for review`, and `Done` board columns through explicit start, one branch-isolated configured coding-agent run, durable blocking-question resume, verification evidence, an optional supported web preview, authorized approval or feedback-based rejection, and an in-product completion notification. Show `Blocked` as a status without moving the feature to another column.

## Implementation Boundary

Included:

- One project-scoped feature board with the five approved lifecycle columns, gated action-driven transitions, a separate visible `Blocked` status, and a feature detail workflow.
- Guided requirement structure with visible blocking findings, non-blocking suggestions, and suggestion dismissal.
- Explicit start for one approved specification revision.
- One configured coding-agent and worker boundary without provider-selection UX.
- One isolated feature branch and resumable run.
- Feature creator, project-wide participant assignment, `Assign to me`, assignee-or-creator blocking-question routing, accepted-answer write-back, progress, comments, and typed evidence.
- Required project checks and supported screenshot capture.
- One configured branch-preview path when available.
- `Ready for review` handoff, authorized approval to `Done`, and feedback-based rejection to `In development`.
- In-product action-required and completion notifications.
- Privacy, access, retention, redaction, and audit controls for the slice.

Excluded:

- Multiple concurrent agents on one feature.
- Worker installation, provisioning, or provider setup UX.
- External notification channels.
- Automatic merge, default-branch writes, production deployment, or release management.
- General-purpose issue tracking and broad collaboration administration.

Deferred after this slice:

- Multiple agent and model providers.
- Worker pools, scheduling policies, and cross-worker migration.
- Custom board workflows and organization-wide views.
- Email, chat, mobile, or webhook notifications.
- Merge, release, production deployment, rollback, and preview cleanup policies beyond the first configured path.

## Tasks

- [ ] Establish the feature lifecycle, specification revision, readiness, authorization, and access contracts.
  - Purpose: Make the board and start boundary durable and understandable before agent execution exists.
  - Proof: Domain, permission, and browser tests cover the five lifecycle columns, rejection of free drag-and-drop transitions, gated authorized movement, feature creation with creator and optional assignment, assignment by any authorized project participant to any other authorized participant, `Assign to me`, rejection of unauthorized assignment actions or targets, guided missing information, blocking and non-blocking classification, rejection of blocker dismissal, authorized suggestion dismissal, unavailable start while blocked, readiness changes, revision binding, explicit start authorization, and duplicate-start rejection.

- [ ] Implement one branch-isolated agent run with durable progress and blocking-question resume.
  - Purpose: Execute the approved slice while preserving completed work and routing product decisions back into the specification.
  - Proof: Integration tests cover dispatch, branch isolation, progress, one focused blocked question, visible `Blocked` status while remaining in `In development`, assigned-participant routing, creator fallback, responder authorization, accepted-answer write-back, idempotent resume, cancellation, worker disconnect, and reconciliation.

- [ ] Collect and present verification evidence.
  - Purpose: Let users judge the result from tests, screenshots when supported, branch state, and explicit failures.
  - Proof: Automated and browser tests cover required checks, failed proof, secret redaction, supported screenshot capture, unsupported screenshot disclosure, evidence provenance, and no false success.

- [ ] Deliver an optional branch preview, human-review handoff, and final in-product notification.
  - Purpose: Give users a testable web result when available and reserve accepted completion for an authorized reviewer.
  - Proof: Integration and browser tests cover configured and unavailable preview paths, preview failure, branch and run linkage, non-production labeling, `Ready for review`, rejection of agent or unauthorized completion, authorized approval to `Done`, authorized rejection with feedback to `In development`, resumable work, notification deduplication, authorization, and links to evidence.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Five-column feature lifecycle, gated transition enforcement, project-participant assignment, `Assign to me`, separate `Blocked` status, blocker enforcement, suggestion dismissal, readiness, revision, authorization, and duplicate-start tests pass.
- [ ] Agent dispatch, branch isolation, assignee-or-creator blocked-question routing, write-back, resume, cancellation, and recovery tests pass.
- [ ] Required verification, evidence provenance, screenshot, failure, and secret-redaction tests pass.
- [ ] Configured preview and no-preview scenarios pass without production deployment.
- [ ] `Ready for review`, unauthorized-transition rejection, authorized approval to `Done`, and feedback-based rejection to resumable `In development` scenarios pass.
- [ ] In-product action-required, review-ready, and completion notifications pass.
- [ ] Desktop and mobile board, feature, activity, blocked, review, and completion scenarios pass.
- [ ] GDPR data contract, access, retention, deletion, processor, transfer, audit, and privacy review are complete.
- [ ] Build, formatting, lint, static, security, and canonical test commands pass.
- [ ] New decisions and invalidated proof are written back.

## Blocked Decisions

- Resolve the product questions about preview approval, notification channels, and mandatory evidence.
- Define the durable orchestration boundary for reusing or reimplementing OpenAI Symphony behavior behind the selected Phoenix control plane.
- Define persistent lifecycle, event, idempotency, checkpoint, and reconciliation contracts.
- Define local and remote worker trust, transport, isolation, credential, and agent-provider boundaries.
- Define specification revision, blocking-answer write-back, and resumable agent-context contracts.
- Define evidence, screenshot, preview deployment, notification, retention, redaction, and cleanup contracts.
- Approve the slice GDPR processing inventory and required privacy or legal reviews.
- Define canonical build, test, security, browser, worker, agent, and preview verification commands.

## Progress Log

### 2026-07-23 - Initial product-loop draft

- Completed: Captured the guided specification, readiness, explicit start, autonomous implementation, blocking-question resume, evidence, preview, and notification workflow.
- Remaining: Resolve the listed product decisions before transitioning to feature-specific orchestration and worker design.
- Failed checks: None; implementation has not started.
- Spec updates: Created the core product workflow specification, limited its first executable slice to one configured agent path, and recorded the shared Phoenix control-plane decision from Slice 01.
