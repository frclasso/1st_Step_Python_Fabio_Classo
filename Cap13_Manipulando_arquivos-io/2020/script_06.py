


techs = ['Python\n', 'Django\n', 'Ruby\n', 'C++\n']

with open('teste.txt', 'w') as file_writer:
    file_writer.writelines(techs) # writelines espera uma lista


techs = ['Python', 'Django', 'Ruby', 'C++']

with open('teste.txt', 'a') as file_writer:
    #file_writer.write(techs)  #ERRO
    for t in techs:
        file_writer.write(t + '\n')



