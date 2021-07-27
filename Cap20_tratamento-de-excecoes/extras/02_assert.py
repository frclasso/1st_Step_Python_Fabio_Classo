#!/usr/bin/env python3

import sys


def linux_interaction():
    assert ('linux ' in sys.platform), 'Function can only run on Linux systems. '
    print("Doing something.")


try:
    linux_interaction()

except AssertionError as error:
    print(error)
    print("The linux_interaction() function was not executed.")
else:
    print("Executing else clause.")


"""Rodando em uma maquina windows temos  a seguinte saida:
   Function can only run on Linux systems.
   The linux_interaction() function was not executed.
   
   Rodando em Linux, temos:
   Doing something.
   Executing else clause.
"""
#
# print()
# if sys.platform == "linux":
#     print("--- OS Linux ---")
# else:
#     "Not Linux"