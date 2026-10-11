#!/usr/bin/env python3
"""Validate owned schemas/catalog; optionally validate actual runtime descriptors."""
import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON property: {key}")
            result[key] = value
        return result
    return json.loads(path.read_text(), object_pairs_hook=unique)


def validator(name):
    schema = load(ROOT / 'contracts' / name)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def catalog(data):
    validator('module-catalog.schema.json').validate(data)
    for field in ['id', 'repository']:
        values = [module[field] for module in data['modules']]
        if len(set(values)) != len(values):
            raise ValueError(f'duplicate catalog {field}')
    for module in data['modules']:
        if 'all' in module['platforms'] and len(module['platforms']) != 1:
            raise ValueError('all cannot be combined with named platforms')
        expected = ('nddev-opennetwork-design-system' if module['id'] == 'design-system'
                    else 'nddev-device-sync-' + module['id'])
        if module['repository'] != expected:
            raise ValueError('repository does not match its module boundary')


def descriptor(data):
    validator('module-manifest.json').validate(data)
    dependencies = [dependency['id'] for dependency in data['dependencies']]
    if data['id'] in dependencies or len(set(dependencies)) != len(dependencies):
        raise ValueError('self or duplicate module dependency')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('runtime_manifests', nargs='*', type=Path)
    args = parser.parse_args()
    catalog(load(ROOT / 'contracts/module-catalog.json'))
    validator('module-manifest.json')
    for path in args.runtime_manifests:
        descriptor(load(path))
    print(f'Catalog and schemas valid; {len(args.runtime_manifests)} runtime descriptors checked.')


if __name__ == '__main__':
    main()
