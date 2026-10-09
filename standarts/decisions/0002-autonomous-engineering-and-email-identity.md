# ADR 0002: autonomous engineering and passwordless owner identity

Status: accepted, 2026-10-09.

## Decision

The owner defines product outcomes and trust boundaries; the agent owns the
implementation, verification and approved delivery workflow. The engineering
contract is a small, executable system: one owner per rule, production paths
instead of placeholders, bounded work, measured optimization and removal of
superseded code. Standards and short decision records capture intent; code,
schemas, migrations and checks describe the implementation.

Alpha product sign-in uses email one-time codes, with no passwords or GitHub
sign-in alternative. One bootstrap owner is configured privately by the
operator; the product never claims an instance for the first public visitor.
GitHub remains an integration for repository tooling, not the NDS identity
provider. Email authentication, device identity and vault decryption remain
separate trust boundaries. OTP does not recover lost device or vault keys.

Normal and debug observability modes share one redacted event contract.
Debug increases diagnostic detail within explicit bounds; it does not expose
secrets. Tests execute real rules and adapters with isolated test inputs and
dependencies; mock responses are not acceptance evidence.

## Consequences

This replaces the GitHub-only identity decision in the current standards.
Published alpha tags and existing module locks keep their original meaning;
consumers adopt this decision through a subsequent versioned standards and
protocol change. No legacy GitHub login path is needed: it was never shipped
as a working NDS feature. New owner credentials or accounts are not provisioned
by this document, and no private owner address belongs in public source.

The next work begins with technical stabilization of the five existing
repositories. A usable application requires a deliberately selected set of
working modules and observed end-to-end acceptance, not the entire catalog.
Release, deployment and other external actions retain their authorization
boundaries. The no-backup/no-recovery policy is unchanged.
