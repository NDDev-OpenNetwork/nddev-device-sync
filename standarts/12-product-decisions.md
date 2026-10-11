# Product decisions

- Public source and self-hosting are first-class requirements.
- Rust, Flutter and public design tokens use AGPL-3.0-only. NDDev OpenNetwork
  attribution and the https://nddev.ai link remain in product surfaces.
- Email OTP, GitHub OAuth PKCE and passkeys are the accepted sign-in target for
  one privately configured bootstrap owner. Vault access prepares automatically
  after sign-in through server-managed keys, independently of other devices.
  Existing locked clients implement two methods and trusted-device transfer.
  See [identity](03-identity-and-vault.md) and
  [ADR 0006](decisions/0006-agent-first-sign-in-and-vault-access.md).
- Agent interfaces and Flutter consume the same Rust use cases through typed,
  bounded capabilities and redacted results. Native consumers use secret
  references; the control plane preserves each existing provider's policies.
- The server owns committed state; devices catch up at startup and reconnect.
  Server-managed vault keys use a wrapping key outside PostgreSQL. The server
  has decryption authority; this supersedes the client-only E2EE boundary.
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
