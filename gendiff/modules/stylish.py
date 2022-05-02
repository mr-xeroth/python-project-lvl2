#!/usr/bin/env python3
import sys


def stringify(value):
    translate = {True: 'true', False: 'false', None: 'null', '': ' '}
    new = translate.get(value)
    return new if new else value


def parse_diff(diff):
    diffs = "diff-", "diff+"
    values = []
    for x in diffs:
        try:
            value = diff[x]
        except KeyError:
            values.append(None)
        else:
            values.append({'val': value})
    return values


def get_diff(diff):
    if not isinstance(diff, dict):
        return '', diff
    values = parse_diff(diff)
    if values[0] and values[1]:
        return '*', values[0]['val'], values[1]['val']
    elif values[0]:
        return '-', values[0]['val']
    elif values[1]:
        return '+', values[1]['val']
    else:
        return '', diff


def neat_format(data, indent=4):
    def walk(data, depth):
        if not isinstance(data, dict):
            return data
        tab_close = indent * depth * ' '
        tab_indent = tab_close + (indent - 2) * ' '
        template = f'{tab_indent}{{}} {{}}: {{}}\n'
        output = ''
        for each in data.keys():
            # list of sorts [diff_mark, value1_pos, value2_opt]
            values = data[each]
            parsed = map(lambda x: walk(x, depth + 1), values[1:])
            if (mark := values[0]):
                if mark == '*':
                    mark = '-'
                    output += template.format(mark,
                                              each, next(parsed))
                    mark = '+'
            else:
                mark = ' '
            output += template.format(mark, each, next(parsed))
        return '{\n' + output + f'{tab_close}}}'
    return walk(data, 0)


def stylish(diff):
    def walk(diff):
        output = {}
        if not isinstance(diff, dict):
            return stringify(diff)
        for each in diff.keys():
            # list of sorts [diff_mark, value1_pos, value2_opt]
            values = get_diff(diff[each])
            parsed = map(lambda x: walk(x), values[1:])
            if (mark := values[0]) and mark == '*':
                value = [mark, next(parsed), next(parsed)]
            else:
                value = [mark, next(parsed)]
            output.update({each: value})
        return output
    return neat_format(walk(diff))


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
