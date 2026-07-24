# GitHub Identity Linking Design

## Context

GitHub and passwordless hosted access can create separate stable identities and personal workspaces for the same person. Email-based automatic candidate detection is security-sensitive because provider email semantics, aliases, reassignment, normalization, project conflicts, worker credentials, and retained merge evidence can cause account takeover or data loss if a match can mutate accounts without proof and consent.

This design uses conservative automatic candidate detection followed by fresh proof of both sign-in methods and explicit confirmation for initial linking. Re-linking after user unlink remains a separate explicit two-proof path.

## Proposed Approach

1. Retrieve one unambiguous verified primary GitHub email with minimum permission and discard secondary addresses after transient provider processing.
2. Apply first-release ASCII eligibility, base normalization, and exact-provider rules.
3. Resolve at most one passwordless identity candidate without account disclosure.
4. Require fresh passwordless proof for the candidate while retaining the fresh GitHub authentication that started the attempt.
5. Preflight the complete resulting project set and all workspace ownership changes without mutation.
6. Collect explicit conflict choices and rerun the full preflight.
7. Identify both accounts and the merge consequences and require explicit confirmation.
8. Commit identity attachment, project moves, worker revocation, merge record creation, and audit atomically.
9. Support fresh-passwordless-proof unlinking and persist a minimal policy that suppresses future automatic re-link.
10. Support explicit re-link by proving both sign-in methods, confirming the accounts, rerunning preflight, and revalidating repositories.

## Components Affected

- GitHub and passwordless identity services.
- Email normalization and provider-rule registry.
- Identity match, preflight, merge, unlink, and re-link orchestration.
- Personal workspace and project ownership persistence.
- Project naming and repository conflict recovery.
- Worker pairing revocation and re-pairing.
- Repository connection authorization and status.
- Merge evidence, unlink policy, audit, notification, privacy, and rights workflows.

## Data and Access Boundaries

- `ExternalIdentity`: one GitHub or verified passwordless sign-in method attached to a stable hosted identity.
- `IdentityMergeAttempt`: transient matching, preflight, conflict, and confirmed-choice state.
- `IdentityLinkPolicy`: minimal personal-data state suppressing automatic GitHub linking after explicit unlink.
- `WorkspaceMergeRecord`: the field-limited inaccessible post-commit evidence record.
- `PersonalWorkspace`: the stable ownership boundary; the existing passwordless workspace survives.

Required boundaries:

- Secondary GitHub emails are transient, non-matchable, and non-retainable.
- Automatic match eligibility and canonicalization run before any identity or workspace mutation.
- Provider transformations are exact-domain and account-type scoped and version governed.
- Automatic matching yields zero or one candidate; ambiguity fails closed.
- Candidate state is transient and non-mutating and cannot expose the matched account before fresh passwordless proof succeeds.
- Initial linking requires fresh proof of both sign-in methods, successful preflight, and explicit confirmation.
- Preflight covers all projects, names, repositories, ownership moves, and confirmed recovery choices.
- The merge commits as one transaction or leaves both original identity boundaries unchanged.
- Worker credentials are revoked after commit, never transferred.
- The merge record and unlink policy are personal data with separate minimized schemas and approved lifecycles.
- A linked GitHub identity may authenticate the surviving hosted identity after passwordless email loss, but it cannot replace proof of the current verified email.
- Explicit unlink and re-link require independent passwordless proof; GitHub-only sessions cannot authorize them.
- Accountless device projects remain outside hosted identity mutation.

## Interfaces

- GitHub email interface: return one verified primary address and treat all other addresses as transient.
- Automatic-candidate interface: enforce ASCII eligibility, approved canonicalization, collision checks, transient candidate state, and account-neutral failure.
- Initial-link proof and confirmation interface: require fresh passwordless proof alongside the initiating GitHub authentication, identify both accounts only after proof, present merge consequences after preflight, and record explicit confirmation.
- Provider-rule interface: version independently approved case, dot, and tag transformations by exact domain and account type.
- Merge-preflight interface: evaluate complete name and repository uniqueness and produce non-mutating recovery choices.
- Merge-commit interface: attach GitHub as a sign-in method, move every hosted project, revoke source pairings, create the minimal merge record, and audit atomically.
- Conflict-recovery interface: confirm provisional name and repository choices and trigger a fresh full preflight.
- Unlink interface: require fresh passwordless proof, warn, confirm, revoke GitHub access, disconnect repositories, and persist suppression atomically.
- Re-link interface: detect suppression before matching, prove both identities, identify and confirm them, preflight, commit, and revalidate repositories.
- Privacy interface: enforce the separate merge-record and link-policy data contracts, rights behavior, and deletion deadlines.

## Decisions and Tradeoffs

### Verified Primary GitHub Email Only

