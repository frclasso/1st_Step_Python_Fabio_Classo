#!/usr/bin/env python3

import os, sys

# Assumindo que temos permissoes de leitura e escrita sobre o arquivo foo.txt

ret = os.access('foo.txt', os.F_OK)
print("F_Ok - return value {}".format(ret))

ret = os.access('foo.txt', os.R_OK)
print("R_Ok - return value {}".format(ret))

ret = os.access('foo.txt', os.W_OK)
print("W_Ok - return value {}".format(ret))

ret = os.access('foo.txt', os.X_OK)
print("X_Ok - return value {}".format(ret))
