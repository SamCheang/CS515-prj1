#!/usr/bin/env python3
from typing import List, Tuple
from argparse import ArgumentParser
from os.path import exists, isdir
from sys import stdin


class IsADirError(Exception):
    pass


def wc(files: List[str]) -> Tuple[int, int, int, str]:
    for file in files:
        if not exists(file):
            exit(-1)
            # raise FileExistsError(f"{file} does not exist")
        if isdir(file):
            exit(-1)
            # raise IsADirectoryError(f"{file}: read: Is a directory")

        with open(file, "r") as fp:
            txt = fp.read()

        lines = txt.count("\n")
        words = len(txt.split())
        chars = len(txt)

        yield lines, words, chars, file


def wc_pipeline(pipe: str) -> Tuple[int, int, int]:
    lines = pipe.count("\n")
    words = len(pipe.split())
    chars = len(pipe)
    return lines, words, chars


def output_str(
    lines: int,
    words: int,
    chars: int,
    file: str,
    pipe: bool = False,
    l: bool = False,
    w: bool = False,
    c: bool = False,
) -> str:
    if not any((l, w, c)):
        lines = f"{lines:>8}"
        words = f"{words:>8}"
        chars = f"{chars:>8}"
    else:
        lines = f"{lines:>8}" if l else ""
        words = f"{words:>8}" if w else ""
        chars = f"{chars:>8}" if c else ""

    file = f" {file}" if not pipe else ""

    return f"{lines}{words}{chars}{file}"


if __name__ == "__main__":
    PARSER = ArgumentParser(epilog="wc emulation")

    PARSER.add_argument("files", nargs="*", type=str, help="List of files")
    PARSER.add_argument("-l", action="store_true", help="count lines")
    PARSER.add_argument("-w", action="store_true", help="count words")
    PARSER.add_argument("-c", action="store_true", help="count chars")

    args = PARSER.parse_args()

    if not stdin.isatty():
        piped = stdin.read()
        lines, words, chars = wc_pipeline(piped)
        print(
            output_str(
                lines, words, chars, None, pipe=True, l=args.l, w=args.w, c=args.c
            )
        )

        exit()

    for lines, words, chars, file in wc(args.files):
        print(output_str(lines, words, chars, file, l=args.l, w=args.w, c=args.c))
