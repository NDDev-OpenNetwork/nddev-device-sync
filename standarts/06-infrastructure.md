# Infrastructure

## Local and server runtime

`just` is the canonical command runner. Docker Compose is the only alpha
deployment path for the server stack. Compose defines the local development
services and the initial single-server deployment. The same
service names, health endpoints, migrations and environment contract are used
in both environments.

The initial server stack is:

- `nddev-sync-server`;
- `nddev-observability`;
- PostgreSQL 18.x;
- Vector;
- OpenObserve;
- optional server-agent connections to other hosts.

Images are pinned by digest in release deployments. Services run as non-root
users with explicit networks, healthchecks, bounded resources and read-only
root filesystems where supported. Secrets are mounted through Docker Compose
secrets or the server's native secret mechanism; credentials do not live in
`.env` files committed to Git.

## Database roles

PostgreSQL roles are separated for migrations, runtime application access,
read-only observability queries and administrative maintenance. The application
does not use a superuser. Row-level security is available when the account or
organization model requires tenant separation.

## Storage policy

PostgreSQL and OpenObserve use named data volumes with explicit retention and
resource limits. The no-backup/no-recovery policy in
`03-identity-and-vault.md` applies to these volumes as well. A release rollback
may restore an earlier image and schema-compatible application version; it does
not restore deleted data.
