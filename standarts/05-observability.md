# Observability

All Rust services, Flutter clients, desktop agents and server agents emit
structured OpenTelemetry-compatible telemetry. The common fields are:

```text
timestamp
severity
service.name
service.version
deployment.environment
device.id
server.id
module
event.name
trace_id
span_id
error.type
```

The W3C trace context is propagated across client, server, agent and module
boundaries. User content, tokens, cookies, authorization headers, private
keys, full environment values and raw command secrets are redacted before an
event leaves the process.

## Pipeline

```text
Flutter/Rust clients and agents
              │ authenticated telemetry API
              ▼
     nddev-observability (Rust)
              │ normalize, redact, alert state
              ▼
           Vector
              │ buffer, batch, route
              ▼
         OpenObserve
```

Vector also collects journald, system service logs and container logs where a
local collector is required. OpenObserve access is never granted to Flutter or
desktop clients. Only the central pipeline receives the scoped ingestion
credential.

The Rust observability service owns operational alerts: device offline, sync
stalled, agent heartbeat expired, migration failed, telemetry delivery lagging,
or a release health check degraded. OpenObserve owns search, dashboards and
query-based analysis.

Every pipeline exposes its own health: queue depth, delivery age, dropped
events, exporter failures, storage pressure and alert notification status.

