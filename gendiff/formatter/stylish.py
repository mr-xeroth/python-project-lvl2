#!/usr/bin/env python3
import sys

from gendiff.formatter.stringify import stringify


def get_diff(diff):
    mark, values = None, None
    types = {
        'nested': ' ',
        'untouched': ' ',
        'updated': '*',
        'removed': '-',
        'added': '+'
    }

    # simple value that isn't of dict type
    if not isinstance(diff, dict):
        return '', diff

    # unpack values from "diff" kind of dict
    if 'type' in diff and 'value' in diff:
        mark = types[diff['type']]
        if mark == '*':
            values = mark, diff['value']['old'], diff['value']['new']
        else:
            values = mark, diff['value']
    else:
        # nondiff dict
        values = '', diff

    return values


def stylish_format(indent, mark, key_, data):
    double = ''
    template = '{}{} {}: {}\n'
    if not mark:
        mark = ' '
    if mark == '*':
        mark = '-'
        double = template.format(indent, mark, key_, next(data))
        mark = '+'
    return double + template.format(indent, mark, key_, next(data))


def stylish(data, indent=4):
    def walk(data, depth):
        if not isinstance(data, dict):
            return stringify(data)
        tab_close = indent * depth * ' '
        tab_indent = tab_close + (indent - 2) * ' '
        output = ''
        for each in data.keys():
            mark, *values = get_diff(data[each])
            parsed = map(lambda x: walk(x, depth + 1), values)
            output += stylish_format(tab_indent, mark, each, parsed)
        return '{\n' + output + f'{tab_close}}}'
    return walk(data, 0)


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
