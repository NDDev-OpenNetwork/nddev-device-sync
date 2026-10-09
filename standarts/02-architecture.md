# System architecture

Flutter desktop/mobile presentation calls a typed bridge into the Rust core
and device agent. HTTPS/WebSocket connects device identities to the Rust
control server. PostgreSQL owns authoritative control state and encrypted
vault records. Telemetry follows the [observability pipeline](05-observability.md).

## Ownership and dependencies

The central repository owns standards and assembly metadata. Runtime code lives
in the separate repositories in the [module catalog](../contracts/module-catalog.json);
it is not copied into a second central workspace.

| Boundary | Responsibility |
| --- | --- |
| Core domain | Pure entities, invariants and value objects |
| Core application | Use cases and ports; no concrete I/O |
| Protocol | Canonical versioned wire schemas and error contracts |
| Server | HTTP, identity delivery, PostgreSQL and TLS adapters; composition |
| Device agent | Background lifecycle and OS adapters |
| Desktop/mobile | Flutter presentation and typed bridge clients |
| Observability | Telemetry normalization, delivery and alert state |
| Other modules | Their declared capabilities and integrations |

Flutter does not own sync rules, secrets, shell execution or package policy.
Domain code imports no async runtime, filesystem, SQL, HTTP or UI libraries.
Application ports describe behavior, deadlines and cancellation; adapters own
I/O. Do not create a crate, process or abstraction for each diagram box unless
it has a real owner and an accepted responsibility.

Each rule, schema, token and mutable state has one canonical owner.
Centralization means reusing that owner, not routing unrelated work through
one global service or duplicating authority in a client cache.

## Contracts and execution

OpenAPI 3.1 and JSON Schema own wire contracts. Rust/Dart projections are
generated reproducibly and identify their source version; handwritten duplicate
wire DTOs are forbidden. Domain models are separate from transport DTOs.

Modules are compiled-in and manifest-driven. Runtime descriptors declare
capabilities, permissions, dependencies and supported platforms. Repository
metadata describes packaging; it must map explicitly to runtime descriptors
rather than imply that every repository is an activated module.
Permissions are least-privilege: a health-only adapter receives no credential
store or process-execution authority. Existing tool signatures remain binding.

UI and process adapters expose only allowlisted operations. A process adapter
uses an executable and argv vector, with bounded output and explicit environment,
working directory, timeout and cancellation; it does not construct a shell
command from user input. Existing tools retain their authorization boundaries.

Runtime native plugins, distributed orchestration and additional brokers require
a measured requirement and a separate decision. Native plugins additionally
require a signed, versioned ABI, compatibility negotiation and crash isolation.
Horizontal scale must preserve
ownership and consistency contracts; the alpha remains a bounded single-server
Compose deployment.
