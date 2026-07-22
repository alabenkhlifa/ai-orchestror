# Project Onboarding

## Status

Draft

## Outcome

A BA, PO, PM, developer, or other project contributor can enter SDD Orchestrator with GitHub or without a GitHub account and create a personal project linked to exactly one Git repository.

The repository can be hosted on GitHub or remain on the user's computer. Linking a repository prepares the project for later specification and agent workflows without modifying the repository or starting an agent.

## Users

- Business analysts defining and refining product requirements.
- Product owners and product managers organizing work and approving scope.
- Developers and technical contributors who also use the SDD workflow.

## Primary Workflow

1. The entry page presents two primary actions: `Login with GitHub` and `Work without GitHub`.
2. A user who selects `Login with GitHub` authenticates with GitHub, enters their personal workspace, and selects from the repositories available through their granted GitHub access.
3. A user who selects `Work without GitHub` continues to local repository onboarding without being required to authenticate with GitHub.
4. The local path connects to a Git repository on the user's computer through the local-repository mechanism approved for that path.
5. The product derives the default project name from the selected repository, allows the user to edit it, and validates repository and name uniqueness within the personal workspace.
6. The product creates the project and repository connection together, then shows the project and its connection status without starting an AI agent.

## In Scope

- Present `Login with GitHub` and `Work without GitHub` as the two entry-page actions.
- Sign in and sign out with a GitHub account when the GitHub path is selected.
- Continue to local repository onboarding without GitHub authentication when the local path is selected.
- Create or restore one personal workspace for the current user context.
- Show every repository available through the user's authorized GitHub account in a searchable repository picker.
- Create a project by selecting one GitHub repository.
- Offer local repository linking as a separate source option.
- Guide the user through installing and pairing a local worker when no paired worker is available.
- Select and link a Git repository available to the paired local worker.
- Keep local repository content on the user's computer.
- Show the linked repository source and current connection status on the project.
- Assign a default project name from the linked repository name and keep project names unique within the user's personal workspace.
- Edit the project name during onboarding or at any time after project creation.
- Prevent the same repository from being linked to more than one project in the personal workspace.
- Keep a project visible with a disconnected status when its linked GitHub repository is no longer accessible.
- Present authentication, authorization, pairing, validation, and connection failures in language a non-developer can act on.

## Out of Scope

- Shared workspaces, organizations, team membership, roles, or project invitations.
- External identity providers other than GitHub; `Work without GitHub` is a local-repository path, not another external sign-in provider.
- AI-provider authentication, model selection, or coding-agent configuration.
- Specification authoring, approval, implementation, or verification workflows.
- Starting Codex or another coding agent.
- Selecting whether a later AI agent runs locally or remotely; local onboarding describes the repository location, not the agent location.
- Remote workers hosted in the cloud or on user-managed devices such as a Raspberry Pi.
- Uploading or copying a local repository into the control plane.
- Browsing, editing, or executing repository content from the onboarding flow.
- Unlinking, deleting, transferring, or sharing a project.
- Linking multiple repositories to one project.
- Creating multiple projects for the same repository in one personal workspace.
- Selecting an implementation language, framework, database, hosting platform, or Symphony integration strategy.

## Business Rules

- The entry page must show exactly two primary actions: `Login with GitHub` and `Work without GitHub`.
- A GitHub account is not required to start the local repository path.
- Choosing `Work without GitHub` means the repository is local to the user's computer. It does not require the AI agent to run locally or prevent a later remote-agent configuration.
- Each established user context owns one personal workspace.
- A project must be linked to exactly one repository.
- A repository can be linked to at most one project in the same personal workspace.
- The same repository can be linked independently by different users in their separate personal workspaces.
- A project name must be unique within its user's personal workspace using a case-insensitive comparison; another user can use the same project name.
- The default project name is the repository name.
- If the default name is already used by another project in the same personal workspace, ignoring letter case, append the lowest available positive integer suffix: `-1`, then `-2`, and so on.
- A user may edit a project name during onboarding and at any time after creation. Every saved name must satisfy the same case-insensitive, workspace-scoped uniqueness rule.
- A project's stable identity and repository connection must not change when its editable display name changes.
- Repository uniqueness and project-name uniqueness are separate rules. Changing or suffixing the project name must not allow the same user to link the same repository twice.
- GitHub sign-in makes every repository returned by GitHub under the user's granted access visible in the repository picker; visibility does not link a repository automatically.
- A project is created only after the user explicitly selects and confirms a repository.
- Linking a GitHub repository must not modify its files, branches, settings, issues, or pull requests.
- When a linked GitHub repository becomes inaccessible, its project must remain visible and show a disconnected status until access is restored or another future project-management action is approved.
- A local repository must be a valid Git repository and must be selected through a paired local worker.
- A local worker belongs to the current personal workspace and cannot register a project for another workspace.
- Local source files must remain on the user's computer. The control plane may receive only the metadata required to identify the repository and report its connection state.
- Linking a local repository must not modify its files, branches, remotes, or Git configuration.
- A paired worker becoming unavailable must change the repository connection status; it must not remove the project or its recorded link.
- Authentication credentials, repository credentials, session secrets, and worker pairing credentials must never be displayed after they are accepted.

