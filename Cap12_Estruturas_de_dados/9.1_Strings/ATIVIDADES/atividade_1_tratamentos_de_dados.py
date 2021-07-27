
# cadastro de cliente

cliente1 = ['FABIO', 'REIS CLASSO','.111.222.333', '123456789', '(48)9174-3152']

# NOME COMPLETO
nome = cliente1[0]
sobrenome = cliente1[1]
nome_completo = nome + ' ' + sobrenome

# INSERIR CAMPO EMAIL
email = nome+sobrenome+'@empresa.com.br'
email = email.lower()
#print(email)

cpf = cliente1[2]
cpf_new = cpf.zfill(15)

idt = cliente1[3]
idt_new = idt.zfill(10)


#adicionar 9
telefone_old = cliente1[4]
telefone_new = []
# print(telefone_old)
for t in telefone_old:
    if t in (['(', ')', '-']):
        telefone_old.split(t)
        #print(t)
    else:
        #print(t)
        telefone_new.append(t)

print(telefone_new)
telefone_new.insert(2, '9')
print(telefone_new)
tel = ''.join(telefone_new)
print(tel)


print()
cliente1_new = [nome_completo, cpf_new, idt, tel]
print(cliente1_new)