# Project Onboarding

## Status

Draft

## Outcome

A BA, PO, PM, developer, or other project contributor can sign in without needing strong software-engineering knowledge and create a personal SDD Orchestrator project linked to exactly one Git repository.

The repository can be hosted on GitHub or remain on the user's computer. Linking a repository prepares the project for later specification and agent workflows without modifying the repository or starting an agent.

## Users

- Business analysts defining and refining product requirements.
- Product owners and product managers organizing work and approving scope.
- Developers and technical contributors who also use the SDD workflow.

## In Scope

- Sign in and sign out with a GitHub account.
- Create or restore one personal workspace for the signed-in user.
- Show every repository available through the user's authorized GitHub account in a searchable repository picker.
- Create a project by selecting one GitHub repository.
- Offer local repository linking as a separate source option.
- Guide the user through installing and pairing a local worker when no paired worker is available.
- Select and link a Git repository available to the paired local worker.
- Keep local repository content on the user's computer.
- Show the linked repository source and current connection status on the project.
- Prevent the same repository from being linked to more than one project in the personal workspace.
- Present authentication, authorization, pairing, validation, and connection failures in language a non-developer can act on.

## Out of Scope

- Shared workspaces, organizations, team membership, roles, or project invitations.
- Sign-in providers other than GitHub.
- AI-provider authentication, model selection, or coding-agent configuration.
- Specification authoring, approval, implementation, or verification workflows.
- Starting Codex or another coding agent.
- Remote workers hosted in the cloud or on user-managed devices such as a Raspberry Pi.
- Uploading or copying a local repository into the control plane.
- Browsing, editing, or executing repository content from the onboarding flow.
- Unlinking, deleting, transferring, or sharing a project.
- Linking multiple repositories to one project.
- Creating multiple projects for the same repository in one personal workspace.
- Selecting an implementation language, framework, database, hosting platform, or Symphony integration strategy.

## Business Rules

- GitHub is the only sign-in method for the first version.
- Each authenticated user owns one personal workspace.
- A project must be linked to exactly one repository.
- A repository can be linked to at most one project in the same personal workspace.
- GitHub sign-in makes every repository returned by GitHub under the user's granted access visible in the repository picker; visibility does not link a repository automatically.
- A project is created only after the user explicitly selects and confirms a repository.
- Linking a GitHub repository must not modify its files, branches, settings, issues, or pull requests.
- A local repository must be a valid Git repository and must be selected through a paired local worker.
- A local worker belongs to the authenticated user's personal workspace and cannot register a project for another user.
- Local source files must remain on the user's computer. The control plane may receive only the metadata required to identify the repository and report its connection state.
- Linking a local repository must not modify its files, branches, remotes, or Git configuration.
- A paired worker becoming unavailable must change the repository connection status; it must not remove the project or its recorded link.
- Authentication credentials, repository credentials, session secrets, and worker pairing credentials must never be displayed after they are accepted.

## Acceptance Criteria

- Given a signed-out user, when they complete GitHub sign-in, then they enter their personal workspace under the identity returned by GitHub.
- Given a returning user with a valid session, when they open SDD Orchestrator, then their existing personal workspace and linked projects are restored.
- Given a signed-in user, when they sign out, then protected workspace and project views are no longer accessible without signing in again.
- Given a signed-in user who chooses GitHub as the repository source, when the repository picker loads, then it shows every repository returned by GitHub under the user's granted access and supports finding a repository without requiring its URL.
- Given an unlinked GitHub repository in the picker, when the user confirms it, then one project is created and identifies that repository as its only repository.
- Given a GitHub repository already linked in the personal workspace, when the user attempts to link it again, then project creation is blocked and the existing project is identified.
- Given a GitHub authorization or repository-listing failure, when the picker cannot load, then the user sees an actionable recovery message and no partial project is created.
- Given a signed-in user who chooses a local repository and has no paired worker, when the local flow starts, then the product presents guided worker installation and pairing before repository selection.
- Given a successfully paired local worker, when the user selects a valid local Git repository and confirms it, then one project is created and identifies that local repository as its only repository.
- Given a selected local folder that is not a valid Git repository, when linking is attempted, then the project is not created and the user is told how to select a valid repository.
- Given a local repository link, when onboarding completes, then repository content has not been uploaded to the control plane and the local repository has not been modified.
- Given a linked local repository whose worker goes offline, when the user views the project, then the project remains present and its repository connection is shown as unavailable.
- Given any unsuccessful sign-in, pairing, validation, or link attempt, when the operation ends, then no duplicate user workspace, worker, repository connection, or project is created.

## Open Questions

- Should a project display name always follow the repository name in the first version, or can the user edit it during onboarding?
- When a previously linked GitHub repository is no longer accessible to the user, should the project remain visible as disconnected or be hidden from the workspace?

