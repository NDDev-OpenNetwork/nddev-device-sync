# Synchronization and data ownership

## Stores

- Client metadata and offline queues use per-user SQLite.
- The server's authoritative control state uses PostgreSQL 18.
- Logs, metrics and traces use OpenObserve.
- Secret bytes use the encrypted vault and native keyrings.
- Project source remains in Git and is not copied into the sync database.

## Operation protocol

Every mutation has an `operation_id`, `device_id`, `entity_id`, base revision,
payload schema version and idempotency key. The server assigns a monotonic
`server_seq`. Clients persist an outbox before acknowledging a local mutation,
then advance an inbox cursor only after applying a verified server operation.

The idempotency scope, request fingerprint and retention are explicit. Reusing a
key with a different request is rejected. Entity state, revision, operation and
original result commit atomically. Concurrent duplicates return that result.
Sequence/cursor semantics must not skip an operation that commits later; a
database sequence allocation alone does not guarantee commit order. Expired
history requires an explicit fresh-state synchronization path, never silent loss.

Retries are bounded and use exponential backoff. Replaying the same operation
is safe and returns the original result. Conflicts create an explicit conflict
record containing both revisions and a resolution state; silent last-write-wins
is not used for credentials, devices, permissions or release policy.

Tenant/user ownership comes from authenticated server context and is checked
for every entity and cursor. Offline clients expose pending/conflicted state
and freshness; they cannot claim immediate global consistency while disconnected.

## Data classes

1. Device and module state.
2. Connection registry: endpoints, ports, labels, capabilities and health
   policy.
3. Harness account metadata and encrypted credential references.
4. Server inventory and health snapshots.
5. Audit records and alert incidents.

Each class has a schema version, owner, retention policy and redaction rules.
PostgreSQL migrations are forward-reviewed and exercised from an empty
database in CI.
