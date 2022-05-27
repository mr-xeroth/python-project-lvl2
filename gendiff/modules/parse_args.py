"""To parse cli arguments for diff generation"""

import argparse
import sys


def parse_cli_args(argv) -> tuple:
    """Returns file1_name, file2_name, view_format strings.
Prints help and quits if no arguments given"""

    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', type=str, default="stylish",
                        help='set format of output: "plain", "json", \
                        default "stylish" ')

    # if len(sys.argv) == 1:
    #     parser.print_help(sys.stderr)
    #     sys.exit(0)

    args = parser.parse_args(argv)

    return args.first_file.name, args.second_file.name, args.format
