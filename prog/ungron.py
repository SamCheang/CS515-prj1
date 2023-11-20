#!/usr/bin/env python3
import json
from sys import stdin
import re

def ungron(groned: str) -> dict:
    def parse_path(path):
        keys = re.findall(r"\w+|\[\d+\]", path)
        return [int(key[1:-1]) if key.startswith("[") else key for key in keys]

    def ensure_structure(data, key, is_last_key):
        if isinstance(key, int):
            if not isinstance(data, list):
                return [None] * key + [{} if is_last_key else []]
            while len(data) <= key:
                data.append(None)
            if data[key] is None or (is_last_key and not isinstance(data[key], dict)):
                data[key] = {} if is_last_key else []
            return data[key]
        else:
            if not isinstance(data, dict):
                data = {k: data[k] for k in range(len(data))} if isinstance(data, list) else {}
            if key not in data or (is_last_key and not isinstance(data[key], dict)):
                data[key] = {}
            return data[key]

    def merge(data, keys, value):
        for key in keys[:-1]:
            data = ensure_structure(data, key, False)
        last_key = keys[-1]
        last_data = ensure_structure(data, last_key, True)
        last_data[last_key] = value

    result = {}
    lines = [line for line in groned.split("\n") if line.strip() != ""]

    for line in lines:
        path, value = line.split(" = ")
        value = json.loads(value[:-1])  # Remove trailing semicolon and parse JSON
        keys = parse_path(path)
        merge(result, keys, value)

    return result

if __name__ == "__main__":
    ungroned = ungron(stdin.read())
    print(json.dumps(ungroned, indent=2))
