#!/ur/bin/env python3

total = 0  # variavel gobal


def sum(arg1, arg2):
    total = arg1 + arg2  # agora total eh uma variavel local
    print("Inside the function local total: ", total)
    return 

# Chamando a funcao
sum(10, 20)
print()
print("Outside the function global total: ", total)