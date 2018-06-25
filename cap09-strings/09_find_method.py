#!/usr/bin/python3

"""Description
The find() method determines if the string str occurs in string, or in a substring of string
if the starting index beg and ending index end are given.

Syntax
str.find(str, beg=0 end=len(string))
"""

str1 = "this is string example....wow!!!"
str2 = "exam";
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))