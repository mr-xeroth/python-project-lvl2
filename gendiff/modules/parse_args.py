"""To parse cli arguments for diff generation"""

import argparse
from gendiff.formatters.view_formats import VIEW_FORMATS, VIEW_DEFAULT


def parse_cli_args(argv) -> tuple:
    """Returns file1_name, file2_name, view_format strings"""

    # print('\nSYS ARGV:', sys.argv)
    # print('\nINT ARGV:', argv)
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', type=argparse.FileType('r'))

    parser.add_argument('second_file', type=argparse.FileType('r'))

    parser.add_argument(
        '-f', '--format',
        type=str,
        choices=VIEW_FORMATS,
        default=VIEW_DEFAULT,
        help='set the format of output'
    )

    args = parser.parse_args(argv)

    return args.first_file.name, args.second_file.name, args.format
