import string

# string module constants
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.whitespace)
print(string.punctuation)

print()
my_string = 'Floripa Code Gurus, escola de tecnologia, cursos de Python e Django'
print(string.capwords(my_string))