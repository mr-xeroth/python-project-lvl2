#!/usr/bin/env python3
import sys

from gendiff.modules.stringify import stringify


def quote_string(func):
    def wrap(value):
        result = None
        if type(value) is str:
            result = f"'{value}'"
        else:
            result = func(value)
        return result
    return wrap


stringify = quote_string(stringify)


def filter_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return stringify(value)


def get_diff(diff):
    report = None
    if 'type' in diff and 'value' in diff:

        if diff['type'] == 'updated':
            values = [filter_value(x) for x in [diff['value']['old'],
                                                diff['value']['new']]]
            report = f" updated. From {values[0]} to {values[1]}\n"
        elif diff['type'] == 'removed':
            report = " removed\n"
        elif diff['type'] == 'added':
            report = f" added with value: {filter_value(diff['value'])}\n"
    return report


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

            if (closing := get_diff(diff[each])):
                output += opening + closing
            else:
                output += walk(diff[each], node_name)
        return output
    return walk(diff, '').rstrip('\n')


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
