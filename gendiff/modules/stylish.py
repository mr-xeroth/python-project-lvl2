#!/usr/bin/env python3
import sys

from gendiff.modules.stringify import stringify


def get_diff(diff):
    if not isinstance(diff, dict):
        return '', diff
    if 'type' in diff and 'value' in diff:
        if diff['type'] == 'updated':
            result = '*', diff['value']['old'], diff['value']['new']
        elif diff['type'] == 'removed':
            result = '-', diff['value']
        elif diff['type'] == 'added':
            result = '+', diff['value']
    else:
        result = '', diff
    return result


def neat_stringify(indent, mark, key_, data):
    double = ''
    template = '{}{} {}: {}\n'
    if not mark:
        mark = ' '
    elif mark == '*':
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
            # list of sorts [diff_mark, value1_pos, value2_opt]
            values = get_diff(data[each])
            parsed = map(lambda x: walk(x, depth + 1), values[1:])
            output += neat_stringify(tab_indent, values[0], each, parsed)
        return '{\n' + output + f'{tab_close}}}'
    return walk(data, 0)


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
