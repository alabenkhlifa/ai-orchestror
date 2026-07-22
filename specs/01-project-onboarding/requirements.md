# Project Onboarding

## Status

Draft

## Outcome

A BA, PO, PM, developer, or other project contributor can enter SDD Orchestrator with GitHub or without a GitHub account, choose where SDD project data is stored, and create a project linked to exactly one Git repository.

The repository can be hosted on GitHub or remain on the user's computer. Linking a repository prepares the project for later specification and agent workflows without modifying the repository or starting an agent.

## Users

- Business analysts defining and refining product requirements.
- Product owners and product managers organizing work and approving scope.
- Developers and technical contributors who also use the SDD workflow.

## Primary Workflow

1. The entry page presents two primary actions: `Login with GitHub` and `Work without GitHub`.
2. A user who selects `Login with GitHub` authenticates with GitHub. If GitHub returns one email marked both primary and verified, both verified addresses satisfy the first-release ASCII matching boundary, and the addresses match under the approved normalization rules, the product preflights an automatic merge into the existing passwordless personal workspace, retains every hosted project from both identities, and completes the merge only when the resulting workspace has no project-name or repository conflict. Secondary GitHub addresses never trigger automatic matching. A project-name conflict pauses the merge and offers a user-confirmed numeric-suffix name; a repository conflict pauses it until the user chooses which project keeps the repository and selects a different repository for the other project.
3. A user who selects `Work without GitHub` continues to local repository onboarding without being required to authenticate with GitHub.
4. After selecting either a GitHub or local repository, the user chooses whether that project's SDD data remains on the current device or is stored by SDD Orchestrator as hosted data.
5. If a user entered without GitHub and selected hosted storage, the product verifies their email address through a passwordless magic link before creating or exposing hosted data.
6. The local path connects to a Git repository on the user's computer through the local-repository mechanism approved for that path.
7. The product derives the default project name from the selected repository, allows the user to edit it, and validates repository and name uniqueness within the workspace.
8. The product creates the project and repository connection together, then shows the project and its connection status without starting an AI agent.
9. The user can export a project and import a compatible project into an available storage mode.
10. The user can later change the project's storage mode directly without using export and import.
11. If the device user later authenticates, the product shows their on-device projects alongside hosted projects without changing either storage mode.
12. After an automatic identity merge, the user can unlink GitHub only after freshly proving access through the verified passwordless email attached to the surviving hosted identity; unlinking preserves the workspace and projects while GitHub-dependent repository connections become disconnected. A later GitHub sign-in cannot reverse that choice automatically and requires fresh passwordless proof and explicit confirmation before re-linking.

## In Scope

- Present `Login with GitHub` and `Work without GitHub` as the two entry-page actions.
- Sign in and sign out with a GitHub account when the GitHub path is selected.
- Continue to local repository onboarding without GitHub authentication when the local path is selected.
- Let the user choose on-device or hosted storage separately for each project's SDD data.
- Offer the same project-data storage choices for GitHub and local repositories.
- Show on-device and hosted projects together after authentication while keeping each project's storage mode visible and unchanged.
- Create or restore a workspace in the selected storage mode.
- Keep on-device project data on the current device.
- Store hosted project data in storage managed by SDD Orchestrator so authorized colleagues can collaborate when collaboration is enabled.
- Authenticate a non-GitHub hosted user with a verified email address and passwordless magic link.
- Automatically merge a GitHub identity with an existing passwordless-email identity only when GitHub's verified primary email and the verified passwordless email satisfy the first-release ASCII matching boundary and match under the approved normalization rules, retaining the existing passwordless personal workspace and every hosted project from both identities without deletion or overwrite.
- Let a user unlink GitHub from a merged hosted identity after fresh passwordless proof while preserving the stable passwordless identity, workspace, projects, and project data.
- Require fresh passwordless proof and explicit confirmation before GitHub can be linked again after a user-initiated unlink; never re-link it automatically from a later matching sign-in.
- Reduce the absorbed GitHub-backed workspace to a minimal inaccessible merge record immediately after a successful merge.
- Show every repository available through the user's authorized GitHub account in a searchable repository picker.
- Create a project by selecting one GitHub repository.
- Offer local repository linking as a separate source option.
- Guide the user through installing and pairing a local worker when no paired worker is available.
- After a successful identity merge, revoke pairings owned by the absorbed workspace and guide the user to re-pair the installed worker with the surviving workspace.
- Select and link a Git repository available to the paired local worker.
- Keep local repository content on the user's computer.
- Show the linked repository source and current connection status on the project.
- Assign a default project name from the linked repository name and keep project names unique within the user's personal workspace.
- Edit the project name during onboarding or at any time after project creation.
- Prevent the same repository from being linked to more than one project in the personal workspace.
- Resolve an automatic-merge repository conflict by letting the user choose which project keeps the repository and select a different repository for the other project before retrying.
- Keep a project visible with a disconnected status when its linked GitHub repository is no longer accessible.
- Export and import projects without exporting accepted credentials or secrets.
- Change an existing project directly between on-device and hosted project-data storage.
- When a hosted project moves to on-device storage, mark its hosted copy and related hosted data as deleted, retain that deleted data for two years, and then clean it up permanently except for retained analytics.
- Apply the two-year cleanup to every project-scoped hosted record and derived copy, including specifications, tasks, agent runs, artifacts, comments, memberships, collaboration records, repository metadata, synchronization baselines, operational logs, caches, search indexes, backups, and exports.
- Resynchronize an on-device project to hosted storage by sending changes made since the latest retained hosted version when that baseline is still available.
- Apply GDPR data-protection requirements to every database record, backend operation, integration, log, export, retention process, and deletion process introduced by this feature.
- Retain only anonymous aggregate analytics that cannot identify or be linked back to a user, colleague, workspace, project, or repository.
- Present authentication, authorization, pairing, validation, and connection failures in language a non-developer can act on.

