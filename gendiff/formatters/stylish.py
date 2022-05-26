""" stylish JSON diff formatter. """
from json import dumps

TAB_SIZE = 4
TAB_FILL = ' '

TEMPLATE = '{}{} {}: {}'


def nested_indent(depth):
    return TAB_FILL * (TAB_SIZE * depth - 2)


def bracket_indent(depth):
    return TAB_FILL * TAB_SIZE * (depth - 1)


# it might be a simple value or nested dict
def parse_any_value(value, depth):
    if isinstance(value, dict):
        return stylish(value, depth)
    else:
        return dumps(value)


def make_nested_value(tab, mark, key, value):
    return TEMPLATE.format(tab, mark, key, value)


def stylish(data, depth=1):

    output = []

    output.append('{')

    for key, node in data.items():

        if node['type'] == 'updated':
            output.append(
                make_nested_value(
                    nested_indent(depth),
                    '-',  # node mark
                    key,
                    parse_any_value(node['value']['old'], depth + 1)
                )
            )

            output.append(
                make_nested_value(
                    nested_indent(depth),
                    '+',  # node mark
                    key,
                    parse_any_value(node['value']['new'], depth + 1)
                )
            )

        else:
            if node['type'] == 'removed':
                node_mark = '-'
            elif node['type'] == 'added':
                node_mark = '+'
            elif node['type'] == 'untouched' or node['type'] == 'nested':
                node_mark = TAB_FILL

            output.append(
                make_nested_value(
                    nested_indent(depth),
                    node_mark,
                    key,
                    parse_any_value(node['value'], depth + 1)
                )
            )

    output.append(f'{bracket_indent(depth)}}}')
    return '\n'.join(output)
