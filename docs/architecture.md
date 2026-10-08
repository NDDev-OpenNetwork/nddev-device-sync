# Architecture (historical draft)

The normative architecture is now in
[`../standarts/02-architecture.md`](../standarts/02-architecture.md). This
file records the earlier Tauri-oriented exploration and is retained as design
history. The current module boundaries are defined in
[`../standarts/02-architecture.md`](../standarts/02-architecture.md) and the
public module catalog.

## Runtime shape

The app is split into a common Rust core and three small platform adapters:

```text
Tauri UI (thin, allowlisted commands)
             |
       application use cases
             |
  ports: store / keyring / process / platform / module
       /             |             \
  macOS adapter   Linux adapter   Windows adapter
```

The domain crate has no async runtime, filesystem calls, subprocess calls,
network clients or UI types. That keeps the highest-value rules fast to test
and makes the same binary logic usable by every target.

## Module contract

Every module has an immutable descriptor containing an id, semantic version,
API version, supported platforms, capabilities, permissions and dependencies.
The registry validates identifiers, rejects duplicate dependencies, checks API
compatibility and produces a dependency-first activation order.

The first release uses compiled-in module implementations. A runtime native
plugin ABI would make memory safety, signing, upgrades and cross-version
compatibility much harder. If runtime extensions become necessary, the next
step is a signed manifest plus a narrow IPC/WASM boundary rather than loading
arbitrary platform-specific dynamic libraries into the main process.

## Existing modules

| Module | Owner of state | App responsibility |
| --- | --- | --- |
| GDS | `github-device-sync` | invoke verified commands, display receipts |
| RDS | existing RDS client/server | invoke local client, display connection health |
| sysinfo | `rldyour-sysinfo` | read socket protocol and render snapshot |
| clipboard | `rldyour-clipboard` | invoke existing daemon/CLI |
| cleaner | `rldyour-cleaner` | request plan/run and show preservation result |
| updater | `rldyour-updater` | trigger policy-approved update and show receipt |
| accounts | this app | register accounts and broker official harness adapters |

No module receives another module's database path or secret. Cross-module
coordination is typed events and use-case calls, so dependencies remain
visible and testable.

## Account lifecycle

```text
PendingAuthorization -> Authorized -> Active
                         |              |
                         v              v
                      Revoked        Inactive
```

An account record contains an opaque id, harness id, label, optional username
hint, status and timestamps. Its token/session bytes are addressed by a
deterministic key in the native credential store. Secret values never enter
SQLite, JSON events, logs or UI payloads.

Each harness adapter declares `Official` or `Unsupported` switching. The
application refuses an activation request for an unsupported harness. A future
adapter may provide an official browser login flow, device-code flow, or vendor
account switch command without changing the domain model.

## Persistence

The planned state adapter is a per-user SQLite database with migrations, file
permissions restricted to the user, and WAL mode for concurrent UI/service
reads. It stores module state, account metadata, redacted receipts and schema
version only. WAL is local-machine only; the database must never live on a
network filesystem.
