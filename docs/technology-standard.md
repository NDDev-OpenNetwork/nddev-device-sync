# nddev-device-sync technology standard (proposal)

Status: **proposed, pending product confirmation**.

This document freezes the default choices for the first implementation. A
change after the first released module must be recorded as an ADR with the
reason, migration impact and validation evidence.

## Product shape

`nddev-device-sync` is a per-user desktop control plane for macOS, Ubuntu/Linux
and Windows. It coordinates existing NDDev tools and owns the account registry
module. It is not a replacement for GDS, RDS, sysinfo, clipboard, cleaner or
updater, and it is not a server or a remote desktop product.

## Proposed stack

| Area | Standard | Reason |
| --- | --- | --- |
| Language | Rust 2024 edition | one memory-safe core on all targets |
| Toolchain | stable Rust; MSRV 1.88 until explicitly raised | matches the existing NDDev Rust tools and keeps CI reproducible |
| Desktop shell | Tauri 2.x stable | native OS WebView, small Rust-first shell and explicit capabilities |
| Frontend | static HTML/CSS + small TypeScript modules | no framework runtime or state duplication in the first release |
| Async | Tokio only in the application/adapters layer | domain remains deterministic and runtime-free |
| Serialization | Serde with versioned DTOs | typed Rust boundaries and stable IPC payloads |
| Metadata store | SQLite via `rusqlite` with migrations and WAL | mature local transactions and easy inspection; never on a network filesystem |
| Secrets | native credential stores through the keyring adapter | Keychain, Secret Service/KWallet, and Windows Credential Manager |
| Internal events | typed bounded channels | explicit module coupling and backpressure |
| Existing tools | argv-only CLI, JSON protocol or Unix/named socket adapters | preserve each tool's owner and safety policy |
| Extensions | compiled-in modules first | no unsafe native plugin ABI or arbitrary code loading |
| Release updates | signed artifacts and existing updater policy | one authority for system/tool updates; no duplicate package manager |
| CI | GitHub Actions matrix + fmt/test/clippy/audit/deny | repeatable checks on all three operating systems |

The Tauri dependency is limited to the shell. The domain and application
crates must remain usable as a headless CLI/service and must not import Tauri
types.

## Hexagonal boundaries

1. **Domain** contains entities, invariants, module manifests and account
   state transitions. It has no I/O, OS, UI or runtime dependency.
2. **Application** contains use cases and ports: module registry, state store,
   secret store, process runner, platform services and harness account adapter.
3. **Adapters** implement one port at a time. OS adapters are separated into
   macOS, Linux and Windows modules; existing-tool adapters never share their
   private files.
4. **UI** calls a small allowlist of application commands and receives redacted
   DTOs/events. It cannot execute arbitrary processes or read arbitrary paths.

## Module rules

Each module has an id, semantic version, API version, supported platforms,
capabilities, permissions and dependencies. The registry validates the graph
before activation and refuses missing dependencies, incompatible APIs and
cycles.

The first release uses compiled-in implementations registered from manifests.
Runtime native dynamic libraries are out of scope until we have a signed ABI,
version negotiation, crash isolation and a tested upgrade/rollback protocol.
If runtime extensions become necessary, the preferred next boundary is a
signed manifest plus a narrow IPC or WASM process, not an in-process dylib.

## Account module rules

The fifth module stores account metadata (id, harness, label, status and
timestamps) in SQLite and secret/session bytes in the native credential store.
Tokens, cookies and raw session files never enter the database, logs or UI
events.

Each harness adapter declares its authorization method and whether official
account switching is supported. The UI can offer “add account” for an
authorization adapter, but “switch” is enabled only for `official` adapters.
The module never rewrites vendor dot-directories or fabricates a switch by
copying session files. A harness can later add an official browser/device-code
flow without changing the account model.

## First release scope

The first vertical slice is intentionally small:

- list and health-check the compiled-in modules;
- read-only adapters for sysinfo and existing tool health;
- metadata schema and native secret-store port for accounts;
- one harness adapter with a documented official authorization/switch flow;
- signed, bounded update receipt display;
- Tauri capability file with no unrestricted shell, filesystem or network
  permission.

GDS/RDS write operations, generic harness auto-discovery, runtime plugins and
bulk account migration start only after this slice passes the cross-platform
contract tests.

## Open decisions before public publication

- repository visibility and license;
- the first officially supported harness adapters;
- whether the UI ships in English and Russian in v0.1 or starts in English;
- the exact SQLite migration crate and release signing service;
- the minimum Windows and Ubuntu versions for the first support matrix.

