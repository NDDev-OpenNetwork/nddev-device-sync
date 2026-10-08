# nddev-device-sync working contract

This repository contains the public cross-platform application and generic
module contracts. It must never contain real account tokens, GitHub
organization data, private estate topology, machine inventory, or runtime
evidence.

## Architecture rules

- Keep domain and application crates independent of operating systems and UI.
- Put OS integration behind ports and small adapters in the module repository
  that owns the integration.
- Modules are compiled-in and manifest-driven in the first release. Do not add
  native dynamic loading until a signed, versioned plugin ABI exists.
- Account secrets belong in the native credential store; the state database may
  contain only redacted metadata and references.
- A harness adapter must declare official account-switch support. The account
  module must refuse switching when that capability is absent.
- Existing GDS, RDS, sysinfo, clipboard, cleaner, and updater tools remain
  owners of their own state and policies. This application orchestrates them
  through explicit adapters; it does not copy their databases or bypass their
  safety boundaries.

## Verification

Run `just standards-check` and validate the module catalog before review.
Runtime repositories own their Rust or Flutter test suites.
