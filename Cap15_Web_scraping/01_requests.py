

import requests

response = requests.get('https://api.github.com/')
print(response)
print(response.status_code)





# fonte
#https://realpython.com/python-requests/
# https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html