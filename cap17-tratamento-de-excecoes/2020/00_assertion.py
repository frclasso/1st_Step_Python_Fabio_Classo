# Assertion
# assertion expressao, argumentos



num = int(input('Digite um numero: '))
assert num >= 0
print(f"Voce digitou o numero: {num}")



num = int(input('Digite um numero: '))
assert num >= 0, "Apenas numeros positivos serão aceitos."
print(f"Voce digitou o numero: {num}")
