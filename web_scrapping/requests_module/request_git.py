import requests
from requests.exceptions import HTTPError

url = 'https://api.github.com'

response = requests.get(url)

'''
Status code:
1xx - information
2xx - sucess
3xx - redirect
4xx - client errors
5xx - server errors
'''

if response:
    print('Success')
else:
    print('Not found')

####################3

for url in ['https://api.github.com', 'https://api.github.com/some_invalid_url']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Http error: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success')