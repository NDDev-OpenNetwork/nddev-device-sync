# nddev-device-sync

License: GNU AGPL-3.0-only. See [`LICENSE`](LICENSE) and
[`TRADEMARKS.md`](TRADEMARKS.md).

`nddev-device-sync` is the planned distributed control plane for NDDev devices,
servers and agent-work tools. It provides one Rust core/server, one Flutter UI
for desktop and mobile, and explicit adapters for GDS, RDS, sysinfo, clipboard,
cleaner, updater and server monitoring.

The public implementation is self-hostable. It keeps the NDDev OpenNetwork
name, attribution and links to [nddev.ai](https://nddev.ai) in the standard
product surfaces.

The central repository is a standards and assembly repository. Runtime code is
implemented in the separate module repositories listed by
[`contracts/module-catalog.json`](contracts/module-catalog.json).

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

## Central repository contents

```text
standarts/                normative product and engineering standards
contracts/module-catalog.json  separate public module repository plan
docs/                      historical design notes
justfile                   standards validation entrypoint
```

## Verification

```sh
just standards-check
```

## Roadmap after the alpha standard is confirmed

1. Build the protocol and core alpha modules from their separate repositories.
2. Create the Flutter desktop/mobile clients and Rust local bridge.
3. Create the sync server, agent and observability service repositories.
4. Add SQLite/PostgreSQL migrations, device enrollment and vault records.
5. Add existing-tool adapters and official harness account flows.
6. Publish signed alpha artifacts for desktop, mobile and server.

## Repository topology

The central repository defines standards and the assembly contract. Runtime
modules are separate repositories under `NDDev-OpenNetwork` and consume a
versioned standards release. The future public self-hosting engine is
`NDDev-OpenNetwork/nddev-device-sync-estate`; a personal estate is deployment
configuration and is not a second product name.
