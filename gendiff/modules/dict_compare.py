"""To genearate raw diff data for formatter's processing"""


def dict_compare(dict1: dict, dict2: dict) -> dict:
    '''Takes in two dicts, returns the diff dict of the two'''

    output = {}
    keys_combined = sorted(set.union(set(dict1), set(dict2)))

    for key in keys_combined:
        if key in dict1 and key not in dict2:
            output[key] = {
                'type': 'removed',
                'value': dict1[key]
            }
        elif key not in dict1 and key in dict2:
            output[key] = {
                'type': 'added',
                'value': dict2[key]
            }
        elif all([isinstance(x, dict) for x in (dict1[key], dict2[key])]):
            output[key] = {
                'type': 'nested',
                'value': dict_compare(dict1[key], dict2[key])
            }
        elif dict1[key] == dict2[key]:
            output[key] = {
                'type': 'untouched',
                'value': dict1[key]
            }
        else:
            output[key] = {
                'type': 'updated',
                'value': {
                    'old': dict1[key],
                    'new': dict2[key]
                }
            }
    return output
