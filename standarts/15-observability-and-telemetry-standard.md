# Observability and telemetry standard

Every Rust process, Flutter client, agent, migration runner and release workflow
emits structured, correlated and redacted events. Observability is part of each
implemented behavior, not a later substitute for error handling.

## Canonical envelope

Use applicable fields with stable names and bounded cardinality:

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

Common process/build metadata is attached centrally, including startup,
shutdown, migration, TLS reload and process failure, not only HTTP spans.
W3C trace context crosses service/module boundaries. Build/test evidence adds
build ID, toolchain, target, suite, schema/migration version and artifact digest.
Metric labels never use unbounded IDs, user content or raw URLs.

## Modes

- **Normal** is the default: lifecycle, security/audit, relevant state changes,
  warnings and errors; operational metrics, correlated traces and alerts remain
  available. Routine high-volume success events may be sampled.
- **Debug** is explicitly enabled for a bounded scope and duration. It adds
  diagnostic spans and structured detail with finite volume/retention. Expiry
  returns to normal; enable/disable transitions are auditable.
- Both modes use the same schema and redaction boundary. Debug never exposes
  OTPs, passwords, tokens, cookies, private keys, authorization headers, raw
  prompts, full command lines, environment values or secret-bearing URLs.
  Do not dump request/response bodies as a general debug mechanism.
- A self-hosted operator may disable telemetry export. Required local failure,
  security and health signals remain available. Report configured mode, actual
  exporter availability and delivery freshness separately; an enabled flag is
  not evidence of a functioning pipeline.

## Delivery and alerts

```text
Flutter/Rust process -> nddev-observability -> Vector -> OpenObserve
```

Redaction happens before events leave a process. Reuse one owned event/redaction
contract; collectors may apply additional checks. Only the central pipeline
holds OpenObserve credentials. Vector may collect journald/container logs.

Queues, batches, retry count/backoff, storage retention and disk use are bounded.
Failures are visible locally. Errors/audit events are not intentionally sampled;
resource exhaustion or exporter failure must surface lost-event counts and
degraded state rather than silently claim complete delivery.

Every service has liveness, readiness and dependency health. An alert has an
owner, severity, deduplication, acknowledgement, silence and resolution state,
with a finite incident lifecycle. Verify notification delivery when a channel
is configured; a created incident is not evidence of a delivered notification.
Debug mode and disabled export must not mask operational failure.

## Acceptance signals

For implemented flows observe latency/errors, sync conflict rate and outbox age,
device/agent heartbeat age, database and migration health, resource pressure,
telemetry delivery age/drops and release health. A dashboard with stale or
missing telemetry is degraded. Acceptance follows an actual correlated event
into OpenObserve and exercises an alert through resolution; mock events do not
prove the application path.
