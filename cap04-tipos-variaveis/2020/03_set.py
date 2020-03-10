
# set, definido por conjunto de valores entre chaves

a = {5,5,1,3,2,7,3,2,4,5,6,8,9,6,5,4}
#print(a)

# set vazio
b = set()

c = {3,4,5,6, 10}
d = {4,5,6,7,8,9}

print(c | d) # uniao
print(c - d) # difereca
print(c & d) # intersecao
print(c ^ d) # XOR
print()
print(c.union(d))
print(c.difference(d))
print(c.intersection(d))
print(c.__ixor__(d))
print()
# membros
basket = {'orange', 'apple', 'lemon', 'pear'}
print('apple' in basket)
print('melon' in basket)
print('melon' not in basket)

