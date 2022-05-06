#!/usr/bin/env python3
import sys
import os
import json
import yaml

from gendiff.modules.parse import parse
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify


def get_file_path(file_name):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, file_name)


def batch_read(files):
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


def generate_diff(file1, file2, format="stylish"):
    func_index = {"stylish": stylish, "plain": plain, "json": jsonify}

    data = batch_read((file1, file2))

    if format in func_index:
        return func_index[format](parse(data[0], data[1]))


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
