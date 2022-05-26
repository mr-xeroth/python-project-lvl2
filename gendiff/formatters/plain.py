"""Plain diff formatter"""

from json import dumps


def filter_value(value: any) -> str:

    if isinstance(value, dict):
        return '[complex value]'
    else:
        return dumps(value)


def plain(diff: dict, path: str = '') -> str:
    '''Takes in diff dict, returns flat changelog'''

    output = []

    for key, node in diff.items():

        node_name = f'{path}.{str(key)}'.lstrip('.')

        opening = f"Property '{node_name}' was"

        closing = None

        if node['type'] == 'updated':
            val1 = filter_value(node['value']['old'])
            val2 = filter_value(node['value']['new'])

            closing = f" updated. From {val1} to {val2}"
            output.append(opening + closing)

        elif node['type'] == 'removed':
            closing = " removed"
            output.append(opening + closing)

        elif node['type'] == 'added':
            closing = f" added with value: {filter_value(node['value'])}"
            output.append(opening + closing)

        elif node['type'] == 'nested':
            output.append(plain(node['value'], node_name))

    return '\n'.join(output)
