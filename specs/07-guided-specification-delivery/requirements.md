# Guided Specification And Delivery

## Status

Draft

## Outcome

A developer or non-developer can turn a feature idea into development-ready requirements on a specification-focused board, explicitly start an AI coding agent, answer blocking questions, and receive a verified implementation with evidence and a preview link when the project supports one.

## Users

- Business analysts, product owners, and product managers defining features without needing strong software-engineering skills.
- Developers defining or reviewing requirements and implementation evidence.
- Feature creators and assigned participants receiving questions about stories they own or are responsible for.
- Authorized project participants answering product questions raised during an agent run.
- Project reviewers deciding whether completed work is acceptable.

## Primary Workflow

1. The user opens a project and creates a feature on its specification-focused Kanban board.
2. The product explains the information and format needed for that feature and helps the user structure the requirements.
3. The AI identifies missing, ambiguous, or conflicting product information, distinguishes blocking findings from non-blocking suggestions, and explains what prevents development readiness.
4. The user resolves every blocking finding and may resolve or dismiss non-blocking suggestions.
5. When no blocking finding remains, the feature is visibly marked development-ready and an explicit `Start development` action becomes available.
6. The user starts development, and an authorized coding agent runs on the configured local or remote worker against an isolated feature branch.
7. The agent implements the approved scope, runs the required checks, captures screenshots when supported, and posts progress and evidence to the feature activity.
8. If a product decision blocks progress, the run pauses, the feature is marked blocked, and the focused question tags the assigned participant when one exists or the feature creator otherwise.
9. An accepted answer is written back to the specification, and the same run resumes from its preserved state.
10. When implementation and verification finish, the agent posts the result, test evidence, and available screenshots to the feature.
11. When the project supports an approved web preview, the completed branch is deployed and its test link is attached.
12. The feature moves to `Ready for review`, and the product notifies the relevant users that the run finished and exposes its evidence, branch, and preview link when available.
13. An authorized user reviews the result and explicitly approves it before the feature moves to `Done`.
14. If the authorized reviewer rejects the result, the review feedback is attached to the feature, which returns to `In development` so work can resume.

## In Scope

- A project-level Kanban board organized around specification and delivery state.
- Five first-release board columns: `Draft`, `Ready for development`, `In development`, `Ready for review`, and `Done`.
- A visible `Blocked` status that does not create a separate board column.
- Guided feature requirement structure for technical and non-technical users.
- AI identification of missing, ambiguous, or conflicting product information.
- Visible development-readiness status and reasons.
- Explicit user-controlled development start.
- Coding-agent execution through a configured local or remote worker.
- Branch-isolated implementation.
- Automated checks and test execution required by the project.
- Screenshot evidence when the application type and execution environment support it.
- Progress, questions, answers, results, and evidence in feature activity and comments.
- Required `Creator` and optional `Assigned` fields for each feature, with participant assignment controls and an `Assign to me` action.
- Durable blocked state, user tagging, accepted-answer write-back, and run resumption.
- Branch preview deployment and test-link attachment when supported.
- Completion notification with the run outcome.
- Human review, explicit approval before a feature is considered done, and feedback-based rejection to resumed development.
- GDPR data protection and lifecycle rules for specifications, comments, runs, evidence, notifications, credentials, and deployment metadata.

## Out of Scope

- General-purpose issue tracking unrelated to specification and delivery.
- Repository, identity, storage, and portability onboarding already owned by `specs/01-` through `specs/06-`.
- Automatic merge to the default branch.
- Production deployment.
- Broad collaboration roles and invitation workflows beyond the authorized participants needed by this feature.
- Worker installation, provisioning, provider authentication, and model-selection experiences.
- Billing, subscriptions, or usage purchasing.
- Support for every application-specific screenshot or preview environment in the first executable slice.

## Business Rules

