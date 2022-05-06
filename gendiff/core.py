#!/usr/bin/env python3
import sys

from gendiff.modules.parse import parse
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify


def generate_diff(json1, json2, format="stylish"):
    func_index = {"stylish": stylish, "plain": plain, "json": jsonify}
    if format in func_index:
        return func_index[format](parse(json1, json2))


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
