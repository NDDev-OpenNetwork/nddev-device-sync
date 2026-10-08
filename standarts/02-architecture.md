# System architecture

## Components

```text
Flutter desktop/mobile UI
          │ typed local bridge or API client
          ▼
Rust client core and device agent
          │ HTTPS/WebSocket + device identity
          ▼
Rust sync/control server
   ┌──────┼───────────┬─────────────┐
   ▼      ▼           ▼             ▼
Postgres vault    observability  module adapters
                  service
                      │
                 Vector → OpenObserve
```

The common business model is Rust. Flutter owns presentation and platform UI;
it does not own sync rules, credentials, process execution or package policy.
The same Flutter feature modules target macOS, Ubuntu/Linux, Windows, iOS and
Android. The desktop agent provides background operation, tray integration,
autostart and system services; the mobile app uses the same Rust core through a
native bridge and respects mobile lifecycle limits.

## Repository shape

```text
apps/
  desktop-mobile-client/
  sync-server/
  server-agent/
  observability-service/
  admin-cli/

crates/
  domain/
  application/
  protocol/
  sync-engine/
  device-identity/
  credential-vault/
  storage-sqlite/
  storage-postgres/
  observability/
  adapters/
  platform/

contracts/
  openapi/
  events/
  json-schema/

infra/
  compose/
  postgres/
  vector/
  openobserve/

standarts/
```

The domain layer has no OS, UI, network or database dependencies. Application
use cases depend on ports. Platform, storage, process, keyring, network and
existing-tool implementations are adapters. Flutter calls a small typed
bridge; it never receives unrestricted shell or filesystem permissions.

Modules are compiled-in and manifest-driven for the alpha channel. A runtime
native plugin ABI requires signing, version negotiation, crash isolation and
rollback; it is not introduced before those contracts exist.

## Canonical contracts

OpenAPI 3.1 describes request/response APIs. JSON Schema describes event
payloads and WebSocket messages. Generated Rust and Dart clients are committed
or reproducibly generated in CI. Hand-maintained duplicate DTOs are forbidden.

