# Identity, authorization and vault

## Actors

- **User identity** authenticates a person through an approved OAuth2/OIDC
  provider with PKCE. Provider passwords are never stored by this product.
- **Device identity** is a per-installation signing key generated on the
  device. The private key stays in the native keyring or secure platform
  storage.
- **Server identity** is a registered device/server record with a public key,
  capabilities, owner, status and last heartbeat.
- **Service identity** is used by Vector, OpenObserve integrations and server
  agents. Service credentials are separate from user and device credentials.

## Enrollment

1. A user authenticates to the control server.
2. The client generates a device key pair locally.
3. The server issues a short-lived enrollment challenge.
4. The device proves possession of the private key.
5. The server stores only the public key and device metadata.
6. The user can revoke or rotate the device at any time.

Server access is represented by an endpoint plus a device enrollment key or
mutual TLS identity. The OpenObserve ingestion token is a separate secret and
is held only by the central telemetry pipeline.

## Vault

The vault stores harness tokens, SSH credentials, API keys and other secret
material as end-to-end encrypted records. The server stores ciphertext,
metadata and device-wrapped key material; it cannot read plaintext secrets.
Each record has an owner, purpose, scope, creation time, rotation state and
revocation state.

Credentials are never written to SQLite metadata, logs, telemetry, generated
reports, Git repositories or UI event payloads. Access is explicit, scoped and
audited. Account switching is exposed only when the harness adapter declares
an official switching mechanism.

## Recovery policy

The product deliberately creates and retains **no backups and no recovery
copies** for the vault, device keys, server database, local state or generated
evidence. This is a product standard. If all authorized device keys and local
secrets are lost, encrypted records are unrecoverable by design.

Operational retry queues and temporary delivery buffers are bounded transport
state; they are not backups and must be deleted according to their retention
policy.

