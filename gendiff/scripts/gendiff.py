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


def get_file_format(file_name):
    format_ = None
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        format_ = 'yaml'
    elif file_name.endswith('.json'):
        format_ = 'json'
    return format_


def file_read(file_name):
    data = None
    with open(file_name, 'r') as f:
        data = f.read()
    return data


def main():
    file1, file2, view_format = parse_cli_args()

    data1, data2 = file_read(file1), file_read(file2)
    data1_type, data2_type = get_file_format(file1), get_file_format(file2)

    print(generate_diff(data1, data1_type, data2, data2_type, view_format))


if __name__ == '__main__':
    main()
