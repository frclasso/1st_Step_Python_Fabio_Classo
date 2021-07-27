# Dos inúmeros módulos da biblioteca padrao, escolhi o móduto matemático (Math) pela
# grande utilização em nosso dia a dia.

import math

#print(dir(math))
#print()

# funções built-in 
x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x) 

# do modulo math
x = math.sqrt(64)

print(x) 

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1 



print(f"PI: {math.pi}")
print(f"e: {math.e}")
print()


# Potencia pow()
print(f"Tres ao quadrado: {3 ** 2}")
print(f"Tres ao quadrado utilizando math.pow(): {math.pow(3,2)}")


print('Radians')
print('radians(3):', math.radians(3))
print('radians(-3):', math.radians(-3))
print('radians(0):', math.radians(0))
print()


"""math.degrees(x)
Convert angle x from radians to degrees."""
print("Degrees")
print("Degrees 0.05235987755982989  ==> {:.1f}".format(math.degrees(0.05235987755982989)))
print("Degrees -0.05235987755982989  ==> {:.1f}".format(math.degrees(-0.05235987755982989)))