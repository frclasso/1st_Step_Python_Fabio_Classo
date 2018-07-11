#!/usr/bin/env python3


def functionName(level):
    if level < 1:
        raise Exception(level)
    return level

try:
    l = functionName(-2)
    print("level=", l)
except Exception as e:
    print("Error in level argument:", e.args[0])