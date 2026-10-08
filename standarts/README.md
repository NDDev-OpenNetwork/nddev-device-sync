# nddev-device-sync standards

This directory is the normative product standard for `nddev-device-sync`.
The documents are written in English because code, APIs, events, schemas,
release metadata and operational identifiers use English. The product UI
supports English and Russian from the first user-facing release.

The standard is intentionally explicit about data ownership, trust boundaries,
release channels, observability and the recovery policy. An implementation may
add detail, but it must not silently weaken a rule here. Any change to a rule
requires an ADR in `standarts/decisions/` before code is changed.

## Normative documents

1. [Product boundary](01-product.md)
2. [System architecture](02-architecture.md)
3. [Identity and vault](03-identity-and-vault.md)
4. [Sync and data](04-sync-and-data.md)
5. [Observability](05-observability.md)
6. [Infrastructure](06-infrastructure.md)
7. [Quality gates](07-quality.md)
8. [Release policy](08-release-policy.md)
9. [Internationalization and visual system](09-i18n-and-visual-system.md)
10. [Operations](10-operations.md)

## Status

The product starts in the `alpha` channel. These documents describe the
baseline for `v0.0.n-alpha.k`; they are reviewed before the first public
artifact and again before moving to `beta`.

