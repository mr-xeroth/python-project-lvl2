#!/usr/bin/env python3
from gendiff.dict_comp.dict_comp import generate_diff
import argparse
import yaml
import json


import sys

file_diff = 'diff.txt'

# def generate_diff(dict1, dict2):
#     keys_agregated = sorted(set.union(set(dict1), set(dict2)))
#     # print(dict_agregated)
#     diff_list = []
#     diff_list.append('{\n')
#     char_diff = ''

#     for key_ in keys_agregated:
#         if key_ in dict1 and key_ not in dict2:
#             char_diff = '-'
#             dict_value = dict1[key_]
#         if key_ not in dict1 and key_ in dict2:
#             char_diff = '+'
#             dict_value = dict2[key_]
#         if key_ in dict1 and key_ in dict2:
#             char_diff = ' '
#             dict_value = dict1[key_]
#         diff_list.append(f'  {char_diff} {key_}: {dict_value}\n')
#     diff_list.append('}')
#     return ''.join(diff_list)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=argparse.FileType('r'))
    parser.add_argument('second_file', type=argparse.FileType('r'))
    parser.add_argument('-f', '--format', type=str, metavar='FORMAT',
                        help='set format of output')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        args = parser.parse_args()
        # print('ARG:', args.first_file.name, args.second_file.name)

        list_files = [args.first_file.name, args.second_file.name]

        list_dicts = []

        for file_name in list_files:
            fobj = open(file_name)
            with fobj:
                if file_name.endswith('.yaml') or file_name.endswith('.yml'):
                    data = yaml.load(fobj, Loader=yaml.FullLoader)
                    print('YD', data)
                    list_dicts.append(data)
                elif file_name.endswith('.json'):
                    list_dicts.append(json.load(fobj))
                else:
                    print("No file with proper '.yaml' or '.json' name")
                    sys.exit(1)

        diff = generate_diff(list_dicts[0], list_dicts[1])
        print(diff)

        with open(file_diff, 'w', encoding='utf-8') as f:
            f.write(diff)
        print(f'Written to {file_diff}')


if __name__ == '__main__':
    main()
