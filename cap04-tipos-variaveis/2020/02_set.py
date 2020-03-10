#!/usr/bin/env python3


# Sets

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Chemistry'}
art_courses = {'History', 'Design', 'Art', 'Math'}


# Interseção (tem em ambos)
#print(cs_courses.intersection(art_courses))  # {'Math', 'History'}

# Diferença
#print(cs_courses.difference(art_courses)) #{'CompSci', 'Physics', 'Chemistry'}

# União
#print(cs_courses.union(art_courses))
# print()

x = set('spam')
y = {'h', 'a', 'm'}

#print(x,y)

# print(x & y)  # intersection
# print(x - y) # diference
# print(x | y) # union
# print()

# print(set('spam') - set('ham')) # diferença entre sets
# print(set('spam') == set('asmp')) # Nao importa a ordem


# print('Math' in cs_courses) # True
# print(cs_courses)



# Filtrando duplicatas
# print(list(set([1,2,1,3,1,3,2])))

# sets also supports membership test operation
#print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

'''Criando um set vazio'''
# colecao = set()  # com parenteses
# print(colecao)
# print(type(colecao))