
# Escreva um programa Python para converter radianos em graus.

"""
Nota: O radiano é a unidade padrão de medida angular, usada em muitas áreas da matemática. 
A medida de um ângulo em radianos é numericamente igual ao comprimento de um arco correspondente 
de um círculo unitário; um radiano é pouco menos de 57,3 graus 
(quando o comprimento do arco é igual ao rai
"""

#Radian : .52
#Expected Result : 29.781818181818185


pi=22/7
radian = float(input("Input radians: "))
degree = radian*(180/pi)
print(degree)