## Out of Scope

- Collaboration workflows, including invitations, memberships, roles, permissions, and identity-merge membership reconciliation; these require a separate collaboration specification.
- AI-provider authentication, model selection, or coding-agent configuration.
- Specification authoring, approval, implementation, or verification workflows.
- Starting Codex or another coding agent.
- Selecting whether a later AI agent runs locally or remotely; local onboarding describes the repository location, not the agent location.
- Remote workers hosted in the cloud or on user-managed devices such as a Raspberry Pi.
- Uploading or copying a local repository into the control plane.
- Browsing, editing, or executing repository content from the onboarding flow.
- Isolating multiple people who share the same operating-system user profile or filesystem access on one device.
- Automatic identity matching for an address with a non-ASCII local part or domain, or with an IDNA-encoded domain, in the first release; supported provider sign-ins for those addresses remain available as separate identities.
- User-initiated project deletion unrelated to the hosted-copy lifecycle created by a storage-mode change, and general project unlinking or repository replacement outside automatic-merge conflict recovery.
- Linking multiple repositories to one project.
- Creating multiple projects for the same repository in one personal workspace.
- Selecting an implementation language, framework, database, hosting platform, or Symphony integration strategy.

## Business Rules

- The entry page must show exactly two primary actions: `Login with GitHub` and `Work without GitHub`.
- A GitHub account is not required to start the local repository path.
- Choosing `Work without GitHub` means the repository is local to the user's computer. It does not require the AI agent to run locally or prevent a later remote-agent configuration.
- A user choosing the local repository path must also choose whether SDD project data is stored on the current device or in SDD Orchestrator-hosted storage.
- Storage mode is selected per project, not once for the entire workspace.
- The same user may have on-device and hosted projects at the same time.
- Repository source does not restrict project-data storage mode; a GitHub or local repository can use either on-device or hosted project-data storage.
- On-device storage must not require an account and must keep SDD project data available from that device.
- Hosted storage must persist SDD project data independently from the current device and establish an authorized identity before exposing that data.
- A user who enters through `Work without GitHub` and selects hosted storage must verify an email address through a passwordless magic link before hosted project data is created or exposed.
- The non-GitHub hosted path must not require or store a password.
- A magic link must be short-lived, single-use, bound to the intended authentication attempt, invalid after successful use, and protected from disclosure in application data, client-visible payloads, analytics, and logs.
- Requesting a magic link must return the same user-facing response whether or not the email already has an account.
- An invalid, expired, already used, or mismatched magic link must not create a session or expose whether an account exists.
- The verified email address and authentication events are personal data governed by the approved GDPR data contract, retention policy, access controls, and data-subject-rights workflows.
- A GitHub identity and passwordless-email identity must be merged automatically only when the single GitHub address marked both primary and verified matches the verified passwordless email under the approved normalization rules.
- A secondary GitHub email must never be used for automatic matching, even when GitHub marks it verified and it matches the passwordless email.
- A missing, unverified, non-matching, or ambiguous GitHub primary email result must not trigger an automatic merge. Multiple addresses claiming to be primary are ambiguous.
- Secondary GitHub email addresses may be inspected transiently only as part of the provider response needed to identify the primary address. They must not be compared for account matching or retained in application records, analytics, logs, or audit payloads.
- After surrounding whitespace is removed and address structure is validated, automatic matching in the first release is eligible only when both verified addresses contain ASCII characters and no domain label begins with the reserved `xn--` prefix, compared case-insensitively.
- If either verified address is ineligible for first-release automatic matching, the product must skip the merge before local-part, alias, Unicode, or IDNA transformations. It must not normalize Unicode forms, transliterate characters, remove diacritics, map confusable characters, or convert between Unicode and ASCII-compatible domain forms to manufacture a match.
- Skipping automatic matching for an internationalized address must not block a successful GitHub or verified passwordless sign-in that otherwise supports the address. The sign-in methods remain attached to separate hosted identities, and the result must not expose whether another identity exists.
- Base email normalization must first remove leading and trailing whitespace and lowercase the domain. Whitespace inside the address remains invalid and must not be removed to manufacture a match.
- Base normalization must preserve the local part's letter case. Local-part case folding may occur only through an exact-domain and account-type rule backed by official provider documentation that case variants reach the same mailbox.
- Provider-specific local-part rules run only after base normalization and in this order: approved case folding, approved period removal, then approved `+tag` stripping.
- Automatic matching must support provider-aware alias normalization that removes period characters from the email local part and strips the first `+` character and every following local-part character before `@`.
- Dot removal and `+tag` stripping must apply only to email domains whose provider-documented mailbox semantics have been explicitly approved for those transformations. They must never be inferred from the provider that hosts a custom domain.
- Approval is exact-domain and account-type specific. Dot removal and `+tag` stripping are approved independently, and each transformation requires official provider documentation that the resulting addresses reach the same mailbox for that exact boundary.
- For a domain without an approved alias-normalization rule, the local part must remain unchanged for automatic matching. Alias-based automatic merging remains unavailable for that domain.
- Alias normalization is a comparison rule only. It must not rewrite the verified email shown to the user or replace the original verified address used for communication and rights workflows.
- If normalization produces an ambiguous match across more than one hosted identity, automatic merging must stop without exposing account existence or data.
- An automatic identity merge must be idempotent, preserve the existing passwordless user identity and personal-workspace identity, attach GitHub as another sign-in method, and never silently overwrite workspace, project, membership, or repository-link data.
- The existing passwordless personal workspace must be the surviving personal workspace. A separate GitHub-backed personal workspace must not replace it.
- The mere presence of hosted projects on both identities must not be treated as a merge conflict. Every hosted project and its related data from both identities must be retained.
- Before changing either identity or workspace, the product must preflight the combined project set against case-insensitive project-name uniqueness and repository uniqueness in the resulting personal workspace.
- The only project-data conflicts that stop an otherwise valid automatic identity merge are a case-insensitive project-name conflict or a repository that would be linked to more than one project in the resulting personal workspace.
- If preflight finds no project-name or repository conflict, the product must combine all hosted projects as one atomic operation while preserving each project's stable identity, display name, repository connection, and related hosted data.
- If preflight finds a project-name or repository conflict, the entire merge must stop before any identity, workspace, project, or repository-link mutation. Neither account nor any project data may be deleted or overwritten, and the user must receive a safe recovery path.
- For each project-name conflict, the product must suggest the lowest available positive-integer suffix under the existing case-insensitive workspace naming rule: `-1`, then `-2`, and so on.
- A suggested merge-conflict name must not change the project until the user confirms it. Confirmation authorizes that display-name change only as part of a retried atomic merge.
- The product must rerun the complete merge preflight after name confirmation. A newly occupied suggested name or any unresolved repository conflict keeps the merge stopped without changing either account or its projects.
- For each repository conflict, the product must show both affected projects and require the user to choose which project keeps the conflicting repository.
- The other project must be linked to a different valid repository that the user is authorized to select and that is not already linked to another project in the resulting personal workspace.
- Choosing the keeper project or a replacement repository must not mutate either account. The confirmed repository replacement is applied only as part of a retried merge that passes the complete preflight and commits atomically.
- Repository-conflict recovery must preserve both projects, their stable project identities, and all related hosted data. It may change only the explicitly selected project's repository connection to the user-confirmed replacement and must not modify either repository.
- If the user cancels recovery, cannot access a valid replacement repository, or selects a repository that fails validation or uniqueness checks, the merge remains stopped and both identities and all projects remain unchanged.
- Every GitHub-backed hosted project must move into the surviving passwordless personal workspace only as part of the successful atomic merge. Its stable project identity and related hosted data must be preserved.
- After a successful merge, the absorbed GitHub-backed personal workspace must not remain accessible as a second active personal workspace and must be reduced to the approved minimal merge record.
- A failed, cancelled, or blocked merge must leave both personal workspaces and their projects unchanged and independently accessible through their pre-merge identities.
- A successful merge must revoke every local-worker pairing credential bound to the absorbed GitHub-backed workspace. Those credentials must not be transferred to or accepted by the surviving workspace.
- Revoking the old workspace pairing must not uninstall the local worker or modify, move, upload, or delete any local repository or file.
- After the merge, the installed worker must show that pairing is required. The user must explicitly pair it with the surviving passwordless workspace, which issues new workspace-bound credentials.
- Until re-pairing and repository revalidation succeed, affected local repository connections remain recorded but show an authorization-required or unavailable state.
- A failed, cancelled, or blocked merge must not revoke or rotate an existing worker pairing.
- After the merge commits, the absorbed workspace must be reduced immediately to one inaccessible merge record. The product must not retain a soft-deleted copy of the workspace under the project's two-year hosted-data rule.
- The retained merge record may contain only the source workspace ID, surviving workspace ID, merge event ID, merge status, completion time, and approved deletion deadline.
- The retained merge record must not contain project content or identifiers, project names, repository metadata, identity attributes such as email, credentials, worker tokens, sessions, conflict payloads, membership data, analytics join keys, or other absorbed-workspace content.
- The merge record may be accessed only by the narrowly authorized idempotency, security-audit, verified-support, data-subject-rights, retention-enforcement, and deletion workflows approved in its data contract. It must not appear in project or workspace interfaces or ordinary APIs.
- The merge record is personal data. Before implementation, its specific purpose, lawful basis, access boundary, shortest necessary retention period, deletion behavior, rights handling, and required privacy or legal review must be approved.
- The approved deletion deadline must be stored with the record and enforced automatically. A longer legal-retention exception requires a separate minimal legal-retention record under the existing legal-retention rules.
- Project onboarding and its identity-merge flow must not create, reconcile, change, or delete collaboration membership, invitation, role, or permission records.
- Before collaboration data exists, a separate collaboration specification must define how identity merges preserve membership history and authorization without silently widening or removing access.
- Automatic merging must be auditable, disclosed to the user, and governed as personal-data processing under the approved GDPR data contract.
- A user may unlink GitHub from a successfully merged hosted identity only after completing a fresh passwordless magic-link authentication for the verified email already attached to that same stable identity.
- An existing hosted session, a GitHub authentication, or passwordless proof for a different identity must not authorize GitHub unlinking.
- Before unlinking, the product must explain that GitHub sign-in will stop working and GitHub-dependent repository connections may become disconnected, then require explicit user confirmation.
- A successful unlink must remove the GitHub external sign-in method, revoke or delete every accepted GitHub credential held by SDD Orchestrator, and end any application session whose continued authorization depends only on GitHub. The freshly authenticated passwordless session remains authorized.
- Unlinking GitHub must not split the stable hosted identity, recreate the absorbed workspace, change the surviving passwordless workspace, delete or reassign a project, change project storage mode, or modify repository content.
- A repository connection that depends on the removed GitHub authorization must remain attached to its project, become disconnected, and require fresh GitHub authorization before access can be restored.
- Failed, expired, mismatched, or cancelled passwordless proof or confirmation must leave the GitHub identity, credentials, sessions, workspace, projects, and repository connections unchanged.
- The unlink attempt and result must be disclosed to the user and audited under the approved GDPR data contract without retaining magic-link secrets or unnecessary GitHub identity data.
- A successful user-initiated unlink must disable automatic GitHub linking for that stable hosted identity. A later GitHub sign-in must not override this state even when its verified primary email matches under the normal automatic-matching rules.
- Re-linking after an explicit unlink requires successful GitHub authentication, fresh passwordless magic-link authentication for the stable hosted identity, and explicit confirmation that GitHub will be attached again.
- When GitHub returns a verified primary email during explicit re-linking, it does not need to match the passwordless email. The automatic-matching normalization, ASCII eligibility, alias, and equality rules do not authorize or block this user-confirmed two-proof flow.
- The confirmation must identify the authenticated GitHub account and the stable passwordless account being joined so the user can reject an unintended pairing before mutation.
- An existing passwordless session, an earlier unlink proof, or GitHub authentication alone must not authorize re-linking.
- Before re-linking mutates either identity, the product must rerun the complete project-name and repository-conflict preflight and use the same user-confirmed conflict recovery and atomic-commit rules as an initial merge.
- A cancelled, failed, expired, or mismatched re-link proof, an unconfirmed re-link, or an unresolved preflight conflict must leave both identities, credentials, workspaces, projects, and repository connections unchanged and must not disclose another account.
- After a successful re-link, repository connections previously disconnected by unlinking remain disconnected until the new GitHub authorization is validated for each repository; re-linking must not modify repository content.
- Enforcing the user's unlink choice requires a minimal privacy-governed automatic-link suppression state. Its purpose, lawful basis, minimum fields, access boundary, retention, deletion, rights behavior, and required privacy or legal review must be approved before implementation.
- An accountless on-device boundary has no verified email identity and must not be automatically merged or uploaded merely because the user later signs in with GitHub.
- Authentication must not attach, upload, synchronize, duplicate, or change the storage mode of an accountless on-device project.
- After authentication, the project catalog may combine on-device projects available to the current device user with hosted projects authorized for the signed-in identity.
- Every project shown in the combined catalog must identify whether its SDD data is on-device or hosted and whether the current device can access it.
- Signing out must remove access to hosted projects while leaving on-device projects available through the accountless device path.
- On-device project access relies on the current operating-system user profile and filesystem permissions. SDD Orchestrator does not provide another local-user isolation layer for people who share that boundary.
- Hosted storage is the storage mode that can support live collaboration with authorized colleagues.
- Repository location, SDD project-data location, and AI-agent execution location are independent choices.
- Every project belongs to one workspace with one storage mode.
- A user may change an existing project's storage mode directly without exporting and importing it.
- A storage-mode change must not modify the linked repository or change the project's stable identity.
- A failed storage-mode change must leave the previously active copy and storage mode usable; it must not leave the project partially moved.
- When a hosted project changes to on-device storage, the on-device copy becomes active and the hosted project plus its related hosted data are marked as deleted.
- A hosted copy marked as deleted through a storage-mode change is retained for two years from that change and then permanently cleaned up.
- At permanent cleanup, every project-scoped hosted record and derived copy must be deleted, including specifications, tasks, agent runs, artifacts, comments, memberships, collaboration records, repository metadata, synchronization baselines, operational logs, caches, search indexes, backups, and exports.
- The only cleanup exceptions are genuinely anonymous aggregate analytics and the minimum records that applicable law explicitly requires SDD Orchestrator to retain.
- A legally required retained record must have a documented legal basis, narrowly defined purpose, minimum necessary fields, restricted access, and its own deletion deadline. It must not retain project content or identifiers beyond what that obligation requires.
- Analytics are excluded from the two-year hosted project-data cleanup.
- Analytics must always be aggregate and genuinely anonymous. They must contain no personal data, project or repository content, names, stable user or device identifiers, repository identifiers, project identifiers, IP addresses, or other values that allow singling out, linkability, or inference about a person.
- Pseudonymised or encrypted personal data is not anonymous analytics and remains subject to the full personal-data lifecycle.
- Personal data must be processed lawfully, fairly, and transparently for explicit purposes and limited to what is necessary for those purposes.
- Database schemas and backend logic must apply data protection by design and by default, including purpose limitation, data minimization, accuracy, storage limitation, least-privilege access, confidentiality, integrity, availability, and auditable deletion.
- Every stored personal-data category must have an approved purpose, lawful basis, access boundary, retention period, deletion behavior, and applicable data-subject-rights behavior before implementation.
- Personal data must not be repurposed for analytics or product improvement unless an approved GDPR basis and transparent user-facing behavior are recorded first.
- The product must support applicable data-subject rights, including access, correction, erasure, restriction, objection, and portability, through identity-verified workflows defined before production.
- Backups, logs, caches, search indexes, exports, soft-deleted records, and third-party processors must follow the same approved privacy and retention rules as primary records.
- Appropriate technical and organizational security measures must protect personal data according to processing risk, and high-risk processing must not ship without the required impact assessment and review.
- While the deleted hosted copy remains retained, its latest version is the baseline for a future resynchronization.
- A soft-deleted hosted copy must be hidden from normal project lists, search, collaboration views, and ordinary project APIs throughout the retention period.
- A soft-deleted hosted copy cannot be opened, browsed, edited, or manually restored as a hosted project. It may be accessed only by the authorized resynchronization process after the user explicitly starts resynchronization from the active on-device project.
- When the user resynchronizes before that baseline is cleaned up, SDD Orchestrator must reactivate hosted storage and synchronize changes made since the latest retained hosted version rather than uploading unchanged project data again.
- When the user returns a project to hosted storage after its retained hosted baseline has been permanently cleaned up, SDD Orchestrator must perform a full upload while preserving the project's stable identity and repository connection.
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
- Project exports must not contain authentication credentials, repository credentials, session secrets, worker pairing credentials, or other accepted secrets.
- Importing a project must not silently overwrite an existing project, weaken repository uniqueness, or modify a linked repository.

