#!/usr/bin/env python3
import sys
import json
import yaml
import argparse

from gendiff.modules.parse import parse
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify



def generate_diff(json1, json2, format="stylish"):
    func_index = {"stylish": stylish, "plain": plain, "json": jsonify}
    if format in func_index:
        return func_index[format](parse(json1, json2))


def batch_load(files):
    content = []
    for fname in files:
        data = None
        with open(fname) as f:
            if fname.endswith('.yaml') or fname.endswith('.yml'):
                data = yaml.load(f, Loader=yaml.SafeLoader)
            elif fname.endswith('.json'):
                data = json.load(f)
            content.append(data)
    return content


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration \
                                     files and shows a difference.')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', type=str, default="stylish",
                        help='set format of output')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(0)

    args = parser.parse_args(sys.argv[1:])

    files = [args.first_file.name, args.second_file.name]

    data = batch_load(files)
    is_complete = [isinstance(x, dict) for x in data]
    if not all(is_complete):
        print('File reading failed')
        sys.exit(1)

    print(generate_diff(data[0], data[1], args.format))


if __name__ == '__main__':
    main()
