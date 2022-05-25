from gendiff.formatter.stringify import stringify


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


# replace dict type for a "here lies dict"
def filter_value(value):

    if isinstance(value, dict):
        return '[complex value]'
    else:
        return stringify(value)


def plain_report(node, node_name):
    closing = None

    if node['type'] == 'updated':
        values = (filter_value(node['value']['old']),
                  filter_value(node['value']['new']))
        closing = f" updated. From {values[0]} to {values[1]}\n"

    elif node['type'] == 'removed':
        closing = " removed\n"

    elif node['type'] == 'added':
        closing = f" added with value: {filter_value(node['value'])}\n"

    if closing:
        return f"Property '{node_name}' was" + closing


def plain(diff):
    def walk(diff, path):
        output = ''
        for key, node in diff.items():
            node_name = path + f'.{key}' if path else str(key)

            if node['type'] == 'nested':
                output += walk(node['value'], node_name)
            elif report := plain_report(node, node_name):
                output += report
        return output
    return walk(diff, '').rstrip('\n')
