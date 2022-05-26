"""JSON diff formatter"""

from json import dumps


def json(diff: dict) -> str:
    '''Takes in diff dict, returns JSON string'''

    return dumps(diff, indent=2, sort_keys=True)
