import requests

# 1
params = {'status': 'available'}
r = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params)

print(r.status_code)
print(r.json())


username = 'string'
r1 = requests.get(f'https://petstore.swagger.io/v2/user/{username}')

print(r1.status_code)
print(r1.json())
