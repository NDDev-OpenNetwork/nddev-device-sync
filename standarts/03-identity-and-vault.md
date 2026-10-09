# Identity, authorization and vault

## Product identity

NDS alpha sign-in offers email OTP and GitHub OAuth with PKCE for one account.
There are no passwords or hidden test-login paths. The two-method decision is
recorded in [ADR 0003](decisions/0003-dual-sign-in-and-platform-scope.md).

An operator privately configures one bootstrap owner address. No public
registration or first-visitor ownership claim exists. The owner has a stable
internal user ID, independent of the email address; identity comparisons follow
one explicit normalization rule. Real addresses and provider credentials never
belong in public source, fixtures or manifests.

OTP challenges use a cryptographically secure generator, finite lifetime,
bounded attempts, resend limits and bounded storage. A resend invalidates the
previous code. Successful verification atomically consumes the challenge;
concurrent replay must not create another session. Persist a protected verifier,
not a plaintext code or an easily brute-forced unkeyed hash of a short code.
Responses must not reveal whether an address is permitted. Enforce both subject
and source abuse limits without unbounded rate-limit state.

The server sends codes through a narrow email-delivery adapter. Delivery
credentials belong to the operator's secret store. Provider acceptance is not
proof of mailbox delivery. Sessions have explicit expiry, revocation and
authorization scope. Email possession authenticates the account; it does not
prove possession of a device key or grant vault decryption.
Email OTP trusts mailbox control; it is not phishing-resistant multifactor
authentication. Delivery and authentication secrets never become log fields.

GitHub sign-in uses an unguessable single-use state, PKCE S256, an exact
allowlisted callback and bounded one-time handoff to the initiating client.
The server revalidates the provider identity after code exchange and matches
its stable numeric ID to an explicit private owner binding. Never merge accounts
by a client-supplied identity, display name or unverified email. Both methods
issue the same NDS session type and enforce the same authorization policy.
The operator stores the OAuth application secret separately; provider tokens
are transient for identity verification and are not retained as product
credentials. Linking a provider requires explicit authenticated revalidation
or an operator's preconfigured binding; it is not open registration.

## Device and service identities

A per-installation signing key is generated on the device; the private key
stays in native secure storage. After user authentication, a short-lived
enrollment challenge and proof-of-possession bind the public key and device
metadata to the authenticated owner. Revocation and explicit key-rotation
transitions are enforced by the server and preserve authorization boundaries.
Server records include their public identity, capabilities and heartbeat.

Service identities for agents, email delivery and telemetry are separate from
user/device credentials. Vector/OpenObserve credentials remain in the central
telemetry pipeline. Authorization is checked at the owning use case and storage
boundary, not inferred from a client-supplied tenant or user ID.

## Vault

Harness tokens, SSH credentials and API keys are E2EE records. The server stores
ciphertext, metadata and device-wrapped key material; it cannot read plaintext.
Each record has an owner, purpose, scope and lifecycle. Native credential stores
hold local secrets; metadata stores and UI events hold references or redacted
metadata, never plaintext secret bytes. Public DTOs and logs cannot expose
resolved secrets. OTP verifiers and session records follow the separate
authentication contract, not the vault encryption model.

A new vault creates keys locally. An additional device receives existing
vault key material wrapped by an already-authorized device. Email sign-in alone
cannot reconstruct or reset these keys. No server escrow or password fallback
is introduced. Account switching uses only declared official harness support.

## Recovery policy

The product creates and retains no backups or recovery copies of the vault,
device keys, databases, local state or generated evidence. If every authorized
device key is lost, the old encrypted records remain unrecoverable. Email OTP
does not change this policy. Retry queues are bounded transport state with
explicit retention, not recovery copies.
