#!/usr/bin/env python3
from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify

import argparse
import yaml
import json
import sys


def batch_load(files):
    content = []
    for fname in files:
        data = None
        with open(fname) as f:
            if fname.endswith('.yaml') or fname.endswith('.yml'):
                data = yaml.load(f, Loader=yaml.FullLoader)
            elif fname.endswith('.json'):
                data = json.load(f)
            content.append(data)
    return content


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(0)

    args = parser.parse_args(sys.argv[1:])

    files = [args.first_file.name, args.second_file.name]

    data = batch_load(files)
    data = [x for x in data if isinstance(x, dict)]
    if len(data) != 2:
        print('File load failed')
        sys.exit(1)

    diff = generate_diff(data[0], data[1])

    if args.format == 'plain':
        print(plain(diff))
    elif args.format == 'json':
        print(jsonify(diff))
    else:
        print(stylish(diff))


if __name__ == '__main__':
    main()
