# nddev-device-sync

`nddev-device-sync` is the planned distributed control plane for NDDev devices,
servers and agent-work tools. It provides one Rust core/server, one Flutter UI
for desktop and mobile, and explicit adapters for GDS, RDS, sysinfo, clipboard,
cleaner, updater and server monitoring.

The current checkout is a compileable architecture draft rather than a
finished installer. It establishes boundaries before integrations are added,
so the desktop UI does not become a second owner of every tool's state.

The normative technology and product decisions are recorded in
[`standarts/README.md`](standarts/README.md). The earlier files under `docs/`
and the Tauri shell are exploratory drafts; the Flutter-first standard in
`standarts/` is authoritative for the alpha product.

## Design decisions

- **Rust core, Flutter UI:** domain and use cases are independent of the UI and
  OS. Flutter is presentation-only; the Rust core owns system access, sync,
  secrets and observability.
- **Hexagonal architecture:** domain rules have no I/O; application use cases
  depend on ports; OS, process, keyring and existing-tool integrations are
  adapters.
- **Compiled-in modules first:** the initial modules are registered through a
  manifest and dependency graph. Native dynamic plugins are intentionally
  deferred until a signed, versioned ABI exists.
- **Account manager as module five:** account metadata is stored locally, while
  tokens and session secrets go to the native credential store. Switching is
  enabled only for harness adapters that declare official support.
- **Existing tools stay authoritative:** GDS, RDS and the four tools keep their
  own data, policies and update mechanisms. This app coordinates them through
  narrow adapters and never copies their private state.

## Workspace

```text
crates/domain             pure entities, invariants and module graph
crates/application        use cases and ports
crates/adapters-memory    deterministic test adapters
crates/adapters-keyring   macOS Keychain/Linux Secret Service/Windows Credential Manager
crates/desktop            exploratory smoke-test shell; alpha UI follows standarts/
apps/                     server, agent and Flutter client targets
standarts/                normative product and engineering standards
docs/architecture.md      historical architecture draft
docs/security.md          threat model and permission rules
contracts/                versioned module contract examples
```

## Verification

```sh
cargo fmt --all -- --check
cargo test --workspace
cargo clippy --workspace --all-targets -- -D warnings
cargo run -p nddev-device-sync
```

## Roadmap after the alpha standard is confirmed

1. Create the Flutter desktop/mobile shell and the Rust local bridge.
2. Add SQLite and PostgreSQL migrations with the offline outbox/inbox protocol.
3. Add device enrollment, vault records and server-agent health.
4. Add OpenTelemetry, Vector, OpenObserve and Rust alert state.
5. Add existing-tool adapters and official harness account flows.
6. Publish signed alpha artifacts for desktop, mobile and server.
