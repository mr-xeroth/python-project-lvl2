#!/usr/bin/env python3
"""To run generate_diff with cli args"""

from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.parse_args import parse_cli_args


def main(argv=None):
    file1, file2, view_format = parse_cli_args(argv)

    print(generate_diff(file1, file2, view_format))


if __name__ == '__main__':
    main()
