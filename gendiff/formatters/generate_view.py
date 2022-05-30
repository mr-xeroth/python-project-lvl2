"""To run selected diff formatter with raw diff"""

from gendiff.modules.view_formats import VIEW_FORMATS
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


FORMATTER_TABLE = dict(zip(VIEW_FORMATS, (stylish, plain, json)))


def generate_view(diff_dict: dict, view_format: str) -> str:
    '''Takes in diff dict, view format, return formatted view'''

    if view_format in FORMATTER_TABLE:
        return FORMATTER_TABLE[view_format](diff_dict)
