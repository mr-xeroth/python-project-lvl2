#!/usr/bin/env python3
import sys


def parse_diff(diff):
    diffs = "diff-", "diff+"
    values = []
    for x in diffs:
        try:
            value = diff[x]
        except KeyError:
            values.append(None)
        else:
            # insulate bool values
            values.append({'val': value})
    return values


def get_diff(key_, diff):
    values = parse_diff(diff)
    if values[0] and values[1]:
        new_key = key_ + '__updated'
        value = {'old': values[0]['val'], 'new': values[1]['val']}
        return new_key, value
    elif values[0]:
        new_key = key_ + '__removed'
        value = values[0]['val']
        return new_key, value
    elif values[1]:
        new_key = key_ + '__added'
        value = values[1]['val']
        return new_key, value
    return None, None


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
    return walk(diff)


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()