#!/usr/bin/env python3
from gendiff.modules.generate_diff import generate_diff
import json
import sys
import pathlib
import pytest


def test_generate_diff  ():
    list_files = ['file1.json', 'file2.json']

    list_json = []

    diff_to_get = {
    'common': {
        'follow': {'diff+': False},
        'setting1': 'Value 1',
        'setting2': {'diff-': 200},
        'setting3': {'diff-': True, 'diff+': None},
        'setting4': {'diff+': 'blah blah'},
        'setting5': {'diff+': {'key5': 'value5'}},
        'setting6': {'doge': {'wow': {'diff-': '',
                     'diff+': 'so much'}}, 'key': 'value',
                     'ops': {'diff+': 'vops'}},
        },
    'group1': {'baz': {'diff-': 'bas', 'diff+': 'bars'}, 'foo': 'bar',
               'nest': {'diff-': {'key': 'value'}, 'diff+': 'str'}},
    'group2': {'diff-': {'abc': 12345, 'deep': {'id': 45}}},
    'group3': {'diff+': {'deep': {'id': {'number': 45}},
               'fee': 100500}},
    }

    #print('CWD:', pathlib.Path().resolve())+
    #print(list_files)

    for file in list_files:
        try:
            fobj = open(file)
        except OSError:
            print ("Could not read file", file)
            sys.exit(1)
        with fobj:
            list_json.append(json.load(fobj))

    diff = generate_diff(list_json[0], list_json[1])

    assert dict(diff) == diff_to_get