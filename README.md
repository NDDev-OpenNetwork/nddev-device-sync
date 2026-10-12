# nddev-device-sync

NDS is the public, self-hostable NDDev OpenNetwork control plane for devices,
servers and agent-work tools. Rust owns the domain and system behavior; Flutter
provides desktop, mobile and web presentation in English and Russian. The product keeps
the NDDev OpenNetwork name and [nddev.ai](https://nddev.ai) attribution.

License: AGPL-3.0-only. See [LICENSE](LICENSE) and [TRADEMARKS.md](TRADEMARKS.md).

This repository owns the [standards](standarts/README.md) and
[module catalog](contracts/module-catalog.json). Runtime modules are separate
repositories. The catalog reserves boundaries; it does not assert that planned
modules are implemented or require building all of them for the first alpha.

The [engineering contract](standarts/13-engineering-and-agent-standard.md)
governs autonomous delivery, minimal code and state, real verification and
scope control. [ADR 0002](standarts/decisions/0002-autonomous-engineering-and-email-identity.md)
records the engineering baseline; [ADR 0006](standarts/decisions/0006-agent-first-sign-in-and-vault-access.md)
records email OTP, GitHub and passkey sign-in with automatic vault access and
native agent capabilities. The coordinated implementation includes
server-managed owner keys, encrypted replica catch-up, paginated vault records,
explicit conflict resolution and signed client diagnostics. Advertised sign-in
methods depend on the instance configuration. A compiled platform is not proof
of runtime qualification; each runtime repository owns that evidence.
Existing module locks and published alpha tags keep their original meaning.

The catalog describes repository boundaries and declared platforms, not a
release bill of materials or a runtime capability response. The accepted
[offline browser scope](standarts/decisions/0007-offline-browser-client.md)
is implemented by the [web assembly](https://github.com/NDDev-Technocracy-OpenNetwork-NDS/nddev-device-sync-web),
which reuses the shared Flutter UI and Rust domain/application modules. Browser
adapters provide encrypted local credentials, a durable replica and telemetry
queue, while the server remains authoritative for committed state. The web
repository owns artifact provenance and browser qualification; an alpha catalog
entry does not assert deployment or support for untested browsers.

Run `just setup` once to install isolated, pinned structural tooling, then
`just check` for the central repository's structural checks. Runtime
repositories own their implementation and acceptance checks. Passing central
checks is not evidence that the application or observability pipeline works.

To check an actual compiled-in descriptor against the central contract, run
`.venv/bin/python scripts/check-contracts.py /path/to/module/contracts/module.json`.
This validates schema and dependency declarations; runtime activation, dependency
graph compatibility and OS behavior remain the runtime owner’s responsibility.
