

numeros = {1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,0,0}
print(numeros)
print(type(numeros))
numeros.add(500)
print(numeros)
frozen_numeros = frozenset(numeros)
print(frozen_numeros)
print(type(frozen_numeros))
# frozen_numeros.add(600)

nuns = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,0,0]
colecao = tuple(set(nuns))
print(colecao)
print(type(colecao))