import pytest
import os

from gendiff.formatters.view_formats import VIEW_FORMATS, VIEW_DEFAULT
from gendiff.scripts.gendiff import main

SOURCE_FORMATS = ("json", "yaml")

FIXTURES = 'fixtures'

FILE1 = 'file1'

FILE2 = 'file2'

VIEW = 'view'


def get_file_by_path(file, folder):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, folder, file)


@pytest.fixture
def file1(request):
    type_ = request.param
    return get_file_by_path(f'{FILE1}.{type_}', FIXTURES)


@pytest.fixture
def file2(request):
    type_ = request.param
    return get_file_by_path(f'{FILE2}.{type_}', FIXTURES)


@pytest.fixture
def expected_view(request):
    view_format = request.getfixturevalue('view_format')
    with open(get_file_by_path(
            f'{VIEW}_{view_format}.txt', FIXTURES), 'r') as f:
        expected = f.read()
    return expected


@pytest.mark.parametrize("view_format", VIEW_FORMATS)
@pytest.mark.parametrize("file1", SOURCE_FORMATS, indirect=True)
@pytest.mark.parametrize("file2", SOURCE_FORMATS, indirect=True)
def test_gendiff(capsys, file1, file2, view_format, expected_view):

    try:
        main([f'-f{view_format}', file1, file2])
    except SystemExit:
        pass

    captured = capsys.readouterr()

    assert captured.out == expected_view


@pytest.mark.parametrize("view_format", (VIEW_DEFAULT,))
@pytest.mark.parametrize("file1", ['json'], indirect=True)
@pytest.mark.parametrize("file2", ['json'], indirect=True)
def test_gendiff_default_format(
        capsys, file1, file2, view_format, expected_view):

    try:
        main([file1, file2])
    except SystemExit:
        pass

    captured = capsys.readouterr()

    assert captured.out == expected_view
