#!/usr/bin/env python3
import sys
import json
import yaml

from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify


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


def parse_format(flags, data):
    diff_keys = ['diff-', 'diff+']
    result = {}
    for i, diff in enumerate(diff_keys):
        if flags[i]:
            result.update({diff: data[i]})
    return result


def parse(dict1, dict2):
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
            else:
                result = parse_format(is_value, data)
            output[each] = result
        return output
    return walk(dict1, dict2)


def convert_to_dict(data, format_):
    result = None
    if format_ == "yaml":
        result = yaml.load(data, Loader=yaml.SafeLoader)
    elif format_ == "json":
        result = json.loads(data)
    return result


def generate_diff(data1, data2, data_format="json", view_format="stylish"):
    view_index = {"stylish": stylish, "plain": plain, "json": jsonify}

    dict1 = convert_to_dict(data1, data_format)
    dict2 = convert_to_dict(data2, data_format)

    if view_format in view_index:
        return view_index[view_format](parse(dict1, dict2))


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
