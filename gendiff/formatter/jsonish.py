#!/usr/bin/env python3
import sys
import json


def jsonish(diff):
    return json.dumps(diff, indent=2, sort_keys=True)


def main():
    print(sys.modules[__name__])


if __name__ == '__main__':
    main()
