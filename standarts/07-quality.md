# Quality gates

Every pull request must pass the smallest relevant checks and the full gate
before release:

## Rust

- `cargo fmt --all -- --check`;
- `cargo clippy --workspace --all-targets -- -D warnings`;
- unit, property and contract tests;
- `cargo nextest` for the workspace suite;
- `cargo deny` and `cargo audit`;
- coverage report for domain, protocol and sync-engine crates.

## Flutter

- `dart format --set-exit-if-changed`;
- `dart analyze`;
- unit and widget tests;
- integration tests on each supported desktop and mobile target;
- accessibility and localization checks;
- golden tests for core screens and error states.

## Integration

- start the Compose infrastructure from an empty state;
- run PostgreSQL migrations from zero;
- verify generated API and event clients;
- exercise offline outbox/inbox replay and conflict handling;
- send a telemetry event through Vector into OpenObserve;
- verify redaction and absence of secrets;
- check device enrollment, revocation and token rotation;
- verify release health endpoints and graceful shutdown.

## Supply chain

Lockfiles, pinned toolchains, dependency advisories, licenses, SBOM, image
provenance and signed release artifacts are part of the gate. CI actions are
pinned to immutable commits and receive the minimum token permissions.

