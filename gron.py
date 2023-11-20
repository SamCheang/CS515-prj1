#!/usr/bin/env python3
import json
from argparse import ArgumentParser
from os.path import exists, isdir
from sys import stdin
from typing import Any, List


def read_json(json_file: str) -> Any:
    if not exists(json_file):
            exit(-1)
            # raise FileExistsError(f"{file} does not exist")
    if isdir(json_file):
            exit(-1)
            # raise IsADirectoryError(f"{file}: read: Is a directory")

    with open(json_file, "r") as fp:
        return json.load(fp)


def flatten(json: Any, base_key: str = "json") -> List[str]:
    res = []
    flatten_helper(json, res, base_key)
    return res


def flatten_helper(json: Any, res: List, base_key: str = "json") -> None:
    if isinstance(json, dict):
        res.append(f"{base_key} = {{}};")
        for key in sorted(json.keys()):
            flatten_helper(json[key], res, base_key=f"{base_key}.{key}")

    elif isinstance(json, list):
        res.append(f"{base_key} = [];")
        for idx, item in enumerate(json):
            flatten_helper(item, res, base_key=f"{base_key}[{idx}]")

    elif isinstance(json, str):
        res.append(f'{base_key} = "{json}";')

    else:
        res.append(f"{base_key} = {json};")


if __name__ == "__main__":
    PARSER = ArgumentParser(epilog="gron emulation")

    PARSER.add_argument("json_file", nargs="?", type=str, help="base object name")
    PARSER.add_argument("--obj", default="json", help="base object name")

    args = PARSER.parse_args()
    data = read_json(args.json_file) if stdin.isatty() else json.loads(stdin.read())
    json_flattened = flatten(data, base_key=args.obj)

    for item in json_flattened:
        print(item)
