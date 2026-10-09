# ADR 0001: permanent development and release branches

Status: accepted, 2026-10-09.

## Decision

Public NDS repositories retain both `main` and `dev` as permanent branches.
Scoped working branches submit pull requests to `dev`; reviewed integration
is promoted from `dev` to `main` through a pull request. Commits use
Conventional Commits and signatures. Neither permanent branch permits force
pushes or deletion.

The initial personal alpha requires the repository quality check before
merge. A second human approval is not required for a sole-maintainer project;
team approval rules are added when additional maintainers are enabled.
CODEOWNERS records review ownership without claiming a second reviewer exists.

Branch protection and passing checks do not authorize a product release,
deployment, credential change, recovery operation or destructive cleanup.

## Consequences

Existing working branches and uncommitted work are preserved. GitHub-hosted
checks use immutable action pins and minimal permissions. The source release
and module compatibility locks remain explicit; introducing these checks does
not itself publish a new standards or application release.
