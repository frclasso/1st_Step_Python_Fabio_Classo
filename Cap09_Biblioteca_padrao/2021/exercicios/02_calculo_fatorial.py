"""Fatorial é um número natural inteiro positivo, o qual é 
representado por n! O fatorial de um número é calculado pela
multiplicação desse número por todos os seus antecessores até 
chegar ao número 1."""

# Modo tradicional


def factorialTrad(n):
     if n == 0:
         return 1
     else:
         return n * factorialTrad(n-1) # recursivo
         #return (n-2)*(n-1)*(n) # nao recursivo


print(f"fatorialTrad: {factorialTrad(4)}")

# Utilizando a função math.factorial()
print(f"Fatorial utilizando math.factorial(): {math.factorial(4)}")
print()