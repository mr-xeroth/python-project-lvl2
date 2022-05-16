#!/usr/bin/env python3
import sys
import json


def get_diff(key_, diff):
    new_key, value = None, None
    if 'type' in diff and 'value' in diff:
        value = diff['value']
        new_key = key_ + f'__{diff["type"]}'
    return new_key, value


def jsonify(diff):
    def walk(diff):
        output = {}
        keys = [x for x in diff.keys() if isinstance(diff[x], dict)]
        for each in keys:
            key_, value = get_diff(each, diff[each])
            if not key_:
                key_ = each
                value = walk(diff[each])
            output.update({key_: value})
        return output
    return json.dumps(walk(diff), indent=2, sort_keys=True)


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