## Acceptance Criteria

- Given a user opens the entry page, when it finishes loading, then it shows `Login with GitHub` and `Work without GitHub` as two distinct primary actions.
- Given a user does not want to authenticate with GitHub, when they select `Work without GitHub`, then they continue toward linking a repository on their computer without being asked for GitHub authentication.
- Given a user selects `Work without GitHub`, when they later configure an AI agent, then the earlier local-repository choice does not by itself restrict that agent to local execution.
- Given a signed-out user, when they complete GitHub sign-in, then they enter their personal workspace under the identity returned by GitHub.
- Given a returning user with a valid session, when they open SDD Orchestrator, then their existing personal workspace and linked projects are restored.
- Given a signed-in user, when they sign out, then protected workspace and project views are no longer accessible without signing in again.
- Given a signed-in user who chooses GitHub as the repository source, when the repository picker loads, then it shows every repository returned by GitHub under the user's granted access and supports finding a repository without requiring its URL.
- Given an unlinked GitHub repository in the picker, when the user confirms it, then one project is created and identifies that repository as its only repository.
- Given a repository named `example` and no project named `example` in the user's personal workspace, when the user links it, then the created project is named `example`.
- Given a repository named `example` and projects named `example` and `example-1` in the user's personal workspace, when the user links the repository, then the created project is named `example-2`.
- Given a repository named `example` and projects named `Example` and `EXAMPLE-1` in the user's personal workspace, when the default name is allocated, then the created project is named `example-2`.
- Given a user is onboarding a repository, when they edit the generated project name to an available name and confirm it, then the project is created with the edited name.
- Given an existing project, when the user changes its name to an available name, then the new name is saved without changing the project's identity or repository connection.
- Given an existing project named `Example`, when the user attempts to save `example` for another project in the same personal workspace, then the conflicting name is not saved and the user receives an actionable message.
- Given two different users with separate personal workspaces, when each user links the same repository or repositories with the same name, then each user can use the unsuffixed project name when it is available in their own workspace.
- Given a GitHub repository already linked in the personal workspace, when the user attempts to link it again, then project creation is blocked and the existing project is identified.
- Given a GitHub authorization or repository-listing failure, when the picker cannot load, then the user sees an actionable recovery message and no partial project is created.
- Given a linked GitHub repository is no longer returned under the user's granted access, when the workspace or project is viewed, then the project remains visible with a disconnected status and guidance for restoring access.
- Given a user who chooses `Work without GitHub` and has no paired worker in the current personal workspace, when the local flow starts, then the product presents guided worker installation and pairing before repository selection.
- Given a successfully paired local worker, when the user selects a valid local Git repository and confirms it, then one project is created and identifies that local repository as its only repository.
- Given a selected local folder that is not a valid Git repository, when linking is attempted, then the project is not created and the user is told how to select a valid repository.
- Given a local repository link, when onboarding completes, then repository content has not been uploaded to the control plane and the local repository has not been modified.
- Given a linked local repository whose worker goes offline, when the user views the project, then the project remains present and its repository connection is shown as unavailable.
- Given any unsuccessful sign-in, pairing, validation, or link attempt, when the operation ends, then no duplicate user workspace, worker, repository connection, or project is created.

## Open Questions

- What identity and persistence boundary owns the personal workspace when a user selects `Work without GitHub`?
- If a user starts without GitHub and later signs in with GitHub, should the existing local workspace be attached to that identity, merged, or remain separate?
