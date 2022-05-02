#!/usr/bin/env python3
import sys


def generate_diff(dict1, dict2): # noqa: max-complexity: 10
    def walk(dict1, dict2):
        output = {}
        keys_combined = sorted(set.union(set(dict1), set(dict2)))
        for each in keys_combined:
            if each in dict1 and each in dict2:
                if dict1[each] == dict2[each]:
                    value = dict1[each]
                else:
                    if isinstance(dict1[each], dict) and\
                       isinstance(dict2[each], dict):
                        value = walk(dict1[each], dict2[each])
                    else:
                        value = {"diff-": dict1[each],
                                 "diff+": dict2[each]}
            else:
                if each in dict1:
                    value = {"diff-": dict1[each]}
                if each in dict2:
                    value = {"diff+": dict2[each]}
            output[each] = value
        return output
    return walk(dict1, dict2)


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
