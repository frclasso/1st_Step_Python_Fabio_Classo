#!/usr/bin/env python3

try:
    fh = open('testfile', 'w')
    try:
        fh.write("This is my NEW test file fo r exception handling!!")
    finally:
        print("Going to close the file.")
        fh.close()
except IOError:
    print("Error:  can't find file or read data.")