# Assertion
# assertion expressao, argumentos

try:
    num=int(input('Digite um  numero: '))
    assert(num >=0), "Apenas fibonacci_exemplos positivos serão aceitos."
    print(num)
except AssertionError as msg:
    print(msg)