- Choice: Use only one GitHub email marked both primary and verified for automatic matching.
- Reason: A narrow authoritative candidate reduces unintended consolidation and secondary-address retention.
- Consequence: Missing, unverified, non-matching, or ambiguous primary results remain separate. GitHub documents the attributes and required permission in its [email API](https://docs.github.com/en/rest/users/emails).

### Conservative Provider-Aware Normalization

- Choice: Trim surrounding whitespace, lowercase domains, preserve local-part case by default, and enable case folding, dot removal, and `+tag` stripping only through independently approved exact-provider rules.
- Reason: SMTP assigns local-part semantics to the receiving host, so transformations are not globally safe, as described by [RFC 5321](https://www.rfc-editor.org/rfc/rfc5321.html).
- Consequence: Unknown and custom domains fail closed for alias matching. Google, for example, documents different period behavior for personal and organizational domains in [Gmail Help](https://support.google.com/mail/answer/7436150?hl=en).

### ASCII-Only Automatic Matching At Launch

- Choice: Exclude non-ASCII addresses and domain labels beginning with `xn--` from automatic matching.
- Reason: Unicode equivalence, IDNA conversion, and confusables require a dedicated security model. [RFC 5890](https://www.rfc-editor.org/rfc/rfc5890.html) defines the `xn--` ASCII-compatible form.
- Consequence: Supported sign-ins remain separate; future internationalized matching needs a new specification update and collision proof.

### Automatic Detection, Explicit Linking

- Choice: Use automatic matching only to identify a transient candidate. Require fresh proof of both sign-in methods, a complete preflight, and explicit confirmation before initial linking commits.
- Reason: An email match alone is not sufficient authority for an irreversible account and project merge.
- Consequence: Failed proof, cancellation, or missing confirmation leaves both accounts unchanged. The minimal post-merge record remains viable because the product no longer performs an unconfirmed automatic merge.

### Passwordless Workspace Survives

- Choice: Preserve the passwordless identity and workspace and move every GitHub-backed hosted project only inside a successful atomic merge.
- Reason: The passwordless workspace is the existing hosted recovery anchor.
- Consequence: Project conflicts require recovery before commit; the GitHub workspace becomes inaccessible and only minimized evidence remains.

### User-Confirmed Conflict Recovery

- Choice: Suggest deterministic name suffixes and require an authorized replacement repository while keeping all choices provisional until fresh preflight.
- Reason: This preserves all projects without silently renaming or overwriting them.
- Consequence: Cancellation or any newly detected conflict leaves both identities unchanged.

### Revoke Rather Than Transfer Worker Pairings

- Choice: Revoke absorbed-workspace pairings after commit and require explicit re-pairing.
- Reason: Pairing grants machine access within one workspace trust boundary.
- Consequence: Workers stay installed and local files remain unchanged, but affected connections require authorization again.

### Minimal Post-Merge Evidence

- Choice: Retain only source and survivor IDs, merge event ID, status, completion time, and approved deletion deadline.
- Reason: Idempotency and approved security or support may need evidence, but a soft-deleted workspace would retain excessive personal data.
- Consequence: Lawful basis, purpose, access, rights, shortest retention, and deletion need privacy or legal approval before implementation.

### Fresh Proof For Unlink And Re-Link

- Choice: Require fresh passwordless proof to unlink and fresh proof of both sign-in methods plus confirmation to re-link.
- Reason: A GitHub-only session must not remove or restore its own trust relationship unilaterally.
- Consequence: Explicit re-link may join different verified emails because control of both identities replaces email equality, while automatic linking rules stay unchanged. A linked GitHub method may preserve account access after passwordless email loss, but it cannot authorize verified-email change, unlinking, or re-linking by itself.

## Risks

- Incorrect normalization can identify the wrong candidate. Fail closed, expose no candidate account data before proof, and require both proofs plus confirmation before mutation.
- Concurrent merges can duplicate or lose data. Use idempotency, complete preflight, persistence constraints, and atomic commit.
- Conflict recovery can mutate state before consent. Keep choices transient until confirmed and revalidated.
- Worker credential transfer can grant machine access unexpectedly. Revoke after commit and require re-pairing.
- Merge evidence or unlink policy can become an indefinite identity map. Minimize fields, restrict access, prohibit analytics linkage, and enforce approved deletion.
- Unlink can lock out the user or leave provider credentials active. Require independent proof, warning, atomic credential removal, and session termination.
- Linked-provider recovery can be mistaken for authority to replace the verified email. Keep account access separate from email-change and link-management proof.
- Automatic re-link can defeat explicit consent. Check the unlink policy before email matching and preserve it after failed attempts.
- Collaboration data could widen or remove access during merge. Keep it out of scope until a membership-aware specification exists.

## Open Questions

- Technical design: Which provider domains and account types enter the launch normalization registry?
- Technical design: How are registry review, versioning, deployment, rollback, and rule removal governed?
- Active-slice implementation: Which lawful basis and retention are approved for the merge record and unlink policy?
- Product requirements: Which user and support recovery process applies when a user challenges a merge they explicitly confirmed?
- Product requirements: Is a verified primary GitHub email required for explicit re-link after both methods are proven?
- Technical design: Which candidate expiry, proof binding, transaction, locking, idempotency, notification, audit, and credential-revocation mechanisms implement the contracts?
- Required verification: Which privacy, security, integration, concurrency, and browser proof forms the verification gate?
