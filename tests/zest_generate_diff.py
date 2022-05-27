import pytest
import os

from gendiff.modules.generate_diff import generate_diff

FIXTURES = 'fixtures'

source_formats = ("json", "yaml")

view_formats = ("stylish", "plain", "json")


def get_file_by_path(file, folder):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, folder, file)


@pytest.fixture
def file1(request):
    type_ = request.param
    return get_file_by_path(f'file1.{type_}', FIXTURES)


@pytest.fixture
def file2(request):
    type_ = request.param
    return get_file_by_path(f'file2.{type_}', FIXTURES)


@pytest.fixture
def expected_view(request):
    view_format = request.getfixturevalue('view_format')
    with open(get_file_by_path(f'view_{view_format}.txt', FIXTURES), 'r') as f:
        expected = f.read()
    return expected


@pytest.mark.parametrize("view_format", view_formats)
@pytest.mark.parametrize("file1", source_formats, indirect=True)
@pytest.mark.parametrize("file2", source_formats, indirect=True)
def test_generate_diff(file1, file2, view_format, expected_view):
    assert generate_diff(file1, file2, view_format) == expected_view
