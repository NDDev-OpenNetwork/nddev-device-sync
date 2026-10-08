# Development workflow and consistency

## Change path

1. Update or confirm the owning contract.
2. Write the smallest domain rule or adapter change.
3. Add a focused test and telemetry for the new state or failure.
4. Run the module's `just` check and integration checks affected by the
   contract.
5. Update the standards lock or generated clients only through their source
   release.
6. Commit with a scoped message and a release note when behavior changes.

Public module repositories use protected `main`, signed commits, pull requests,
CODEOWNERS and pinned CI actions. The central repository's standards release is
the compatibility anchor. A module may consume an older standards release only
with an explicit compatibility note.

## Consistency rules

- Server is authoritative for synchronized control state.
- Mutations use idempotency keys and optimistic revisions.
- Read models may be eventually consistent but expose freshness and revision.
- Secrets are never resolved into a public DTO or event.
- Timeouts, retries, cancellation and resource limits are part of each port's
  contract.
- Feature flags are versioned, scoped and observable.
- Migrations are forward-reviewed and tested from an empty database.
- A release artifact records its source commit, standards release, protocol
  version, schema version and dependency lock hash.

## Deferred work

Backup/recovery, multi-tenant administration, team roles, advanced deployment
orchestration and runtime plugins remain disabled until an explicit standards
change and migration plan exist. Their future interfaces may be designed, but
alpha code must not implement hidden partial versions of them.

