import requests
from getpass import getpass
'''
url = 'https://api.github.com/user'

requests.get(url, auth=('kerenskybr', getpass()))
###########################3
'''
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme"""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API to custom auth header"""
        r.headers['X-TokenAuth'] = f'{self.token}'
        return r

response = requests.get('https://httpbin.org/get', auth=TokenAuth('1234abcde-token'))
print(response)