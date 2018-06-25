#!/usr/bin/python3
str1 = "this is really a string example....wow!!!"
str2 = "is"
print (str1.rindex(str2))
print (str1.rindex(str2,10)) #ERRO: ValueError: substring not found

"""The rindex() method returns the last index where the substring str is found, or raises an 
exception if no such index exists, optionally restricting the search to string[beg:end].
"""