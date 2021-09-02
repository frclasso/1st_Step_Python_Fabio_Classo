import os
import json

#print(os.getcwd())
os.chdir("C:/Users/fabio.classo/Downloads/fabio/aulas_python/1st_Step_Python_Fabio_Classo-master/Cap12_Estruturas_de_dados/9.3_Dicionarios/2021")
print(os.getcwd())

def read_json_data():
	"""Converting JSON encoded data into Python dictionary"""
	with open("developer.json", "r") as read_file:
		developer = json.load(read_file)

		for key, value in developer.items():
			print(key, ":", value)

read_json_data()

def add_new_skills(skill):
	with open("developer.json", "r") as read_file:
		developer = json.load(read_file)
		print(developer['skills'])
		print(type(developer['skills']))
		developer['skills'].append('Python')
		print(developer['skills'])
		return(developer)
add_new_skills('python')


def save_data(data):
	with open("developer_updated.json", "w") as  write_file:
		 json.dump(data, write_file, indent=4)

save_data(add_new_skills("Python"))