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
precede secret workflows; sign-in cannot reconstruct existing vault keys.

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
