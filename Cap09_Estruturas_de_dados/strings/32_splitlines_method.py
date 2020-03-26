#!/usr/bin/python3


"""The splitlines() method returns a list with all the lines in string, optionally including the 
line breaks (if num is supplied and is true).
"""

str = "this is \nstring example....\nwow!!!"
print (str.splitlines( ))
print()

"""Escape Sequence	Character
\n	Newline
\r	Carriage Return
\r\n	Carriage Return + Line Feed
\v or \x0b	Line Tabulation
\f or \x0c	Form Feed
\x1c	File Separator
\x1d	Group Separator
\x1e	Record Separator
\x85	Next Line (C1 Control Code)
\u2028	Unicode Line Separator
\u2029	Unicode Paragraph Separator"""

print('foo\f\f\fbar'.splitlines())
print('foo\f\f\fbar'.splitlines(True))
print('foo\nbar\nqux'.splitlines(True))
print('foo\nbar\nqux'.splitlines(1))
