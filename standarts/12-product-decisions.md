# Product decisions

- Public source and self-hosting are first-class requirements.
- Code, server, modules and OpenNetwork design tokens use AGPL-3.0-only.
- The NDDev OpenNetwork name, attribution and `https://nddev.ai` link remain in
  standard product surfaces.
- GitHub is the first and only alpha user identity provider.
- Docker Compose is the alpha deployment path.
- The first scale target is one person or one small team per self-hosted
  instance. Multi-tenancy and team administration are designed into the
  contracts but implemented later.
- Backup and recovery are disabled until the owner explicitly enables a future
  module. This remains true after the first release.
- Telemetry is enabled by default and can be disabled by the self-hosted
  operator. Disabled telemetry must be visible in health and settings.
- Desktop, mobile and server have separate release versions and artifacts.
- Existing repositories are replaced by the new module repositories only after
  migration, compatibility checks and release receipts. Old repositories are
  archived afterward.

