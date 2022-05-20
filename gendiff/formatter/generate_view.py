#!/usr/bin/env python3
import sys

from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.jsonish import jsonish


def generate_view(diff_dict, view_format):
    view_index = {'stylish': stylish, 'plain': plain, 'json': jsonish}
    if view_format in view_index:
        return view_index[view_format](diff_dict)


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
