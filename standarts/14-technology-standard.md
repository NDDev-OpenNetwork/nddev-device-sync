# Technology standard

The alpha technology baseline is intentionally small and pinned by each
repository's lockfile:

| Concern | Standard |
| --- | --- |
| Core language | Rust 1.99 stable, edition 2024 |
| UI | Flutter 3.47+ and Dart stable |
| Desktop background | Rust device agent; Flutter connects through a typed local bridge |
| Mobile bridge | Rust core through a generated native bridge |
| Server | Rust async service with Tokio and Axum |
| API contract | OpenAPI 3.1 for HTTP; JSON Schema draft 2020-12 for events |
| Local state | SQLite with migrations, WAL and bounded outbox/inbox |
| Server state | PostgreSQL 18.x through SQLx with checked migrations |
| Secrets | Native keyring plus end-to-end encrypted vault records |
| Identity | GitHub OAuth with PKCE; per-device signing keys |
| Transport | HTTPS/WebSocket with rustls and W3C trace context |
| Observability | `tracing`, OpenTelemetry, Vector and OpenObserve |
| Infrastructure | Docker Compose only for alpha; `just` as command runner |
| Rust checks | rustfmt, clippy, nextest, cargo-deny, cargo-audit, coverage |
| Flutter checks | dart format, dart analyze, Flutter unit/widget/integration tests |
| Design | `nddev-opennetwork-design-system`, pinned alpha release |

React, Tauri, Kubernetes, service meshes, runtime native plugins and additional
message brokers are outside the alpha baseline. They may be proposed through an
ADR when a measured requirement justifies the added surface.

Dependencies are added only with a purpose, owner, license decision, update
path and removal condition. A package must not be added merely to wrap one
standard-library operation.

