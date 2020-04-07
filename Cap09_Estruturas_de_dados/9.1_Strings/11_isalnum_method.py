#!/usr/bin/python3

"""The isalnum() method checks whether the string consists of alphanumeric characters."""

str = "this2016" # No space in this string
print(str.isalnum())
str = "this is string example....wow!!!"
print(str.isalnum())
print()


print('abcdef'.isalnum())
print('abcdef$1234'.isalnum())
print('abcdef1234'.isalnum())
print(''.isalnum())


