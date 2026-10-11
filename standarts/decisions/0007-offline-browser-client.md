# ADR 0007: browser client and durable offline replicas

Status: accepted, 2026-10-11; implementation and platform qualification required.

## Decision

The owner requires a Flutter web application alongside desktop and mobile,
including offline work and reconciliation with the authoritative server. This
supersedes the online-only starting assumption in ADR 0005. An empty shell or
an online dashboard does not satisfy this scope.

Reuse OpenNetwork tokens, en/ru presentation and generated typed interfaces.
Rust owns application rules on native targets and WebAssembly. Browser storage,
credentials, HTTP, clocks, lifecycle and clipboard are explicit adapters;
JavaScript/Dart must not acquire a second implementation of revision, conflict,
cryptographic envelope or authorization rules. Native tools remain native.

## Browser trust boundary

Serve application assets and browser API from the same HTTPS origin. Online
authentication uses a Secure, HttpOnly, host-only session cookie with a narrow
SameSite policy. Exact-origin/CSRF checks apply independently of device proof.
Preserve email OTP, GitHub PKCE and passkeys and the existing account policy;
cookie possession is not possession of an enrolled device signing key.

Persistent browser credentials use a non-extractable, browser-managed
cryptographic key and authenticated-encrypted credential material. Unwrapped
vault/signing keys stay inside the Rust/browser credential adapter, outside
presentation DTOs, telemetry and plaintext persistent storage. The operational
credential store is separate from the ciphertext replica and its metadata.
No token or plaintext key is stored in localStorage, an application cache or a
service worker cache. Persist only encrypted record bodies and bounded public
replication metadata in the replica.

This does not make the browser an OS keychain or prevent compromised same-origin
script from using available keys. Enforce a restrictive CSP, self-hosted pinned
assets, no untrusted scripts and no plaintext HTTP-response caching. Clearing
browser storage can destroy unsent work; this is not a recovery mechanism.
Report unavailable/evictable storage honestly and request persistent storage
where supported. Failure to obtain it must not become a false durability claim.

## Consistency and authorization

Offline access requires a previous successful online sign-in and active-device
verification. Protect the cached authorization and bind it to the exact origin,
owner, device and existing session expiry. It is evidence of the last check,
not a fresh server decision. Expiry, explicit local sign-out or a known
revocation locks secret use. A disconnected device cannot discover a new remote
revocation immediately; reconnect revalidates before uploading queued changes.
Failed revalidation preserves encrypted unsent work without transmitting it or
silently changing its owner, device or key.

Use the same encrypted operation format, idempotency, committed server sequence,
revision checks, tombstones and explicit conflict resolution on every platform.
Persist an outbox transaction before confirming a local edit. Authenticate and
validate the entire inbox page before committing its state and cursor. Read
models expose local pending edits, conflicts and the last complete observation.
Only a complete successful catch-up establishes freshness. Storage/quota errors,
interrupted commits and unknown network outcomes must remain explicit.

Closing a tab, restarting offline and simultaneous tabs cannot discard an
acknowledged local edit or create independent writers with conflicting local
state. Coordinate access through browser-owned storage/locking facilities with
bounded admission. Never use a relaxed-only persistence adapter while reporting
durable success. Do not replace an uncertain store with an empty database.

Offline application assets are versioned separately from operational data.
Cache only an explicit build manifest, never identity/vault/API responses.
An update must not force-reload active work or erase compatible replica state.
Reconcile on startup, resume and reconnect. Browsers do not guarantee execution
after a page closes, so synchronization and log delivery cannot promise it.

## Observability and qualification

Reuse the canonical Rust event/redaction contract. Include browser startup,
framework/async failures, storage admission/commit failures, offline/resume,
authentication/revocation, synchronization/conflicts and delivery degradation.
Normal/debug modes retain identical privacy guarantees. Bound queues, retention,
retry and shutdown; expose actual acknowledgements, loss and freshness. An
offline event is not remotely delivered until the pipeline accepts it.

Acceptance uses actual browser storage, cryptography, HTTPS and PostgreSQL:
offline restart and edits, cross-device replay/conflicts, concurrent tabs,
interrupted writes, quota/permission denial, logout/expiry/revocation and upgrades.
Trace real browser operations through the existing collector/Vector/OpenObserve
pipeline. Qualify Chromium, Firefox and Safari separately and run affected native
regressions. Build support does not assert real browser or hardware acceptance.

No general remote shell, replacement tool database, backup/recovery, runtime
plugin system or external alert channel is introduced. Deployment is a separate
reviewed action. Existing source locks and release tags retain their meaning.

References: [Flutter Web](https://docs.flutter.dev/platform-integration/web/faq),
[Web Crypto](https://www.w3.org/TR/webcrypto/),
[IndexedDB](https://www.w3.org/TR/IndexedDB/),
[OAuth browser application guidance (draft)](https://www.ietf.org/archive/id/draft-ietf-oauth-browser-based-apps-26.html),
[OWASP session management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
