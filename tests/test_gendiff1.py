from gendiff.scripts.gendiff import generate_diff
import json
import sys
import pathlib
import pytest


def test_generate_diff():
    list_files = ['file1.json', 'file2.json']

    list_json = []

    diff_to_get = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
    timeout: 50
  + verbose: True
}"""

    print('CWD:', pathlib.Path().resolve())
    print(list_files)

    for file in list_files:
        try:
            fobj = open(file)
        except OSError:
            print ("Could not read file", file)
            sys.exit(1)
        with fobj:
            list_json.append(json.load(fobj))

    print('data:', list_json)

    diff = generate_diff(list_json[0], list_json[1])
    print(diff)
    assert diff == diff_to_get