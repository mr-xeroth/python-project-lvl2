#!/usr/bin/env python3
import sys


def diff_format(key_, key_entries, nodes):
    result = None
    if all(key_entries):
        if nodes[0] == nodes[1]:
            result = {
                'type': 'untouched',
                'value': nodes[0]
            }
        else:
            result = {
                'type': 'updated',
                'value': {
                    'old': nodes[0],
                    'new': nodes[1]
                }
            }
    elif key_entries[0]:
        result = {
            'type': 'removed',
            'value': nodes[0]
        }
    elif key_entries[1]:
        result = {
            'type': 'added',
            'value': nodes[1]
        }
    return result


def dict_compare(dict1, dict2):
    output = {}
    keys_combined = sorted(set.union(set(dict1), set(dict2)))
    for each in keys_combined:
        result = None

        keys_exist = [each in x for x in (dict1, dict2)]

        combo = zip(keys_exist, (dict1, dict2))

        nodes = [x[1][each] if x[0] else None for x in combo]

        if all(keys_exist):
            nodes_are_dict = [isinstance(x, dict) for x in nodes]
        else:
            nodes_are_dict = [False]

        if all(nodes_are_dict):
            result = dict_compare(nodes[0], nodes[1])
        else:
            result = diff_format(each, keys_exist, nodes)

        output[each] = result
    return output


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
