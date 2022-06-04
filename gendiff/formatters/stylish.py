"""Stylish diff formatter"""

from json import dumps

TAB_SIZE = 4
TAB_FILL = ' '

TEMPLATE = '{}{} {}: {}'


def nested_indent(depth: int) -> str:
    return TAB_FILL * (TAB_SIZE * depth - 2)


def bracket_indent(depth: int) -> str:
    return TAB_FILL * TAB_SIZE * (depth - 1)


# it might be a simple value or nested dict
def parse_any_value(value: any, depth: int) -> str:
    if isinstance(value, dict):
        return stylish(value, depth)
    else:
        return dumps(value).strip('"')


def stylish(data: dict, depth: int = 1) -> str:  # noqa: C901
    '''Takes in diff dict, returns its nested tree view'''

    if not type(depth) is int or depth not in range(1, 20):
        depth = 1

    output = []

    output.append('{')

    for key, node in data.items():

        if not isinstance(node, dict) or 'type' not in node:
            output.append(
                TEMPLATE.format(
                    nested_indent(depth),
                    TAB_FILL,
                    key,
                    parse_any_value(node, depth + 1)
                )
            )
            continue

        if node['type'] == 'updated':
            output.append(
                TEMPLATE.format(
                    nested_indent(depth),
                    '-',  # node mark
                    key,
                    parse_any_value(node['value']['old'], depth + 1)
                )
            )

            output.append(
                TEMPLATE.format(
                    nested_indent(depth),
                    '+',  # node mark
                    key,
                    parse_any_value(node['value']['new'], depth + 1)
                )
            )
            continue

        if node['type'] == 'removed':
            node_mark = '-'
        elif node['type'] == 'added':
            node_mark = '+'
        elif node['type'] == 'untouched' or node['type'] == 'nested':
            node_mark = TAB_FILL

        output.append(
            TEMPLATE.format(
                nested_indent(depth),
                node_mark,
                key,
                parse_any_value(node['value'], depth + 1)
            )
        )

    output.append(f'{bracket_indent(depth)}}}')
    return '\n'.join(output)
