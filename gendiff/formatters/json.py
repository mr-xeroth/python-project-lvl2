""" json diff formatter. """
from json import dumps


def json(diff):
    return dumps(diff, indent=2, sort_keys=True)
