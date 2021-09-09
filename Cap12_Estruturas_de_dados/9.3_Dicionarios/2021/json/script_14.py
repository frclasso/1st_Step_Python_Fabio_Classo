import os
import json

# CONVERTE DICIONARIO PARA JSON STRNG

person = {
    "name": "jane doe",
    "salary": 9000,
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "JaneDoe@pynative.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}

print(type(person))
person_json = json.dumps(person, indent=4) # CONVERTE UM TIPO PYTHON EM JSON STRING
print(type(person_json)) # str
print(person_json)


file_path = "C:/Users/fabio.classo/Downloads/fabio/"\
"aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/"\
    "9.3_Dicionarios/2021/json"

os.chdir(file_path)

# Writing  JSON file
with open('person_2.json', 'w') as json_file:
    json.dump(person, json_file)  # RECEBE UM DICIONARIO E ESCREVE UM AQUIVO JSON
    
    # pretify json
    #json.dump(person, json_file, indent=4)

