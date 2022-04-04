#!/usr/bin/env python3


def generate_diff(dict1, dict2):
    keys_agregated = sorted(set.union(set(dict1), set(dict2)))
    diff_list = []
    diff_list.append('{\n')

    for key_ in keys_agregated:
        if key_ in dict1 and key_ in dict2:
            if dict1[key_] == dict2[key_]:
                diff_list.append(f'    {key_}: {dict1[key_]}\n')
            else:
                diff_list.append(f'  - {key_}: {dict1[key_]}\n')
                diff_list.append(f'  + {key_}: {dict2[key_]}\n')
        else:
            if key_ in dict1 and key_ not in dict2:
                diff_list.append(f'  - {key_}: {dict1[key_]}\n')
            if key_ not in dict1 and key_ in dict2:
                diff_list.append(f'  + {key_}: {dict2[key_]}\n')

    diff_list.append('}')
    return ''.join(diff_list)


def main():
    print('dict_comp.py')


if __name__ == '__main__':
    main()
