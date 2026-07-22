# Project Onboarding Tasks

## Status

Blocked

## Active Slice

Deliver the first usable onboarding path: a user signs in with GitHub, enters a personal workspace, sees all repositories available under their granted GitHub access, links one unlinked repository, and lands on the created project.

## Implementation Boundary

Included:

- Application bootstrap required for this slice after the technology decisions are approved.
- GitHub sign-in, session restoration, and sign-out.
- Personal workspace creation and restoration.
- GitHub repository catalog retrieval, search, loading, empty, and failure states.
- Project and repository-connection creation with the one-to-one repository rule.
- A project summary showing the linked GitHub repository and connection status.
- Automated and browser-level proof for the active acceptance criteria.
- Security checks for session and GitHub credential exposure within this slice.

Excluded:

- Local worker installation, pairing, and local repository linking; these remain the next feature slice.
- Project deletion, unlinking, transfer, or sharing.
- Team workspaces and collaboration.
- AI-provider setup, specification workflows, and agent execution.
- Remote workers, cloud workers, and Raspberry Pi deployment.
- Any Symphony orchestration behavior not required to complete onboarding.

## Tasks

- [ ] Establish the approved application skeleton and canonical development checks.
  - Purpose: Provide only the runtime, UI, persistence, configuration, and test foundations required by this slice.
  - Proof: The documented setup, build, static checks, and empty test suite succeed from a clean checkout.

- [ ] Implement GitHub-backed identity and session behavior.
  - Purpose: Let a user sign in, restore access, and sign out without exposing authentication credentials.
  - Proof: Automated authentication tests and a browser scenario cover successful sign-in, restored session, rejected access after sign-out, cancellation, and provider failure.

- [ ] Create and restore the user's personal workspace.
  - Purpose: Establish the ownership boundary for all projects and repository connections.
  - Proof: Automated tests show one workspace per user, stable restoration across sessions, and isolation between different users.

- [ ] Implement the GitHub repository catalog.
  - Purpose: Let non-technical users find any repository returned under their granted GitHub access without entering a URL.
  - Proof: Integration tests cover pagination, search, empty results, private and organization repositories when returned by GitHub, authorization failure, and rate-limit or provider failure.

- [ ] Implement atomic project and repository linking.
  - Purpose: Create one project for one selected repository while preventing duplicate links or partial records.
  - Proof: Domain and persistence tests cover successful creation, concurrent duplicate attempts, provider identity normalization, rollback on failure, and workspace ownership enforcement.

- [ ] Build the GitHub onboarding and project-summary experience.
  - Purpose: Provide a guided path usable by a BA, PO, PM, or developer without requiring repository URLs or terminal commands.
  - Proof: Browser verification covers sign-in, repository search and selection, confirmation, duplicate prevention, actionable failures, and the resulting project summary at supported desktop and mobile sizes.

- [ ] Complete the slice security and observability review.
  - Purpose: Ensure credentials do not leak and failures can be diagnosed without exposing secrets.
  - Proof: Logs and client-visible payloads contain no session or GitHub secrets, security-focused tests pass, and failed onboarding attempts leave no partial project or repository connection.

## Verification Gate

- [ ] Active-slice acceptance criteria pass.
- [ ] Authentication, workspace, repository catalog, and project-linking automated tests pass.
- [ ] GitHub integration tests pass against the approved test strategy.
- [ ] Build, formatting, lint, and type or static checks pass.
- [ ] Required desktop and mobile browser scenarios pass.
- [ ] Credential and session exposure review passes.
- [ ] Failure-path logs are sufficient and contain no secrets.
- [ ] New product and technical decisions are written back to the specification.
- [ ] Local repository onboarding remains recorded as the next slice.

## Blocked Decisions

- Select the application runtime, UI approach, persistence system, and deployment model.
- Decide how the Symphony foundation participates in the first application architecture.
- Select and configure the GitHub integration model and required permissions.
- Define session, GitHub credential, and application-secret storage and revocation.
- Define the test strategy and canonical build, format, lint, static-check, and browser commands.
- Resolve the requirements questions about project naming and lost GitHub repository access.

## Progress Log

### 2026-07-22

- Completed: Captured the first product-onboarding requirements, logical design, first executable slice, and technology-selection gate.
- Remaining: Review the product questions, select technologies, update the design, and approve the slice before implementation.
- Failed checks: None; implementation has not started.
- Spec updates: Created the initial project-onboarding specification from the user discovery conversation.
