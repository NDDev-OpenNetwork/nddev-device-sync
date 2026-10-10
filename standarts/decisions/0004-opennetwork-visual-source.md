# ADR 0004: use the NDDev OpenNetwork direction UI kit

Status: accepted by the owner, 2026-10-10.

The NDS palette was independently invented as cyan/violet space surfaces. The
owner confirmed that NDS must use the existing NDDev platform's OpenNetwork
direction, including its tokens and UI kit. A yellow accent alone is insufficient.

Use OpenNetwork's yellow brand (`#FFD83F`), theme-specific gold button fills,
neutral surfaces, IBM Plex Sans, scales, control geometry and interaction states.
The public design-system repository owns a versioned, reproducible OpenNetwork
projection of the platform design source. Record its source revision and input
hashes; export only reusable visual data, never private platform configuration.
Native Flutter controls retain their semantics, keyboard behavior and platform
accessibility while adopting that kit. Both themes preserve the source's
contrast-corrected roles. Product-specific layouts remain in the client.

Preserve the authentic NDDev mark geometry. Bundle redistributable fonts with
their licenses; no font downloads at runtime. Launcher and in-app marks use the
OpenNetwork direction's color, not the Dev direction or a new NDS palette.

This explicitly supersedes the earlier independently styled visual direction.
Old standards tags and consumer locks remain immutable. Until a new standards
release, an updated consumer records this amendment's source commit alongside
its baseline lock; that amendment covers visual rules only. Update design-system
and client source pins together, with contrast, reflow, native builds and actual
rendered review. This correction does not authorize unrelated features or a
formal product release.
