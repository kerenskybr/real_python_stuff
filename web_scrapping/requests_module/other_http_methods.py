import requests

url = 'https://httpbin.org/'

response = requests.post(url + 'post', data = {'key': 'value'})
print('POST', response.headers)

response = requests.put(url + 'post', data = {'key': 'value'})
print('PUT', response.headers)

response = requests.delete(url + 'post', data = {'key': 'value'})
print('DELETE', response.headers)
