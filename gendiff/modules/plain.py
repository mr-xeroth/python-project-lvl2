#!/usr/bin/env python3
import sys

from gendiff.modules.stringify import stringify


def string_empty(func):
    def wrap (value):
        result = None
        if value == '':
            result = "''"
        else:
            result = func(value)
        return result
    return wrap

stringify = string_empty(stringify)


def parse_diff(diff):
    diffs = "diff-", "diff+"
    values = []
    for x in diffs:
        try:
            value = diff[x]
        except KeyError:
            values.append(None)
        else:
            if isinstance(value, dict):
                values.append('[complex value]')
            else:
                values.append(stringify(value))
    return values


def get_diff(key, diff):
    values = parse_diff(diff)
    if values[0] and values[1]:
        return f" updated. From {values[0]} to {values[1]}\n"
    elif values[0]:
        return " removed\n"
    elif values[1]:
        return f" added with value: {values[1]}\n"


def plain(diff):
    def walk(diff, path):
        output = ''
        keys = [x for x in diff.keys() if isinstance(diff[x], dict)]
        for each in keys:
            if path:
                node_name = path + f'.{each}'
            else:
                node_name = str(each)
            opening = f"Property '{node_name}' was"

            if (closing := get_diff(each, diff[each])):
                output += opening + closing
            else:
                output += walk(diff[each], node_name)
        return output
    return walk(diff, '').rstrip('\n')


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
