#!/usr/bin/env python3
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


def get_diff(flags, data):
    diff_keys = ['diff-', 'diff+']
    result = {}
    for i, diff in enumerate(diff_keys):
        if flags[i]:
            result.update({diff: data[i]})
    return result


def diff_format(diff):
    result = None
    if 'diff-' in diff and 'diff+' in diff:
        result = {
            'type': 'updated',
            'value': {
                'old': diff['diff-'],
                'new': diff['diff+']
            }
        }
    elif 'diff-' in diff:
        result = {
            'type': 'removed',
            'value': diff['diff-']
        }
    elif 'diff+' in diff:
        result = {
            'type': 'added',
            'value': diff['diff+']
        }
    return result


def dict_compare(dict1, dict2):
    output = {}
    keys_combined = sorted(set.union(set(dict1), set(dict2)))
    for each in keys_combined:
        result = None
        is_value, data = parse_key(each, [dict1, dict2])
        if all(is_value) and (data[0] == data[1]):
            result = data[0]
        elif all([isinstance(x, dict) for x in data]):
            result = dict_compare(data[0], data[1])
        else:
            result = diff_format(get_diff(is_value, data))
        output[each] = result
    return output


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
