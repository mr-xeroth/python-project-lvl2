"""To run selected diff formatter with raw diff"""

from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def generate_view(diff_dict: dict, view_format: str) -> str:
    '''Takes in diff dict, view format, return formatted view'''

    view_index = {'stylish': stylish, 'plain': plain, 'json': json}
    if view_format in view_index:
        return view_index[view_format](diff_dict)
