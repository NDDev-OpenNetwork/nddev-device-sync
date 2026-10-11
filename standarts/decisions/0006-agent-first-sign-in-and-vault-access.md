# ADR 0006: agent-first sign-in and automatic vault access

Status: accepted, 2026-10-11.

## Decision

Email OTP, GitHub OAuth PKCE and passkeys are three sign-in methods for the
same NDS account and authorization policy. This supersedes the two-method
restriction in ADR 0003. Passkeys use standard WebAuthn verification; linking
credentials requires a freshly reverified owner session, not implicit account
merging. Implementation and real platform qualification precede advertising
the third method as available.

An authenticated owner is entitled to their vault through any of these methods.
The product prepares vault access automatically after sign-in; a mandatory
manual QR/code transfer is superseded as the desired new-device workflow.
Authentication, device proof and cryptographic key possession remain distinct
implementation responsibilities. Authentication assertions cannot be treated
as the existing random vault encryption key.

Agents and Flutter use the same Rust application use cases through explicit
capabilities. Agent interfaces expose typed operations, secret references,
bounded execution, stable redacted errors and observable results. Authorized
native consumers resolve secrets at the point of use; keys, session tokens and
resolved secrets remain outside presentation DTOs, model transcripts and
telemetry. Existing providers retain their authorization and safety policies.
Do not add a general execution framework or unrestricted shell to implement
these capabilities.

## Server authority

The server owns committed sync state and vault key delivery. An authenticated,
enrolled, active device obtains the owner's existing vault key from the server
without another device being online. Store owner keys as authenticated-encrypted
envelopes in PostgreSQL under a distinct operator-managed wrapping key outside
that database. Deliver key material only through the native authenticated HTTPS
boundary, never presentation DTOs or telemetry. The server has decryption
authority; this is encryption at rest and in transit, not client-only E2EE.

Devices reconcile at startup, after enrollment and on reconnect/resume. Durable
outboxes, revision conflicts and verified inbox cursors retain their existing
invariants. Bounded catch-up continues while the server reports more history;
only a complete successful observation advances the caught-up timestamp.
Offline devices expose stale/pending/conflicted state, not global freshness.

## Transition

Existing module locks and published tags keep their original meaning. Clients
at the time of this decision implemented two sign-in methods and explicit
trusted-device key transfer;
this decision is not runtime acceptance. Adopt server-managed keys and the
three-method contract through a coordinated version boundary. Existing locally
created vaults require one authenticated registration of their existing key
before server-only provisioning is possible. Preserve keys and ciphertext;
an unavailable existing key is an explicit transition error, never a reason to
replace the key or reset history. Published migrations and tags remain immutable.
The no-backup/no-recovery policy remains unchanged.

Reference: [WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/).
