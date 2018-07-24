#!/usr/bin/python3

"""The rstrip() method returns a copy of the string in which """

str = " this is string example....wow!!! "
print(str.rstrip())
str = "*****this is string example....wow!!!*****"
print()

print('    foo bar baz   '.rstrip())
print('foo\t\nbar\t\nbaz\t\n'.rstrip())
print('foo.$$$;'.rstrip(';$.'))  # Opcionalmente podemos passar
                                 # os caracteres a serem removidos
