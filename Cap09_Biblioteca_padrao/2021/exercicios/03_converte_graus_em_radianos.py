
# Escreva um programa Python para converter graus em radianos.

"""
Nota: O radiano é a unidade padrão de medida angular, usada em muitas áreas da matemática. 
A medida de um ângulo em radianos é numericamente igual ao comprimento de um arco correspondente 
de um círculo unitário; um radiano é pouco 
menos de 57,3 graus (quando o comprimento do arco é igual ao raio). 
"""

# dica: uitlize a função input para que a entrada seja dinamica

#Degree : 15
#Expected Result in radians: 0.2619047619047619

pi=22/7
degree = float(input("Input degrees: ")) #90
radian = degree*(pi/180)
print(radian)