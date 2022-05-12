#!/usr/bin/env python3
import sys

from gendiff.modules.json_parse import json_compare
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify


def generate_diff(data1, type1, data2, type2, view_format="stylish"):
    view_index = {"stylish": stylish, "plain": plain, "json": jsonify}

    if view_format in view_index:
        return view_index[view_format](
            json_compare(data1, type1, data2, type2, view_format)
        )


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
