import requests
from requests.exceptions import HTTPError

response = requests.get('https://api.github.com')
print(response.content)
for url in response.content:
    print(url)

# fonte
#https://realpython.com/python-requests/
# https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html