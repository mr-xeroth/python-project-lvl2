#!/usr/bin/env python3
import os
import pytest
import json


from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.stylish import stylish
from gendiff.modules.plain import plain
from gendiff.modules.jsonify import jsonify


def get_file_path(file_name):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data


# list of [json1, json2, diff_raw, diff_stylish, diff_plain, diff_json]
data_plain = read(get_file_path('json_plain.txt')).split('\n\n\n')
data_nested = read(get_file_path('json_nested.txt')).split('\n\n\n')


@pytest.fixture
def diff_plain():
    json1 = json.loads(data_plain[0])
    json2 = json.loads(data_plain[1])
    return generate_diff(json1, json2)


@pytest.fixture
def dataset_plain():
    return {
                'formatter': [
                    stylish,
                    plain,
                    jsonify
                ],
                'result': [
                    data_plain[3],
                    data_plain[4],
                    data_plain[5]
                ]
            }


@pytest.fixture
def diff_nested():
    json1 = json.loads(data_nested[0])
    json2 = json.loads(data_nested[1])
    return generate_diff(json1, json2)


@pytest.fixture
def dataset_nested():
    return {
                'formatter': [
                    stylish,
                    plain,
                    jsonify
                ],
                'result': [
                    data_nested[3],
                    data_nested[4],
                    data_nested[5]
                ]
            }


def test_diff_plain(diff_plain):
    exemplar = eval(data_plain[2])
    assert diff_plain == exemplar


@pytest.mark.parametrize("try_index", range(3))
def test_plain(diff_plain, dataset_plain, try_index):
    d = dataset_plain
    exemplar = d['result'][try_index]
    assert d['formatter'][try_index](diff_plain) == exemplar


def test_diff_nested(diff_nested):
    exemplar = eval(data_nested[2])
    assert diff_nested == exemplar


@pytest.mark.parametrize("try_index", range(3))
def test_nested(diff_nested, dataset_nested, try_index):
    d = dataset_nested
    exemplar = d['result'][try_index]
    assert d['formatter'][try_index](diff_nested) == exemplar
