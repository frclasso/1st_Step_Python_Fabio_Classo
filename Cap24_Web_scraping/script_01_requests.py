import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com/', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Http error ocurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success')



# fonte
#https://realpython.com/python-requests/
# https://requests.readthedocs.io/pt_BR/latest/user/quickstart.html