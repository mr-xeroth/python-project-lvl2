#!/usr/bin/env python3
from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.plain import plain

import json
import sys
import pathlib
import pytest


def test_plain():
    list_files = ['file1.json', 'file2.json']

    list_json = []

    string_to_get = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
"""

    #print('CWD:', pathlib.Path().resolve())
    #print(list_files)

    for file in list_files:
        try:
            fobj = open(file)
        except OSError:
            print ("Could not read file", file)
            sys.exit(1)
        with fobj:
            list_json.append(json.load(fobj))

    #print('data:', list_json)

    diff = generate_diff(list_json[0], list_json[1])
    output = plain(diff)
    #print(output)
    assert output == string_to_get