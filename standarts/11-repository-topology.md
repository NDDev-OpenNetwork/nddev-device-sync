# Repository topology

The central repository owns standards, assembly metadata and the module catalog.
Each runtime module owns its implementation, tests, dependency locks and release
boundary. The future public self-hosting engine is `nddev-device-sync-estate`;
a personal deployment is private configuration, not another product.

Create a module repository when an accepted behavior needs that boundary.
Catalog reservations do not authorize empty repositories or inactive services.

A module contains AGENTS.md, LICENSE, a short README, standarts.lock, module.yaml,
a justfile and its applicable tests. Runtime dependency locks are committed and
checked in CI. A schema-only repository instead pins its validation/generation
tooling; it does not invent a Cargo workspace just to have a Cargo.lock.

Repository metadata declares packaging and ownership. Runtime descriptors
declare API version, capabilities, permissions, platforms and dependencies.
Their relationship is explicit and validated, with no conflicting handwritten
projections. Modules consume immutable source releases, never private estate
files or another repository's mutable branch.

Generated clients and design-token projections record their canonical source
and regenerate without manual edits. The release/check path verifies drift.
Keep operational addresses, accounts, secrets and evidence outside public source.