## Acceptance Criteria

- Given a user opens the entry page, when it finishes loading, then it shows `Login with GitHub` and `Work without GitHub` as two distinct primary actions.
- Given a user does not want to authenticate with GitHub, when they select `Work without GitHub`, then they continue toward linking a repository on their computer without being asked for GitHub authentication.
- Given a user selects `Work without GitHub`, when storage is requested, then they can choose between keeping SDD project data on the current device and storing it with SDD Orchestrator.
- Given a user already has an on-device project, when they create another project, then they can choose hosted storage for the new project without changing the existing project's storage mode.
- Given a user selects a GitHub repository, when they choose project-data storage, then both on-device and hosted modes are available.
- Given a user selects a local repository, when they choose project-data storage, then both on-device and hosted modes are available.
- Given a user chooses on-device storage, when their workspace is established, then no account is required and its SDD project data remains on that device.
- Given a user chooses hosted storage, when their workspace is established, then an authorized identity protects data that persists independently from the current device.
- Given a user entered through `Work without GitHub` and chooses hosted storage, when they submit an email address, then the product sends a passwordless magic link and does not create or expose hosted project data before verification.
- Given a user receives a valid unused magic link for the current attempt, when they open it before expiry, then the email is verified and an authorized hosted session is established without a password.
- Given a magic link is invalid, expired, already used, or belongs to another attempt, when it is opened, then no session is established, no hosted data is exposed, and the user receives an actionable recovery path.
- Given any email is submitted for a magic link, when the request is acknowledged, then the response does not reveal whether that email already has an account.
- Given an existing passwordless account and GitHub returns one primary verified email that matches its verified email under the approved normalization rules, when authentication completes, then GitHub is automatically attached to the existing stable user identity and the user enters the same hosted account and projects.
- Given a verified secondary GitHub email matches the verified passwordless email but the verified primary GitHub email does not, when authentication completes, then the product does not automatically merge the identities.
- Given GitHub returns no primary email, an unverified primary email, multiple primary emails, or a primary email that does not match, when authentication completes, then the product does not automatically merge the identities.
- Given GitHub email data is processed for authentication, when the attempt ends, then no secondary GitHub email remains in application records, analytics, logs, or audit payloads.
- Given either verified address contains a non-ASCII character in its local part or domain, when automatic matching is considered, then no Unicode transformation or automatic merge occurs and each otherwise successful sign-in continues through its separate hosted identity.
- Given either verified address contains a domain label beginning with `xn--` in any letter case, when automatic matching is considered, then no IDNA conversion or automatic merge occurs and the response does not disclose whether another identity exists.
- Given `  User.Name@Example.COM  ` is normalized for matching, when no local-part provider rule applies, then the comparison form is `User.Name@example.com`.
- Given `User.Name@example.com` and `user.name@example.com` use a domain without an approved local-part case rule, when automatic matching is attempted, then letter-case differences in the local part are preserved and do not create a match.
- Given a domain has an approved local-part case-insensitivity rule, when two verified addresses differ only by local-part letter case, then the approved case folding may produce the same comparison form.
- Given an address contains whitespace inside its local part or domain, when normalization is attempted, then the address is rejected rather than having internal whitespace removed.
- Given `first.last+work@approved.example` and `firstlast@approved.example` are verified addresses on a domain approved for both alias rules, when their matching forms are produced, then the period and `+work` suffix are removed from the local part and the addresses can match.
- Given the same local-part variations use a domain without an approved alias rule, when automatic matching is attempted, then neither periods nor the `+tag` suffix are removed and no alias-based merge occurs.
- Given a domain is approved for `+tag` stripping but not dot removal, when an address is normalized, then its approved tag is stripped while periods remain unchanged.
- Given a custom domain is hosted by a provider whose personal-email domain has approved alias rules, when automatic matching is attempted, then the personal-domain rules are not inherited by the custom domain.
- Given alias normalization maps a sign-in address to more than one hosted identity, when automatic matching is attempted, then no merge occurs and the response does not disclose the conflicting accounts.
- Given an automatic merge is requested more than once or concurrently, when it completes, then only one stable user identity remains and no hosted project, membership, or repository link is duplicated or overwritten.
- Given both matching identities contain hosted projects and the combined set has no case-insensitive project-name or repository conflict, when automatic merge completes, then every project from both identities is available under the resulting stable account with its identity, name, repository connection, and related hosted data unchanged.
- Given both matching identities contain hosted projects with a case-insensitive project-name conflict or repository uniqueness conflict, when automatic merge is attempted, then the merge makes no identity, workspace, project, or repository-link changes, deletes or overwrites nothing, and gives the user a safe recovery path.
- Given a merge would add a project named `example` to a workspace that already contains `example` and `example-1`, when the name conflict is presented, then the product suggests `example-2` without changing either project.
- Given the user confirms a suggested conflict name, when the merge is retried, then the product reruns the complete preflight and applies the confirmed rename only if the whole merge commits atomically.
- Given the user does not confirm a suggested conflict name, when they leave or cancel recovery, then both identities and all their projects remain unchanged.
- Given two projects from matching identities are linked to the same canonical repository, when repository-conflict recovery starts, then the product shows both projects and requires the user to choose which one keeps that repository without changing either project yet.
- Given the user chooses a keeper project and selects a different valid unlinked repository for the other project, when the merge is retried and the complete preflight passes, then both projects and all their data are preserved, the chosen project keeps the original repository, and the other receives the confirmed replacement connection as part of the atomic merge.
- Given the user cancels repository-conflict recovery or the replacement repository is inaccessible, invalid, or already linked in the resulting workspace, when recovery ends, then the merge remains stopped and neither identity, project, nor repository connection changes.
- Given a verified GitHub identity matches an existing passwordless identity and each has a personal workspace, when the automatic merge succeeds, then the passwordless personal workspace keeps its stable identity and every GitHub-backed hosted project moves into it with its stable project identity and related data preserved.
- Given an automatic merge succeeds, when the resulting account is restored, then exactly one active personal workspace is available and the absorbed GitHub-backed personal workspace cannot be opened separately.
- Given an automatic merge fails, is cancelled, or remains blocked, when either pre-merge identity is used, then its original personal workspace and projects remain unchanged.
- Given the absorbed GitHub-backed workspace has a paired local worker, when the automatic merge succeeds, then the old pairing credential is revoked, the worker remains installed with its local files unchanged, and it reports that pairing is required.
- Given the user explicitly re-pairs that installed worker with the surviving passwordless workspace, when pairing succeeds, then new workspace-bound credentials are issued and affected local repository connections can be revalidated without modifying repository content.
- Given an automatic merge fails, is cancelled, or remains blocked, when the existing local worker reconnects, then its original workspace pairing remains valid and unchanged.
- Given an automatic merge succeeds, when absorbed-workspace storage is inspected after commit, then only the source workspace ID, surviving workspace ID, merge event ID, merge status, completion time, and approved deletion deadline remain in the inaccessible merge record.
- Given the retained merge record is inspected, when its fields and access paths are reviewed, then it contains no project, repository, email, credential, worker-token, session, conflict, membership, or analytics-linkage data and is absent from normal workspace and project interfaces.
- Given the merge record reaches its approved deletion deadline without a separately approved legal-retention requirement, when retention enforcement runs, then the record is permanently deleted.
- Given the merge record lacks an approved purpose, lawful basis, access boundary, retention period, deletion behavior, rights handling, or required privacy or legal review, when implementation approval is evaluated, then absorbed-workspace cleanup remains blocked.
- Given a merged user completes fresh passwordless magic-link authentication for the verified email attached to the stable hosted identity and confirms the warning, when GitHub unlinking succeeds, then GitHub sign-in and accepted GitHub credentials are removed while the passwordless identity, surviving workspace, projects, and project data remain unchanged.
- Given GitHub unlinking succeeds and a repository connection depended on the removed authorization, when the project catalog is shown, then the project remains visible, its repository connection is disconnected, and restoring access requires fresh GitHub authorization.
- Given a user has only an existing session, authenticates through GitHub, proves a different passwordless identity, or provides invalid, expired, mismatched, or cancelled passwordless proof, when GitHub unlinking is attempted, then no identity, credential, session, workspace, project, or repository-connection state changes.
- Given GitHub unlinking succeeds, when the prior absorbed workspace is inspected, then it remains inaccessible and is not recreated or split from the surviving passwordless workspace.
- Given a user previously unlinked GitHub and later signs in with a GitHub identity whose verified primary email matches the passwordless identity, when GitHub authentication completes, then the product does not automatically attach or merge that identity.
- Given a previously unlinked user successfully authenticates with GitHub, freshly verifies the stable identity through its passwordless magic link, explicitly confirms the identified accounts, and has no unresolved project conflict, when the complete preflight passes, then GitHub is attached again through one atomic operation without changing the stable passwordless identity or losing project data, even when GitHub's verified primary email differs from the passwordless email.
- Given the two verified emails differ in case, alias form, domain, or character set, when the user explicitly re-links after freshly proving both sign-in methods, then the automatic email-normalization and ASCII-matching rules do not reject or authorize the re-link.
- Given a re-link attempt is cancelled, unconfirmed, uses stale or invalid passwordless proof, or has an unresolved project-name or repository conflict, when the attempt ends, then no identity, credential, workspace, project, or repository-connection state changes and no other account is disclosed.
- Given GitHub is successfully re-linked, when previously disconnected repository connections are shown, then each remains disconnected until the new GitHub authorization is validated for that repository.
- Given onboarding or its identity-merge flow runs in this feature, when its persisted changes are inspected, then no collaboration membership, invitation, role, or permission record has been created, reconciled, changed, or deleted.
- Given an accountless user has on-device projects, when they later authenticate with GitHub or passwordless email, then those projects appear alongside their authorized hosted projects and remain on-device without upload, synchronization, duplication, or identity mutation.
- Given an authenticated user views a combined project catalog, when projects use different storage modes, then each project clearly shows its on-device or hosted data location and current availability.
- Given an authenticated user signs out, when the project catalog is revisited through `Work without GitHub`, then on-device projects remain available while hosted projects are no longer accessible without authentication.
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
- Given an existing project, when the user exports it, then the product produces a portable project package without accepted credentials or secrets.
- Given a compatible project package and an available storage mode, when the user imports it, then the project is restored without silently overwriting another project or modifying a repository.
- Given a hosted project, when the user changes its storage mode to on-device and the transfer succeeds, then the on-device copy becomes active and the hosted project with its related hosted data is marked as deleted without changing the linked repository or stable project identity.
- Given a hosted-to-device storage change, when less than two years have passed, then the deleted hosted project data remains retained as an unavailable synchronization baseline while analytics remain retained separately.
- Given a hosted copy is soft-deleted and retained, when the user browses projects, searches, uses collaboration views, or calls ordinary project APIs, then that hosted copy is not returned or accessible.
- Given a soft-deleted hosted baseline exists, when no authorized user has explicitly started resynchronization from its active on-device project, then no normal user or collaborator can read, restore, or modify the retained copy.
- Given a hosted-to-device storage change, when the two-year retention period ends without resynchronization, then the deleted hosted project and its related hosted data are permanently cleaned up except for retained analytics.
- Given the two-year cleanup runs, when project-scoped data is inspected afterward, then no specifications, tasks, agent runs, artifacts, comments, memberships, collaboration records, repository metadata, synchronization baselines, operational logs, caches, search indexes, backups, or exports remain.
- Given a record is retained after cleanup for a legal obligation, when its data contract is reviewed, then it contains only the minimum required fields and has a documented legal basis, purpose, restricted access boundary, and separate deletion deadline.
- Given analytics are retained after project-data cleanup, when the analytics dataset is evaluated alone or with other reasonably available data, then it cannot single out a person, link records to the same person, or support inference about an identifiable person, project, workspace, or repository.
- Given analytics data can be linked back to a person, device, project, workspace, or repository, when its classification is reviewed, then it is treated as personal data rather than retained anonymous analytics.
- Given a proposed database field or backend processing operation handles personal data, when it is reviewed for implementation, then its purpose, lawful basis, necessity, access, retention, deletion, rights handling, and processor or transfer boundary are documented and approved.
- Given a data-subject request applies to hosted personal data, when the request is authenticated and accepted, then all applicable primary records, derived records, logs, indexes, backups, exports, and processor copies follow the approved rights workflow and retention exceptions.
- Given a schema or backend change lacks an approved GDPR data contract or required privacy review, when implementation approval is evaluated, then the change remains blocked.
- Given an on-device project whose deleted hosted baseline is still retained, when the user resynchronizes it to hosted storage, then the hosted project is reactivated and only changes since the latest retained hosted version are synchronized.
- Given an on-device project whose hosted baseline has been permanently cleaned up, when the user returns it to hosted storage, then the full current project data is uploaded as a new hosted copy under the same stable project identity and repository connection.
- Given any storage-mode change fails before completion, when the failure is reported, then the previously active project copy remains usable and no repository content or accepted secret has been changed.
- Given any unsuccessful sign-in, pairing, validation, or link attempt, when the operation ends, then no duplicate user workspace, worker, repository connection, or project is created.

