# bitwise

a = 60
b = 13

print(format(a, '08b'))
#print(bin(a))
print(format(b, '08b'))
#print((bin(b)))

print('________________')
print(format(a & b, '08b'), '<== AND operator')
print(format(a and b, '08b'), '<== AND operator')
print(format(a | b, '08b'), '<== OR operator')
print(format(a or b, '08b'), '<== OR operator')
print(format(a ^ b, '08b'), '<== XOR operator')
print(~a)
print(format(~a, '08b'))
print(format(a, '08b'))
print(format(a << 2, '08b'), ', Deslocamento para esquerda')
n = (a << 2)
print(n)
print(n, '=', format(n >> 2, '08b'), ', Deslocamento para direita')