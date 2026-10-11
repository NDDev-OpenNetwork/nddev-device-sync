# ADR 0005: web client planning boundary

Status: proposed; follows the native first-version qualification.

The owner requests a browser application alongside desktop and mobile. Evaluate
Flutter Web with the same OpenNetwork design tokens, en/ru presentation, Rust
backend and versioned protocol. Extract presentation ports when the browser
caller exists; a catalog entry is not an implemented adapter.

Pure core/application rules remain shared. Browser I/O, key persistence,
WebAuthn, cookies, offline storage and clipboard permissions are separate
adapters. Native keyrings and the current FFI surface cannot be treated as browser
facilities. A browser key-store/trust decision and real browser qualification
precede secret workflows. Server-managed delivery under ADR 0006 does not
provide a browser key store or authorize persisting an unwrapped key in
localStorage/IndexedDB.

GDS/RDS and system tools retain their native agent, state and safety policies.
The browser uses explicitly supported agent capabilities and encrypted read
models. No arbitrary shell, copied tool databases, backup/recovery,
implicit deployment or alternate UI stack is authorized by this proposal.

Existing standards release locks retain their meaning. This proposal does not
declare web runtime support. ADR 0006 separately records the accepted
three-method identity target and server-managed automatic key delivery.

References: [Flutter Web](https://docs.flutter.dev/platform-integration/web),
[Web Crypto](https://www.w3.org/TR/WebCryptoAPI/),
[WebAuthn](https://www.w3.org/TR/webauthn-3/).


## Implementation sequence after native qualification

1. Inventory presentation imports and define only the ports actually consumed by
   the first browser screens. Share design tokens, localization and protocol
   schemas; keep native FFI, keyrings and system-tool adapters outside the bundle.
2. Decide browser session and device-proof ownership. Review a same-origin
   server/BFF with HttpOnly/Secure cookies, CSRF and origin checks, expiry and
   logout against the existing bearer-plus-device-signature contract. Do not
   equate an ambient browser session with possession of a native device key.
3. Deliver authenticated session/device/status views using a declared browser
   adapter. Validate error states, server capability discovery, accessibility,
   en/ru and reconnect on actual supported browsers before secret workflows.
4. Approve key-delivery and persistence behavior for the browser threat model:
   XSS, shared profiles, storage eviction, sign-out and private browsing. A
   non-extractable Web Crypto key does not prevent same-origin script from using
   it. Keep the first scope online-only unless offline access has a justified
   persistence and revocation contract. Never cache plaintext vault responses.
5. Add bounded vault read/write/conflict flows only after that decision, reusing
   server sequence/revision rules and validating real WebAuthn ceremonies. Review
   CSP, dependency integrity, no-store responses, logout/cache cleanup, concurrent
   tabs and expired sessions. Clipboard use requires an explicit user action and
   browser support; native tool execution needs an independently authorized agent
   capability, not a browser shell or a copied provider store.
6. Qualify Chromium, Firefox and Safari separately, including denied permissions,
   disabled storage, offline transitions, credential revocation and accessibility.
   Build provenance, protected-branch delivery and a concrete deployment review
   precede publication. No web code or deployment is implied by this plan.

References for the browser boundary: [Flutter Web FAQ](https://docs.flutter.dev/platform-integration/web/faq),
[OWASP session management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html),
[Web Crypto security considerations](https://www.w3.org/TR/WebCryptoAPI/#security-considerations).
