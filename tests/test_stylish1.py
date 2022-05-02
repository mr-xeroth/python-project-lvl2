#!/usr/bin/env python3
from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.stylish import stylish

import json
import sys
import pathlib
import pytest


def test_stylish1():
    list_files = ['file1.json', 'file2.json']

    list_json = []

    string_to_get = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:  
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

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
    output = stylish(diff)
    assert output == string_to_get