- The board represents feature specification and delivery state, not a generic task list.
- The first-release board has exactly five lifecycle columns: `Draft`, `Ready for development`, `In development`, `Ready for review`, and `Done`.
- `Blocked` is a visible status, not a lifecycle column. A blocked development run remains in `In development` while showing why it cannot continue.
- Cards cannot be freely dragged between lifecycle columns. A feature changes columns only through the workflow's gated actions and validated outcomes.
- A user interaction must not bypass specification readiness, explicit development start, successful verification, or authorized review.
- Every feature has a required `Creator` field and an optional `Assigned` field; the two fields may identify different authorized participants.
- Any authorized project participant may set or change `Assigned` to any authorized participant in the same project.
- `Assign to me` must set `Assigned` to the authorized participant performing the action.
- A blocking question must tag the participant in `Assigned` when that field has a value; when it does not, the question must tag the feature creator.
- AI guidance must explain what information is expected and why a missing or conflicting item blocks readiness.
- Readiness must be based on the current recorded requirements and must expose unresolved items; it cannot be a hidden score.
- Every readiness finding must be visibly classified as blocking or non-blocking.
- A blocking finding cannot be dismissed or overridden, and `Start development` must remain unavailable until every blocking finding is resolved.
- An authorized user may dismiss a non-blocking suggestion without preventing the feature from becoming development-ready.
- Development must never start automatically when a feature becomes ready; an authorized user explicitly starts it.
- The run must use the approved specification and active implementation slice as its scope.
- An agent must not silently invent or change a product requirement during implementation.
- When a product decision is required, the run pauses and asks one focused question with enough context for the tagged users to answer.
- An accepted blocking answer must be written back to the specification before the run resumes.
- A paused run must preserve its branch, workspace, progress, evidence, and pending question so accepted work is not repeated unnecessarily.
- Implementation runs occur on isolated branches and must not write directly to the default branch.
- The feature activity must distinguish agent progress, user comments, blocking questions, accepted answers, verification evidence, preview deployments, and final outcomes.
- A successful claim requires the project’s required verification to pass. Missing or failed proof must remain visible and must not be represented as successful completion.
- Successful agent execution and verification move the feature to `Ready for review`; an agent cannot move a feature directly to `Done`.
- Only an authorized user may approve a feature in `Ready for review` and move it to `Done`.
- Until authorized approval occurs, the feature must remain outside `Done` even when all agent work and verification have finished.
- An authorized reviewer may reject a feature in `Ready for review`; the rejection must record review feedback, return the feature to `In development`, and make the feedback available when work resumes.
- Screenshots are required evidence only when the feature has a visual result and the configured environment can capture a meaningful view.
- A preview link is provided only when the project has a supported and authorized branch-preview path.
- Preview deployments are non-production and must identify the branch and run that produced them.
- Completion notification must state whether the run is ready for review, failed, or remains blocked and link back to its evidence.
- Secrets used by repositories, agents, workers, model providers, notifications, or deployments must not appear in requirements, comments, evidence, screenshots, logs exposed to users, or analytics.
- Personal data and project content must follow approved purpose, access, retention, deletion, rights, processor, transfer, and security rules.
- Analytics must remain aggregate and genuinely anonymous under the project-wide privacy contract.

## Acceptance Criteria

- Given a user opens the first-release project board, when its lifecycle columns are shown, then they are `Draft`, `Ready for development`, `In development`, `Ready for review`, and `Done`.
- Given an active development run needs a product decision, when the run becomes blocked, then the feature remains in `In development`, displays a visible `Blocked` status and reason, and does not move to a separate blocked column.
- Given a user attempts to drag a card to another lifecycle column, when the board handles the interaction, then the feature state does not change and no workflow gate is bypassed.
- Given a feature satisfies the next workflow gate, when the corresponding authorized action or validated outcome occurs, then the board moves the feature to the resulting lifecycle column.
- Given a feature's `Assigned` field identifies a participant, when the agent posts a blocking question, then that participant is tagged even when `Creator` identifies someone else.
- Given a feature's `Assigned` field is empty, when the agent posts a blocking question, then the participant in `Creator` is tagged.
- Given an authorized project participant chooses another authorized participant for `Assigned`, when the assignment is saved, then the story is assigned to that selected participant.
- Given an authorized project participant selects `Assign to me`, when the action succeeds, then `Assigned` identifies that participant.
- Given a user creates a feature, when guided specification begins, then the product shows the expected requirement structure and identifies missing or unclear product information in understandable language.
- Given one or more blocking findings remain, when readiness is evaluated, then the feature is not marked development-ready, each blocker remains visible, and `Start development` is unavailable.
- Given an authorized user tries to dismiss a blocking finding, when the action is evaluated, then the blocker remains active and development cannot start.
- Given a readiness finding is non-blocking, when an authorized user dismisses it, then the suggestion no longer prevents readiness.
- Given every blocking finding is resolved, when readiness is evaluated, then the feature is marked development-ready and an authorized user can explicitly start development.
- Given development has not been explicitly started, when a feature becomes ready, then no coding agent or deployment begins automatically.
- Given an authorized user starts a ready feature, when the run begins, then the agent works from the approved scope on an isolated branch through the configured worker.
- Given the agent can continue without product input, when it implements the feature, then progress and verification evidence appear in the feature activity.
- Given the agent reaches a product decision it cannot safely make, when it becomes blocked, then the run pauses, preserves its state, tags the relevant users, and posts one focused question.
- Given a tagged user provides an accepted answer, when the answer is written back to the specification, then the same run can resume without silently discarding completed work.
- Given required verification fails, when the run reports its result, then the feature does not claim successful completion and the failed evidence remains visible.
- Given a visual feature and a capable environment, when verification finishes, then meaningful screenshots are attached to the feature evidence.
- Given a configured web-preview path and successful verification, when delivery finishes, then the branch preview is deployed and its test link is attached to the feature.
- Given no supported preview path exists, when delivery finishes, then completion remains possible without presenting a nonexistent link.
- Given implementation and required verification succeed, when the agent run finishes, then the feature moves to `Ready for review` rather than `Done`.
- Given a feature is `Ready for review`, when an unauthorized user or an agent attempts to mark it `Done`, then the transition is rejected.
- Given an authorized user approves a feature in `Ready for review`, when approval is recorded, then the feature moves to `Done`.
- Given an authorized reviewer rejects a feature in `Ready for review`, when the rejection and feedback are recorded, then the feedback appears in the feature activity, the feature returns to `In development`, and work can resume.
- Given the run finishes, when notification is delivered, then it identifies that review is required and links the user to the branch, evidence, and preview when available.

## Open Questions

- Should an available branch-preview deployment start automatically after verification or require explicit approval?
- Which notification channels belong in the first release beyond in-product notifications?
- What evidence is mandatory for different project types before a run may report success?
