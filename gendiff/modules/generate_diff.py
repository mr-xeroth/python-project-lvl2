#!/usr/bin/env python3
import sys
import json
import yaml

from gendiff.modules.dict_compare import dict_compare
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify


def file_read(file_name):
    data = None
    with open(file_name, 'r') as f:
        data = f.read()
    return data


def get_file_format(file_name):
    format_ = None
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        format_ = 'yaml'
    elif file_name.endswith('.json'):
        format_ = 'json'
    return format_


def convert_to_dict(data, type_):
    result = None
    if type_ == "yaml":
        result = yaml.load(data, Loader=yaml.SafeLoader)
    if type_ == "json":
        result = json.loads(data)
    return result


def generate_diff(file1, file2, view_format="stylish"):
    view_index = {"stylish": stylish, "plain": plain, "json": jsonify}

    if view_format not in view_index:
        return

    data1, type1 = file_read(file1), get_file_format(file1)
    data2, type2 = file_read(file2), get_file_format(file2)

    dict1 = convert_to_dict(data1, type1)
    dict2 = convert_to_dict(data2, type2)

    return view_index[view_format](dict_compare(dict1, dict2))


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
