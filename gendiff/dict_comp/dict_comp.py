#!/usr/bin/env python3
import sys


def generate_diff(dict1, dict2):
    keys_agregated = sorted(set.union(set(dict1), set(dict2)))
    diff_list = []
    diff_list.append('{\n')

    str_templ = '  {} {}: {}\n'
    for key_ in keys_agregated:
        if key_ in dict1 and key_ in dict2:
            if dict1[key_] == dict2[key_]:
                diff_list.append(str_templ.format(' ', key_, dict1[key_]))
            else:
                diff_list.append(str_templ.format('-', key_, dict1[key_]))
                diff_list.append(str_templ.format('+', key_, dict2[key_]))
        else:
            if key_ in dict1 and key_ not in dict2:
                diff_list.append(str_templ.format('-', key_, dict1[key_]))

            if key_ not in dict1 and key_ in dict2:
                diff_list.append(str_templ.format('+', key_, dict2[key_]))

    diff_list.append('}')
    return ''.join(diff_list)


# __file__.split(os.path.sep)[-1]
def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
