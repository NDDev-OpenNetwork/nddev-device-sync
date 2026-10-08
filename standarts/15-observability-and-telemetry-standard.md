# Observability and telemetry standard

Observability is part of the product contract. Every Rust process, Flutter
client, agent, server module, migration runner and release workflow emits
structured, correlated and redacted telemetry.

## Event envelope

Each log, metric or trace event includes the applicable fields:

```text
timestamp
severity
service.name
service.version
deployment.environment
release.channel
release.version
source.repository
source.commit
module
event.name
device.id
server.id
tenant.id
user.id (pseudonymous where possible)
trace_id
span_id
error.type
duration_ms
outcome
```

Build and test telemetry additionally records `build_id`, toolchain, target,
test suite, migration version and artifact digest. It never records source
secrets or full environment values.

## Pipeline

```text
Flutter/Rust process → local Rust SDK/bridge
                    → nddev-observability
                    → Vector
                    → OpenObserve
```

Vector also collects journald and container logs where a local collector is
needed. OpenObserve credentials exist only in the central telemetry pipeline.
Self-hosted operators may disable telemetry; disabled state, dropped events and
queue pressure remain visible locally.

## Required behavior

- Errors and state transitions are always logged.
- Normal high-volume events are sampled only after error and audit coverage is
  preserved.
- Every retry has a count, backoff, terminal outcome and trace correlation.
- Every service exposes liveness, readiness and dependency health.
- Every alert has deduplication, acknowledgement, silence and resolution
  state.
- Redaction happens before an event leaves the process.
- Tokens, cookies, private keys, Authorization headers, raw prompts, full
  command lines and secret-bearing URLs are prohibited telemetry values.
- Telemetry queues and buffers are bounded, observable and not backups.

## Quality signals

The alpha dashboards must show sync latency, operation conflict rate, outbox
age, agent heartbeat age, API error rate, database health, migration version,
telemetry delivery age, dropped event count and release health. A green
dashboard without fresh telemetry is a degraded state, not success.

