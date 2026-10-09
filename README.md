# nddev-device-sync

NDS is the public, self-hostable NDDev OpenNetwork control plane for devices,
servers and agent-work tools. Rust owns the domain and system behavior; Flutter
provides desktop/mobile presentation in English and Russian. The product keeps
the NDDev OpenNetwork name and [nddev.ai](https://nddev.ai) attribution.

License: AGPL-3.0-only. See [LICENSE](LICENSE) and [TRADEMARKS.md](TRADEMARKS.md).

This repository owns the [standards](standarts/README.md) and
[module catalog](contracts/module-catalog.json). Runtime modules are separate
repositories. The catalog reserves boundaries; it does not assert that planned
modules are implemented or require building all of them for the first alpha.

The [engineering contract](standarts/13-engineering-and-agent-standard.md)
governs autonomous delivery, minimal code and state, real verification and
scope control. [ADR 0002](standarts/decisions/0002-autonomous-engineering-and-email-identity.md)
records the engineering baseline; [ADR 0003](standarts/decisions/0003-dual-sign-in-and-platform-scope.md)
defines email OTP and GitHub sign-in for one account. Existing module
locks and published alpha tags keep their original contracts until consumers
adopt a subsequent standards release.

Run `just check` for the central repository's structural checks. Runtime
repositories own their implementation and acceptance checks. Passing central
checks is not evidence that the application or observability pipeline works.
