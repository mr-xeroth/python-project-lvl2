import pytest
import sys
import os

from gendiff.scripts.gendiff import main

FIXTURES = 'fixtures'

text_help_file = 'argparse_help.txt'


def get_file_by_path(file, folder):
    cwd = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cwd, folder, file)


@pytest.fixture
def expected_help():
    with open(get_file_by_path(text_help_file, FIXTURES), 'r') as f:
        expected = f.read()
    return expected


@pytest.mark.parametrize('option', ('-h',))
def test_gendiff_help(option, expected_help):
    assert main([option]) == expected_help