#!/usr/bin/env python3
import pytest
import os

from gendiff.modules.generate_diff import generate_diff

FIXTURES = 'fixtures'

json_file_names = ("nested1.json", "nested2.json")

yaml_file_names = ("nested1.yaml", "nested2.yaml")

view_file_names = ("nested_stylish.txt", "nested_plain.txt",
                   "nested_json.txt")

views = ("stylish", "plain", "json")

types = ("json1", "json2", "yaml1", "yaml2")

variants = (
    (types[0], types[1], views[0]),
    (types[0], types[1], views[1]),
    (types[0], types[1], views[2]),
    (types[2], types[3], views[0]),
    (types[2], types[3], views[1]),
    (types[2], types[3], views[2]),
    (types[0], types[3], views[0]),
    (types[2], types[1], views[0])
)


def get_file_path(file, folder):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, folder, file)


def batch_read(files):
    text = []
    for name in files:
        with open(get_file_path(name, FIXTURES), 'r') as f:
            text.append(f.read())
    return tuple(text)


@pytest.fixture
def expected_views():
    values = batch_read(view_file_names)
    return dict(zip(views, values))


@pytest.fixture
def source_files():
    values = (get_file_path(n, FIXTURES) for n in
              (json_file_names + yaml_file_names))
    return dict(zip(types, values))


@pytest.mark.parametrize("type1,type2,view", variants)
def test_generate_diff(source_files, type1, type2, expected_views, view):

    file1, file2 = source_files[type1], source_files[type2]
    assert generate_diff(file1, file2, view) == expected_views[view]
