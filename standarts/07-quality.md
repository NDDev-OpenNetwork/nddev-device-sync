# Quality gates

Checks prove observable behavior of the accepted scope. Test count, coverage
percentage and a green job are not substitutes for correctness.

## Test contract

- Exercise production functions, serializers, migrations and adapters.
  Check invariants, boundaries, rejection paths and relevant concurrency.
- Use real isolated dependencies for adapter acceptance: PostgreSQL, actual
  TLS sockets and native credential stores on their supported platforms.
  A mock, fake, stub or canned success response is not integration evidence.
- Test inputs may be generated, temporary and intentionally invalid. This is
  necessary for deterministic boundary and negative tests; never use private
  user data, real account secrets or production databases as fixtures.
- Keep demonstration records, fake-success adapters and test-only login bypasses
  out of runtime. Pure rules take explicit inputs; they need no I/O substitute.
- Induce failures at real boundaries where practical: rejected transactions,
  expired records, broken connections and actual resource saturation. Do not
  assert only that an internal method was called or duplicate the implementation
  as the test oracle.
- External-provider delivery acceptance uses an authorized isolated account and
  recipient. Observe the real outcome. If it cannot run, report it as unverified;
  do not silently replace it with a mock and mark the gate passed.
- Tests own and clean only their ephemeral resources. Never reset a real keyring,
  estate, database or unrelated worktree to make a test pass.

## Rust and Flutter

Rust repositories run formatting, Clippy with warnings denied, unit/property/
contract tests and nextest, plus dependency advisory/license checks. Coverage
identifies untested domain/protocol/sync paths; it is diagnostic, not a quota.

Flutter repositories run formatting, analysis, unit/widget tests and relevant
accessibility/localization checks. Supported target acceptance uses actual
platform builds and interaction tests. Golden tests cover stable visual
contracts when they detect a meaningful regression.

## Contracts, integration and release

- Validate schema semantics, OpenAPI references and valid/invalid payloads.
  JSON parsing alone is only a syntax check.
- Reproduce generated clients/tokens and reject drift from their canonical source.
- Test migrations from empty state, repeat application and each supported upgrade
  path. Verify privileges, required schema version and failure behavior.
- For implemented features, exercise identity/enrollment/revocation, offline
  replay/conflicts, redaction and bounded shutdown through real adapters.
- Observe telemetry delivery and alert lifecycle through the actual pipeline;
  test both normal and debug modes without relaxing redaction.

Every PR runs the checks relevant to its changed contracts, plus the repository's
established gate. A release additionally needs the implemented end-to-end flows,
supported-target acceptance, SBOM, artifact signatures and build provenance.
Lockfiles, immutable CI actions and toolchain pins make inputs reproducible.
Documentation-only changes need structural validation, not invented runtime tests.

An active alpha application must execute its selected workflows with real
modules and dependencies. A health endpoint, module descriptor, empty screen,
mock response or unexecuted test does not establish feature completion.
