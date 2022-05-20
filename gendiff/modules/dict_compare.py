#!/usr/bin/env python3
import sys


def dict_compare(dict1, dict2):
    output = {}
    keys_combined = sorted(set.union(set(dict1), set(dict2)))

    for key in keys_combined:
        if key in dict1 and key not in dict2:
            output[key] = {
                'type': 'removed',
                'value': dict1[key]
            }
        elif key not in dict1 and key in dict2:
            output[key] = {
                'type': 'added',
                'value': dict2[key]
            }
        elif all([isinstance(x, dict) for x in (dict1[key], dict2[key])]):
            output[key] = {
                'type': 'nested',
                'value': dict_compare(dict1[key], dict2[key])
            }
        elif dict1[key] == dict2[key]:
            output[key] = {
                'type': 'untouched',
                'value': dict1[key]
            }
        else:
            output[key] = {
                'type': 'updated',
                'value': {
                    'old': dict1[key],
                    'new': dict2[key]
                }
            }
    return output


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