## Open Questions

- What magic-link lifetime, resend behavior, session lifetime, email-delivery provider, and account-recovery behavior should the hosted email path use?
- Which exact domains and account types have sufficient official provider evidence to enter the launch allowlist for dot removal, `+tag` stripping, or both?
- How are allowlist evidence, security review, version changes, and the effect of removing a previously approved rule governed?
- What lawful basis and shortest necessary retention period receive privacy or legal approval for the minimal absorbed-workspace merge record?
- How can a user challenge and recover from an incorrect automatic identity merge?
- Can explicit re-linking proceed when GitHub returns no verified primary email, provided the user still freshly proves the GitHub and passwordless sign-in methods?
- What minimum data may the automatic-link suppression state contain, and what lawful basis, retention, deletion, rights handling, and privacy review apply to it?
- Which anonymous aggregate metrics are necessary for the product, and what retention period applies to each metric?
- Which entity is the controller or processor for each hosted, local-worker, AI-agent, and third-party data flow?
- What purpose and lawful basis apply to each category of personal-data processing?
- How are data-subject requests authenticated and propagated through live data, soft-deleted data, backups, logs, exports, and subprocessors?
- Which personal-data retention periods and deletion exceptions apply to accounts, collaboration, operational logs, security logs, billing, support, and backups?
- Which subprocessors and international transfers are allowed, and what safeguards and user notices are required?
- Which processing activities require a data protection impact assessment or prior privacy review?
- How are changes, deletions, conflicts, and compatibility detected during incremental resynchronization?
- What project data and history belong in an export package, and does it ever include repository source files?
- How are imported project identity, name conflicts, repository reconnection, and duplicate detection handled?
