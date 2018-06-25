#!/usr/bin/python3
str = "this is string example....wow!!!"
print (str.startswith( 'this' ))
print (str.startswith( 'string', 8 ))
print (str.startswith( 'this', 2, 4 ))

"""The startswith() method checks whether the string starts with str, optionally restricting 
the matching with the given indices start and end.

Following is the syntax for startswith() method-
str.startswith(str, beg=0,end=len(string));

Parameters
str - This is the string to be checked.
beg - This is the optional parameter to set start index of the matching boundary.
end - This is the optional parameter to set start index of the matching boundary.


"""