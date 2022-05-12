#!/usr/bin/env python3
import sys
import argparse

from gendiff.modules.generate_diff import generate_diff


def parse_cli_args():
    """
    returns (file1_name, file2_name, view_format)
    """
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', type=str, default="stylish",
                        help='set format of output: "plain", "json", \
                        default "stylish" ')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(0)

    args = parser.parse_args(sys.argv[1:])

    return args.first_file.name,\
        args.second_file.name,\
        args.format


def main():
    file1, file2, view_format = parse_cli_args()

    print(generate_diff(file1, file2, view_format))


if __name__ == '__main__':
    main()
