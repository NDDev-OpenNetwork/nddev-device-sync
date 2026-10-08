# Repository topology

The public OpenNetwork organization owns generic implementation repositories.
The central `nddev-device-sync` repository owns this standards directory,
assembly metadata and the module catalog. Each module repository has its own
release tag, lockfile, tests and `standarts.lock`.

The future `nddev-device-sync-estate` repository is the public self-hosting
engine. A personal or team deployment is configuration and runtime state for
that engine; it does not become a separate product named `nddev-estate`.

The first alpha implementation wave creates repositories only when their
module has code and a meaningful release boundary. The catalog reserves the
correct names now without creating empty repositories.

Every module repository must contain:

```text
AGENTS.md
LICENSE
README.md
standarts.lock
module.yaml
Cargo.lock or pubspec.lock
justfile
tests/
```

The module manifest declares its repository, API version, capabilities,
platforms, dependencies and standards release. A module must not depend on
private estate files or on a mutable branch of another repository.

