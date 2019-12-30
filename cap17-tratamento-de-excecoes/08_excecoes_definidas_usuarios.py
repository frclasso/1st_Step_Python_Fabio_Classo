#!/usr/bin/env python3


class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise NetworkError("Bad Hostname")
except NetworkError as e:
    print(e.args)