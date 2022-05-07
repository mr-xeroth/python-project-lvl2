#!/usr/bin/env python3
import pytest
import os

from gendiff.core import generate_diff


plain_json_file = ("plain1.json", "plain2.json")

plain_yaml_file = ("plain1.yaml", "plain2.yaml")

plain_view_file = ("plain_stylish.txt", "plain_plain.txt", "plain_json.txt")

nested_json_file = ("nested1.json", "nested2.json")

nested_yaml_file = ("nested1.yaml", "nested2.yaml")

nested_view_file = ("nested_stylish.txt", "nested_plain.txt",
                    "nested_json.txt")

tags = ("stylish", "plain", "json")

variants = (
    (0, tags[0]),
    (1, tags[1]),
    (2, tags[2])
)


def get_file_path(file_name):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, 'fixtures', file_name)


def batch_file_rename(files):
    text = []
    for name in files:
        text.append(get_file_path(name))
    return text


def batch_read(files):
    text = []
    for name in files:
        with open(get_file_path(name), 'r') as f:
            text.append(f.read())
    return text


#
#   PLAIN VIEW
#
@pytest.fixture
def plain_view():
    return batch_read(plain_view_file)


#
#   PLAIN JSON
#
@pytest.fixture
def plain_json():
    return batch_file_rename(plain_json_file)


#
#   PLAIN YAML
#
@pytest.fixture
def plain_yaml():
    return batch_file_rename(plain_yaml_file)


#
#   NESTED VIEW
#
@pytest.fixture
def nested_view():
    return batch_read(nested_view_file)


#
#   NESTED JSON
#
@pytest.fixture
def nested_json():
    return batch_file_rename(nested_json_file)


#
#   NESTED YAML
#
@pytest.fixture
def nested_yaml():
    return batch_file_rename(nested_yaml_file)


#
#   TEST PLAIN JSON
#
@pytest.mark.parametrize("index,style", variants)
def test_plain_json(index, style, plain_view, plain_json):
    exemplar = plain_view[index]
    json1, json2 = plain_json
    print ('file1:', json1, '\nfile2:', json2)
    assert generate_diff(json1, json2, style) == exemplar


#
#   TEST PLAIN YAML
#
@pytest.mark.parametrize("index,style", variants)
def test_plain_yaml(index, style, plain_view, plain_yaml):
    exemplar = plain_view[index]
    yaml1, yaml2 = plain_yaml
    assert generate_diff(yaml1, yaml2, style) == exemplar


#
#   TEST NESTED JSON
#
@pytest.mark.parametrize("index,style", variants)
def test_nested_json(index, style, nested_view, nested_json):
    exemplar = nested_view[index]
    json1, json2 = nested_json
    assert generate_diff(json1, json2, style) == exemplar


#
#   TEST NESTED YAML
#
@pytest.mark.parametrize("index,style", variants)
def test_nested_yaml(index, style, nested_view, nested_yaml):
    exemplar = nested_view[index]
    yaml1, yaml2 = nested_yaml
    assert generate_diff(yaml1, yaml2, style) == exemplar
