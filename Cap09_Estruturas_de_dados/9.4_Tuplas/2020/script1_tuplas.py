

# tuplas

#tupla vazia

tupla_vazia = ()
print(f'Tipo: {type(tupla_vazia)}')
print()

# tupla com um elemento
tupla_com_um_elemento  = (50, )
print(f'Tipo: {type(tupla_com_um_elemento)}')
print()

#ou
tupla_com_um_elemento_sem_parenteses = 50,
print(f'Tipo: {type(tupla_com_um_elemento_sem_parenteses)}')
print()

#Acesando valores
cursos_1 = ('Matematica', 'Economia', 'Estatística')
print(f'Retorna o valor relacionado ao indice 0 na tupla cursos_1: {cursos_1[0]}')
print()


#Indexando
print(f"Retorna o índice de Economia na tupla: {cursos_1.index('Economia')}")

# Concatenaçao
cursos_2 = ('Quimica', 'Fisica', 'Biologia')
print(f'Tuplas concatenadas: {cursos_1 + cursos_2}')
all_courses = cursos_1 + cursos_2
print()

# repeticao
print(f'Repeticao: {cursos_2 * 5}')

# slicing
print(f'Slicing: {all_courses[1:]}')
print()

#Invertendo a ordem
print(f'Tupla invertida: {all_courses[::-1]}')
print()

# Ordenando
print(sorted(all_courses))
print(f'Ordenando: {tuple(sorted(all_courses))}')



# Operacoes basicas
# len, max, min, in, not in
print(f'Quantida de elementos da tuplas: {len(cursos_1)}')

nums = (100,30,4,25)
print(f'Maior valor em nums: {max(nums)}')
print(f'Menor valor em nums: {min(nums)}')
print()

print(f"Verifica se Python esta em cursos_2: {'Python' in cursos_2}")
print(f"Verifica se Python NAO esta em cursos_2: {'Python' not in cursos_2}")
print()

# loops em tuplas
print('Usando o laço for')
for num, curso in enumerate(all_courses):
    print(num, '==>',curso)

print()

print("Usando o laço while")
count = 0
while count < len(all_courses):
    print(count + 1, "==>", all_courses[count])
    count +=1
print()

# a classe tuple()

# convertendo umas lista em tupla
lista_de_cursos = list(all_courses)
print(type(lista_de_cursos))
all_courses_t = tuple(lista_de_cursos)
print(f'Tipo: {type(all_courses_t)}')
print()

# convertendo uma string em tupla
python = 'Python'
t1 = tuple(python)
print(t1)


""" Imutabilidade 

    Os métodos que utilizamos em listas, tais como pop, del, append e insert nao funcionam em tuplas
"""

# all_courses[0] = 'Python'
"""TypeError: 'tuple' object does not support item assignment"""


#all_courses.pop()
"""AttributeError: 'tuple' object has no attribute 'pop'
"""

#all_courses.append('Django')
"""AttributeError: 'tuple' object has no attribute 'append'
"""
print()

