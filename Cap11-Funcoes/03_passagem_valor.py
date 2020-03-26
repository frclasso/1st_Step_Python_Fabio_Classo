#!/usr/bin/env python3



def changeme(mylist):
    "Essa função Não altera a lista passada como argumento"
    mylist=[1,2,3,4] # Isso atribuiria nova referência em mylist
    print("Values inside the function: ", mylist)
    return


#criando a lista
mylist=[10,20,30]

#Chamando a funcao
changeme(mylist)
print("Values outside the function: ",mylist)
