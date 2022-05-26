#!/usr/bin/env python3

from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.parse_args import parse_cli_args


def main():
    file1, file2, view_format = parse_cli_args()

    print(generate_diff(file1, file2, view_format))


if __name__ == '__main__':
    main()
