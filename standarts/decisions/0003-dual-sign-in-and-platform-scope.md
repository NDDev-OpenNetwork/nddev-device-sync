# ADR 0003: two sign-in methods and complete module scope

Status: accepted, 2026-10-10.

## Decision

The owner accepts email OTP and GitHub OAuth with PKCE as two sign-in methods
for the same NDS account. This supersedes only the email-only restriction in
ADR 0002; the autonomous engineering, test and observability decisions remain.
There are no passwords, open registration or implicit first-visitor ownership.

A private bootstrap configuration identifies the permitted owner and explicit
GitHub identity binding. GitHub identity uses the provider's stable numeric ID.
Do not link accounts merely because a display name or unverified email matches.
An authenticated, reverified owner may explicitly link an additional sign-in
identity; a preconfigured binding must be equally explicit. Both methods issue
the same scoped NDS session and neither recovers device or vault keys.

The application scope includes GDS, RDS, sysinfo, clipboard, cleaner, updater
and accounts, with device/sync and observability services. Targets are Linux,
macOS, Windows, Android and iOS. Implement through bounded coordinated changes,
not dormant scaffolding. Platform capabilities remain explicit: mobile clients
may control an authorized desktop agent without executing desktop CLIs locally.
Unavailable capabilities report their actual state rather than fabricated success.

## Consequences

Protocol and consumers adopt the changed identity contract together. Published
tags remain immutable. An active module needs real adapter acceptance and
observable failures. A build is distinct from execution on each supported OS;
report missing platform acceptance rather than implying cross-platform proof.

Actual owner addresses, provider bindings and deployment secrets stay outside
public repositories. Account/provider provisioning and live deployment use
their existing authorization boundaries. No backup or recovery is introduced.
