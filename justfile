set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

fmt:
    cargo fmt --all

fmt-check:
    cargo fmt --all -- --check

test:
    cargo test --workspace

clippy:
    cargo clippy --workspace --all-targets -- -D warnings

check: fmt-check test clippy catalog-check

catalog-check:
    python3 -m json.tool contracts/module-catalog.json >/dev/null

standards-check: catalog-check
    test -s standarts/README.md
    test -s LICENSE

