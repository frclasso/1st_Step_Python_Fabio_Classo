#!/usr/bin/env python3

"""Aqui o argumento está sendo passado por referência e
a referência está sendo sobrescrita dentro da função chamada."""


def changeme(mylist):
    "This is change  a passed list into this function."
    mylist=[1,2,3,4] # Isso atribuiria nova referência em mylist
    print("Values inside the function: ", mylist)
    return


#criando a lista
mylist=[10,20,30]

#Chamando a funcao
changeme(mylist)
print("Values outside the function: ",mylist)
