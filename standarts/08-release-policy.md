# Release policy

## Channels

The release sequence is:

```text
alpha → beta → release
```

The first product artifacts are `alpha`. Promotion requires all quality,
security, observability and compatibility gates for the preceding channel.

## Versions

The synchronized release train uses `v0.0.n` while the product is pre-1.0.
Each artifact has its own channel and component tag:

```text
desktop-v0.0.1-alpha.1
mobile-v0.0.1-alpha.1
server-v0.0.1-alpha.1
```

The `n` value identifies the coordinated product train. The alpha/beta/release
counter identifies the candidate within that channel. Desktop, mobile and
server may ship independently only when their protocol compatibility is
explicitly recorded.

Stable product semantics begin at `v1.0.0`; until then, breaking changes are
allowed only with a migration note and a versioned contract update.

## Artifacts

Desktop artifacts are signed per operating system and architecture. Mobile
artifacts use the platform stores or signed distribution packages. Server
artifacts are signed container images with SBOM and build provenance. Release
receipts contain source commit, toolchain, dependency lock hashes, artifact
digests and migration version.

