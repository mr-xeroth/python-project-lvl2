#!/usr/bin/env python3
import sys


def diff_format(key_, key_entries, dict1, dict2):
    result = None
    if all(key_entries):
        if dict1[key_] == dict2[key_]:
            result = {
                'type': 'untouched',
                'value': dict1[key_]
            }
        else:
            result = {
                'type': 'updated',
                'value': {
                    'old': dict1[key_],
                    'new': dict2[key_]
                }
            }
    elif key_entries[0]:
        result = {
            'type': 'removed',
            'value': dict1[key_]
        }
    elif key_entries[1]:
        result = {
            'type': 'added',
            'value': dict2[key_]
        }
    return result


def dict_compare(dict1, dict2):
    output = {}
    keys_combined = sorted(set.union(set(dict1), set(dict2)))
    for each in keys_combined:
        result = None
        keys_exist = [each in x for x in (dict1, dict2)]

        nodes_are_dict = None

        if all(keys_exist):
            nodes_are_dict = all(
                [isinstance(x, dict) for x in (dict1[each], dict2[each])]
            )

        if nodes_are_dict:
            result = dict_compare(dict1[each], dict2[each])
        else:
            result = diff_format(each, keys_exist, dict1, dict2)

        output[each] = result
    return output


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
