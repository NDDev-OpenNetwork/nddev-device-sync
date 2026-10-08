# Security and trust boundaries

- The frontend can call only explicit application commands exposed by the
  desktop shell. It never receives arbitrary shell, filesystem or network
  access.
- Process adapters use an executable plus an argv vector, never a shell string.
  Environment and working directory are explicit and bounded.
- Account secrets are written to the platform credential store. The app's
  database, logs, telemetry and events hold references and redacted metadata.
- Module permissions are declarative. A module that only reads health cannot
  receive credential-store or process-execution permission.
- GDS and updater signatures remain authoritative. The app does not weaken
  their verification or install an unverified replacement.
- Account switching is an adapter capability, never a best-effort rewrite of
  vendor config/session files. If the official client cannot switch accounts,
  the UI says so and leaves the client untouched.
- All event payloads are designed for redaction. Tokens, cookies, SSH private
  keys and raw process environments are prohibited values.

