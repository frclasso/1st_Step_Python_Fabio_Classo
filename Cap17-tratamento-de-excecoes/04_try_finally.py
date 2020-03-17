#!/usr/bin/env python3

try:
    fh = open('testfile', 'w')
    fh.write("This is my test file fo r exception handling!!")
finally:
    print("Error: Can't find file or read data.")
    fh.close()
