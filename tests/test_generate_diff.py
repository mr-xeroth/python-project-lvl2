#!/usr/bin/env python3
import pytest
import os
import json
import yaml

from gendiff.scripts.gendiff import generate_diff


plain_json_file = ("plain1.json", "plain2.json")

plain_yaml_file = ("plain1.yaml", "plain2.yaml")

plain_view_file = ("plain_stylish.txt", "plain_plain.txt", "plain_json.txt")

nested_json_file = ("nested1.json", "nested2.json")

nested_yaml_file = ("nested1.yaml", "nested2.yaml")

nested_view_file = ("nested_stylish.txt", "nested_plain.txt",\
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


def batch_read(files):
    text = []
    for name in files:
        with open(get_file_path(name), 'r') as f:
            text.append(f.read())
    return text


def batch_load_json(data):
    result = []
    for each in data:
        result.append(json.loads(each))
    return tuple(result)


def batch_load_yaml(data):
    result = []
    for each in data:
        result.append(yaml.load(each, Loader=yaml.SafeLoader))
    return tuple(result)

#
#   PLAIN VIEW
#
@pytest.fixture
def plain_view():
    return batch_read(plain_view_file)

#
#   PLAIN JSON
#
plain_json_text = batch_read(plain_json_file)

@pytest.fixture
def plain_json():
    return batch_load_json(plain_json_text)

#
#   PLAIN YAML
#
plain_yaml_text = batch_read(plain_yaml_file)

@pytest.fixture
def plain_yaml():
    return batch_load_yaml(plain_yaml_text)

#
#   NESTED VIEW
#
@pytest.fixture
def nested_view():
    return batch_read(nested_view_file)

#
#   NESTED JSON
#
nested_json_text = batch_read(nested_json_file)

@pytest.fixture
def nested_json():
    return batch_load_json(nested_json_text)

#
#   NESTED YAML
#
nested_yaml_text = batch_read(nested_yaml_file)

@pytest.fixture
def nested_yaml():
    return batch_load_yaml(nested_yaml_text)

#
#   TEST PLAIN JSON
#
@pytest.mark.parametrize("index,style", variants)
def test_plain_json(index, style, plain_view, plain_json):
    exemplar = plain_view[index]
    json1, json2 = plain_json
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
