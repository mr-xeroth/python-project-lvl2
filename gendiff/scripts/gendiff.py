#!/usr/bin/env python3
import sys
import argparse

from gendiff.core import generate_diff


def main():
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

    files = [args.first_file.name, args.second_file.name]

    print(generate_diff(files[0], files[1], args.format))


if __name__ == '__main__':
    main()
