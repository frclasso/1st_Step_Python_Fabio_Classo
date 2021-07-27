#set

#items exclusivos
# s = {1,2,3}

d_vazio = {} # dicionario
s_vazio = set()
print(type(d_vazio))
print(type(s_vazio))

numeros = {1,2,3,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9}
print(type(numeros))
print(numeros)

user_ids ={1234, 1235, 1236, 1234}
user_ids.add(1236)
user_ids.add(1236)
user_ids.add(1236)
user_ids.add(1236)
user_ids.add(1236)
user_ids.pop()
print(user_ids)

user_ids =[1234, 1235, 1236, 1234]
user_ids.append(1234)
user_ids.append(1234)
user_ids.append(1234)
user_ids.append(1234)
print(user_ids)

num_1 = {1,2,3,4,5}
num_2 = {10,20,30,40,50, 5}

print(num_1.union(num_2))
print(num_1 | num_2)# uniao

print(num_1 & num_2) #intersecao
print(num_1.intersection(num_2))

print(num_1.difference(num_2))
print(num_1 - num_2) # diferenca

s = list(num_1)
print(s[0])