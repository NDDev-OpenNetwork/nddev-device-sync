# Desktop shell

This is a deliberately thin Tauri v2 shell. It owns window lifecycle and the
frontend bridge only; the Rust workspace owns module contracts and use cases.

The shell currently exposes one read-only command, `list_modules`, to prove the
boundary. Filesystem, arbitrary process and network permissions are not added
to the capability file. They will be introduced only with a dedicated module
permission and a bounded adapter.

With the Tauri CLI installed, run from this directory:

```sh
cargo tauri dev
```

