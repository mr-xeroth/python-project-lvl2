import argparse
import json
import sys

file_diff = 'diff.txt'


def generate_diff(dict1, dict2):
    keys_agregated = sorted(set.union(set(dict1), set(dict2)))
    # print(dict_agregated)
    diff_list = []
    diff_list.append('{\n')
    char_diff = ''

    for key_ in keys_agregated:
        if key_ in dict1 and key_ not in dict2:
            char_diff = '-'
            dict_value = dict1[key_]
        if key_ not in dict1 and key_ in dict2:
            char_diff = '+'
            dict_value = dict2[key_]
        if key_ in dict1 and key_ in dict2:
            char_diff = ' '
            dict_value = dict1[key_]
        diff_list.append(f'  {char_diff} {key_}: {dict_value}\n')
    diff_list.append('}')
    return ''.join(diff_list)


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

        list_json = []

        for file_name in list_files:
            fobj = open(file_name)
            with fobj:
                list_json.append(json.load(fobj))

        diff = generate_diff(list_json[0], list_json[1])
        print(diff)

        with open(file_diff, 'w', encoding='utf-8') as f:
            f.write(diff)
        print(f'Written to {file_diff}')


if __name__ == '__main__':
    main()
