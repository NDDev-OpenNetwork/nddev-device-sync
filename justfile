set shell := ["bash", "-euo", "pipefail", "-c"]

default:
    @just --list

check: standards-check catalog-check

catalog-check:
    python3 -m json.tool contracts/module-catalog.json >/dev/null

standards-check: catalog-check
    test -s standarts/README.md
    test -s LICENSE
