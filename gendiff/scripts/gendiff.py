#!/usr/bin/env python3
import sys
import argparse

from gendiff.modules.generate_diff import generate_diff


def parse_cli_args():
    """
    returns (file1_name, file2_name, data_format, view_format)
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

    file_name = args.first_file.name
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        data_format = 'yaml'
    else:
        data_format = 'json'

    return args.first_file.name,\
        args.second_file.name,\
        data_format,\
        args.format


def file_read(file_name):
    data = None
    with open(file_name, 'r') as f:
        data = f.read()
    return data


def main():
    file1, file2, data_format, view_format = parse_cli_args()

    data1 = file_read(file1)
    data2 = file_read(file2)

    print(generate_diff(data1, data2, data_format, view_format))


if __name__ == '__main__':
    main()
