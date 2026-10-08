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

Retries are bounded and use exponential backoff. Replaying the same operation
is safe and returns the original result. Conflicts create an explicit conflict
record containing both revisions and a resolution state; silent last-write-wins
is not used for credentials, devices, permissions or release policy.

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

