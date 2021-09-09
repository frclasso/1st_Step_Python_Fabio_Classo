
import json
import requests

# REAL WORLD EXAMPLE - GETTING DATA FROM API

# API - https://jsonplaceholder.typicode.com/

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(type(todos))
#print(todos)
print(todos[:10]) # DEZ PRIMEIROS REGISTROS
# for t in todos:
#     print(t)


"""
ESTRUTURA DO NOSSO JSON:
{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
}

"""


# https://realpython.com/python-json/