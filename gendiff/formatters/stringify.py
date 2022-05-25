def stringify(value):
    translate = {True: 'true', False: 'false', None: 'null'}
    if type(value) is int:
        return str(value)
    else:
        new = translate.get(value)
        if new:
            return new
        else:
            return value
