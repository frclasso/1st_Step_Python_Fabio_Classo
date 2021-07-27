class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def __repr__(self):
        return '({},{},{})'.format(self.nome, self.idade,self.salario)

emp1 = Empregado('Carl', 37, 7000)
emp2 = Empregado('Sarah', 29, 9000)
emp3 = Empregado('John', 43, 8000)


empregados = [emp1, emp2, emp3]

# 1
#s_empregados = sorted(empregados)

#def e_sort(emp):
    #return emp.nome

#s_empregados = sorted(empregados, key=e_sort, reverse=True)

# 2
# ou , usar uma funcao anonima
# s_empregados = sorted(empregados, key=lambda e: e.nome, reverse=True)
#
# print(s_empregados)

# 3, usando attrgetter
from operator import attrgetter
s_empregados = sorted(empregados, key=attrgetter('idade'))

print(s_empregados)




