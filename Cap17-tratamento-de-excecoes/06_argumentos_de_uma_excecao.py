#!/usr/bin/env python3


def temp_converter(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n", Argument)

temp_converter('xyz')
