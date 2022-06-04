"""To run diff generator and return diff in chosen format"""

import json
import yaml

from gendiff.formatters.view_formats import VIEW_DEFAULT
from gendiff.modules.dict_compare import dict_compare
from gendiff.formatters.generate_view import generate_view


def file_read(file_name: str) -> str:
    data = None
    with open(file_name, 'r') as f:
        data = f.read()
    return data


def get_file_format(file_name: str) -> str:
    format_ = None
    if file_name.endswith('.yaml') or file_name.endswith('.yml'):
        format_ = 'yaml'
    elif file_name.endswith('.json'):
        format_ = 'json'
    return format_


def convert_to_dict(data: str, type_: str) -> dict:
    result = None
    if type_ == "yaml":
        result = yaml.load(data, Loader=yaml.SafeLoader)
    if type_ == "json":
        result = json.loads(data)
    return result


def generate_diff(
    file1: str, file2: str,
        view_format: str = VIEW_DEFAULT) -> str:
    '''Takes in two JSON file names, diff format.
Returns the diff view of the two'''

    data1, type1 = file_read(file1), get_file_format(file1)
    data2, type2 = file_read(file2), get_file_format(file2)

    dict1 = convert_to_dict(data1, type1)
    dict2 = convert_to_dict(data2, type2)

    return generate_view(dict_compare(dict1, dict2), view_format)
