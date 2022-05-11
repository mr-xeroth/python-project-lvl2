#!/usr/bin/env python3
import pytest
import os

from gendiff.modules.generate_diff import generate_diff

json_file_names = ("nested1.json", "nested2.json")

yaml_file_names = ("nested1.yaml", "nested2.yaml")

view_file_names = ("nested_stylish.txt", "nested_plain.txt",
                   "nested_json.txt")

views = ("stylish", "plain", "json")

variants = (
    ("json", views[0]),
    ("json", views[1]),
    ("json", views[2]),
    ("yaml", views[0]),
    ("yaml", views[1]),
    ("yaml", views[2])
)


def get_file_path(file, folder):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, folder, file)


def batch_read(files):
    text = []
    for name in files:
        with open(get_file_path(name, 'fixtures'), 'r') as f:
            text.append(f.read())
    return tuple(text)


@pytest.fixture
def expected_views():
    values = batch_read(view_file_names)
    return dict(zip(views, values))


@pytest.fixture
def source_data():
    return {"json": batch_read(json_file_names),
            "yaml": batch_read(yaml_file_names)}


@pytest.mark.parametrize("source_format,view", variants)
def test_generate_diff(source_data, source_format, view, expected_views):

    data1, data2 = source_data[source_format]

    assert generate_diff(data1, data2, view, source_format) == \
        expected_views[view]
