#!/usr/bin/nv python3


def printme(str):
    """This prints a passed string into this functions."""
    print(str)
    return


printme('This is first call to the user defined function')
printme('Again second call to the same function.')
print(printme.__doc__)