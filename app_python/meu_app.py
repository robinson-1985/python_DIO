'''print('Meu primeiro programa')
a = 2
b = 4
soma = a + b
print(soma)'''

import requests
url = 'https://digitalinnovation.one'
response = requests.get(url)
status_code = response.status_code

