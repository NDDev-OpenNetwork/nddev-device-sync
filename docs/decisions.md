# Architecture decisions

## ADR-0001 — Rust core with a thin Tauri shell

**Status:** proposed.

The application uses a Rust domain/application core and Tauri 2.x only for the
desktop window and typed command bridge. A pure-Rust UI toolkit was considered,
but the first release values native WebView integration, accessibility support
and a small shell over avoiding every web technology. The domain stays usable
without the shell, so this choice is reversible.

## ADR-0002 — Compiled-in modules before runtime plugins

**Status:** proposed.

Modules are explicit Rust implementations behind versioned descriptors. This
keeps the first ABI small and makes permissions reviewable. Native dynamic
plugins are deferred until signing, ABI compatibility, crash isolation and
rollback are designed; the word “plugin” currently means a module boundary,
not arbitrary code loading.

## ADR-0003 — Native credential store for account secrets

**Status:** proposed.

Account metadata and secret bytes have different lifecycles and threat models.
Metadata is queryable local state; credentials belong to the operating system's
credential store. Tests use an in-memory fake and never need real accounts.

