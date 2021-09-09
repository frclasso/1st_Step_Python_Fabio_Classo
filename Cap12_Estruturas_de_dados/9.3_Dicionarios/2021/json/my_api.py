import json
import requests
import os

file_path = "C:/Users/fabio.classo/Downloads/fabio/"\
"aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/"\
    "9.3_Dicionarios/2021/json"
os.chdir(file_path)


def get_data():

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    return todos


"""
ESTRUTURA DO NOSSO JSON:
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
}
"""
# for data in get_data():
#     print(data)

def get_one_register():
    one = get_data()[:1]
    #print(type(one))
    return one

#print(get_one_register())
# for r in get_one_register():
#     print(r)
#     if r['completed'] == False:
#         print('ok')


def get_all_completed_registers():
    completed_resgisters = []
    for register in get_data():
        if register['completed'] == True:
            completed_resgisters.append(register)
    return completed_resgisters
        
for completed in get_all_completed_registers():
    print(completed)


# saving completed registers in a josn file
def save_data_to_json():
    with open('completed.json', 'w') as file:
        json.dump(get_all_completed_registers(),file, indent=4)