# Observability ownership

The canonical event envelope, operating modes and quality signals are defined
once in [the telemetry standard](15-observability-and-telemetry-standard.md).

```text
Rust / Flutter / agents
          |
          v
nddev-observability -> Vector -> OpenObserve
```

Processes redact before emission. The Rust observability service normalizes
events and owns alert state; Vector bounds collection, buffering and routing;
OpenObserve provides search and analysis. Clients never receive its ingestion
credentials. Vector may also collect journald and container logs.

The pipeline reports its own delivery failures and freshness. A service is not
observability-ready because it emits JSON or sets an enabled flag. Acceptance
must demonstrate collection, correlation, searchable delivery, a triggered
alert and its resolution. Operational alerts include dependency failure,
stalled sync, expired heartbeat, telemetry loss and storage pressure.
