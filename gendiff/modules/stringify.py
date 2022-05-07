#!/usr/bin/env python3
import sys


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


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
