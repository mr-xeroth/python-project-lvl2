#!/usr/bin/env python3
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify

import argparse
import yaml
import json
import sys


def parse_key(key_, dicts):
    flags = []
    data = []
    for x in range(len(dicts)):
        try:
            value = dicts[x][key_]
        except KeyError:
            flags.append(False)
            data.append(None)
        else:
            flags.append(True)
            data.append(value)
    return flags, data


def diff_format(flags, data):
    diff_keys = ['diff-', 'diff+']
    result = {}
    for i, diff in enumerate(diff_keys):
        if flags[i]:
            result.update({diff: data[i]})
    return result


def generate_diff(dict1, dict2):
    def walk(dict1, dict2):
        output = {}
        keys_combined = sorted(set.union(set(dict1), set(dict2)))
        for each in keys_combined:
            result = None
            is_value, data = parse_key(each, [dict1, dict2])
            if all(is_value) and (data[0] == data[1]):
                result = data[0]
            elif all([isinstance(x, dict) for x in data]):
                result = walk(data[0], data[1])
            if not result:
                result = diff_format(is_value, data)
            output[each] = result
        return output
    return walk(dict1, dict2)


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
