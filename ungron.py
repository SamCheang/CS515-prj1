#!/usr/bin/env python3
import json
from sys import stdin
import re


def ungron(groned: str) -> dict:
    def parse_path(path):
        keys = re.findall(r"\w+|\[\d+\]", path)
        return [int(key[1:-1]) if key.startswith("[") else key for key in keys]

    def merge(data, keys, value):
        for key in keys[:-1]:
            if isinstance(key, int):
                while len(data) <= key:
                    data.append({})
                if not isinstance(data[key], dict):
                    data[key] = {}
            else:
                if key not in data:
                    data[key] = {}
                data = data[key]
        last_key = keys[-1]
        if isinstance(last_key, int):
            while len(data) <= last_key:
                data.append(None)
            data[last_key] = value
        else:
            data[last_key] = value

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
