# Product boundary

`nddev-device-sync` is a distributed control plane for NDDev devices, servers,
development tools and agent-work harnesses. It has one Flutter UI for desktop
and mobile, a Rust client core, Rust server components, and a server-side
observability pipeline.

The product coordinates these modules through typed contracts:

- GitHub Device Sync (GDS);
- Remote Device Sync (RDS);
- sysinfo;
- clipboard;
- cleaner;
- updater;
- harness account management;
- server inventory and health;
- logs, metrics, traces and alerts.

Each existing tool remains the owner of its own data and safety policy until a
deliberate migration is approved. The control plane consumes stable adapters,
receipts and health contracts rather than copying private databases.

The product owns device identity, synchronization metadata, connection
metadata, module state, alert state and the encrypted vault protocol. It does
not become a general-purpose remote shell, a replacement for Git, or a second
package manager.

