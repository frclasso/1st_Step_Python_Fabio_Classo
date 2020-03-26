student = {'Name':'John', 'age':34, 'courses':['Math', 'Science']}

#print(student['Name'])
#print(student['phone']) # KeyError

# Método get retorna "None" caso nao encontre ou pode se passar um string de saída
# print(student.get('phone','Key Not Found!'))
#
# student.update({'Name':'Fabio', 'age':43, 'phone':'555-555'})
# print(student)

# age = student.pop('age')
# print(age)

for k, v in student.items():
    print(k, '==>', v)