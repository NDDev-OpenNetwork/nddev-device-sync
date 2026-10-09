# Product decisions

- Public source and self-hosting are first-class requirements.
- Rust, Flutter and public design tokens use AGPL-3.0-only. NDDev OpenNetwork
  attribution and the https://nddev.ai link remain in product surfaces.
- Passwordless email OTP is the alpha product sign-in method. One bootstrap
  owner is configured privately; device identity and E2EE vault access remain
  separate. See [identity](03-identity-and-vault.md) and
  [ADR 0002](decisions/0002-autonomous-engineering-and-email-identity.md).
- Docker Compose is the alpha deployment path. The first scale target is one
  person or small team; future ownership boundaries are explicit, while team
  administration remains deferred.
- Telemetry export is enabled by default and operator-controlled. Normal/debug
  modes share the same redaction guarantees and observable delivery state.
- Desktop, mobile and server have separate versioned artifacts in the coordinated
  alpha -> beta -> release train.
- Existing tools retain authority until approved migrations pass compatibility
  checks. Their repositories and private state are not disposable scaffolding.
- Backup/recovery remains disabled, including after the first release, until an
  explicit future product decision.
