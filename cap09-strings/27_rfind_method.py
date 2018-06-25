#!/usr/bin/python3

str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rfind(str2))
print (str1.rfind(str2, 0, 10))
print (str1.rfind(str2, 10, 0))
print (str1.find(str2))
print (str1.find(str2, 0, 10))
print (str1.find(str2, 10, 0))

"""The rfind() method returns the last index where the substring str is found, or -1 if no 
such index exists, optionally restricting the search to string[beg:end].
"""