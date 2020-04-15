# Sets

# setvazio

vazio = set()
print(type(vazio))

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Chemistry', 'Art', 'Math'}
print('Math' in cs_courses)
print('Python' not in cs_courses)
print(cs_courses)

#adicionando elementos
cs_courses.add('Big Data Analytics')
print(f'Adicionando Big Data: {cs_courses}')
cs_courses.add('Data Science')
print(f'Data Science: {cs_courses}')
print()

cs_courses.pop()
print(f'Removendo com pop(): {cs_courses}')
print()

cs_courses.remove('Data Science')
print(f'Removendo com remove(): {cs_courses}')

# cs_courses.clear()
# print(f'Deleta todos os items do conjunto: {cs_courses}')
print()

"""Operacoes de conjunto"""
art_courses = {'History', 'Design', 'Art', 'Math'}

print(f'Interseção: {cs_courses.intersection(art_courses)}')
print(f'Diferença: {cs_courses.difference(art_courses)}')
print(f'União: {cs_courses.union(art_courses)}')