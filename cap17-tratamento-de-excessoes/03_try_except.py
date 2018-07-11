#!/usr/bin/env python3

try:
    fh = open('testfile', 'r')
    fh.write("This is my test file fo r exception handling!!")
except IOError:
    print("Error: Can't find file or read data.")
else:
    print("Written content in the file successfuly.")
    fh.close()
