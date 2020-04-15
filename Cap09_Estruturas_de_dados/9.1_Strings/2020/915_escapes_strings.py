#!/usr/bin/python3

# 9.1.5 Caracteres Escape
# "He said, "What's there?"

# 1
#print("He said, "What's there?" ")

# 2
# print('He said, "What's there?" ')

# 3
print('He said, "What\'s there?" ')

# 4
print("He said, What's there?")

# 5
print('''He said, "What's there?"''')

#6
print(""" He said, "What's there?" """)
print()

# Caso 02
print("C:\\Python32\\Lib")  # o carctere \ aparece uma vez
print()

# Caso 03
print("This is printed\nin two lines")  # quebra de linha \n
print()

# Caso 04
print("This is \x48\x45\x58 representation")
print()

para_str = """              This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t\t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also \n\t\t\t\t\t\t\t\t\t\t\t\t\tshow up.
"""
print (para_str)