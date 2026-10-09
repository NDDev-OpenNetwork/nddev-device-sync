# nddev-device-sync working contract

This public repository owns standards and generic assembly contracts.
Never add real credentials, owner addresses, private organization policy,
estate topology, machine inventory or runtime evidence.

Read the [engineering contract](standarts/13-engineering-and-agent-standard.md),
[development workflow](standarts/16-development-workflow.md), current Git state
and the owning module's AGENTS.md, standarts.lock and module.yaml before work.
The owner defines outcomes and trust boundaries; the agent completes authorized
implementation, verification and delivery without repeatedly asking about
routine engineering choices. Preserve unrelated dirty work and live services.

## Boundaries

- Domain/application stay independent of OS, UI and concrete I/O.
- Native credentials and E2EE keys remain outside metadata stores and telemetry.
- Product email-OTP/GitHub identity is separate from device identity, vault decryption
  and third-party harness accounts. Read the locked identity contract.
- Modules are compiled-in and manifest-driven; planned entries are not working
  adapters. Add only code used by an accepted behavior.
- Existing GDS, RDS and system tools own their state and safety policies.
  Use explicit adapters; do not copy their databases or bypass their controls.
- Harness account switching requires declared official provider support.
- Follow the approved branch/PR workflow. No implicit releases, deployment,
  credential changes, backup/recovery or unrelated cleanup.

## Verification

Run `just standards-check` and `just catalog-check` before review.
These are structural checks only. Runtime repositories own behavioral tests;
report exactly which code, dependencies and platforms were exercised.
