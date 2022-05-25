import json


def jsonish(diff):
    return json.dumps(diff, indent=2, sort_keys=True)
