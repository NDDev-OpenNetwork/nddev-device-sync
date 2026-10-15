# Synchronization and data ownership

## Stores

- Native client metadata and offline queues use per-user SQLite. Browser
  durability must satisfy [ADR 0007](decisions/0007-offline-browser-client.md)
  through its qualified browser storage adapter and the same transaction rules.
- The server's authoritative control state uses PostgreSQL 18.
- Logs, metrics and traces use OpenObserve.
- Secret bytes use the encrypted vault and native keyrings.
- Project source remains in Git and is not copied into the sync database.

The server is the authority for committed state. Devices are replicas: startup,
enrollment, reconnect and resume initiate reconciliation without depending on
another device. Bounded background catch-up continues from its durable cursor
until there is no remaining history. Expose whether the replica is catching up,
its pending/conflicted mutations and its last fully caught-up observation;
receiving one partial page does not establish freshness.

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

[ADR 0009](decisions/0009-first-alpha-product-contract.md) defines the first-alpha
target for continuous native execution, seven-day offline authorization, complete
supported module-data collection and bidirectional GDS commit synchronization.
These are acceptance requirements, not claims that the current runtime has
already implemented them.

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
