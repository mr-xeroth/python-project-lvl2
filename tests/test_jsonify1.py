#!/usr/bin/env python3
from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.jsonify import jsonify

import json
import sys
import pathlib
import pytest


def test_jsonify1():
    list_files = ['file1.json', 'file2.json']

    list_json = []

    string_to_get = """{
  "common": {
    "follow__added": false,
    "setting2__removed": 200,
    "setting3__updated": {
      "new": null,
      "old": true
    },
    "setting4__added": "blah blah",
    "setting5__added": {
      "key5": "value5"
    },
    "setting6": {
      "doge": {
        "wow__updated": {
          "new": "so much",
          "old": ""
        }
      },
      "ops__added": "vops"
    }
  },
  "group1": {
    "baz__updated": {
      "new": "bars",
      "old": "bas"
    },
    "nest__updated": {
      "new": "str",
      "old": {
        "key": "value"
      }
    }
  },
  "group2__removed": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  },
  "group3__added": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
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
    output = json.dumps(jsonify(diff), indent=2, sort_keys=True)
    assert output == string_to_get