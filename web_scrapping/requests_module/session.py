import requests
from getpass import getpass

# Using a context manager, you can release resources after use
with requests.Session() as session:
    session.auth = ('some_github_user', getpass())

    # instead of get we use session.get
    response = session.get('https://api.gihub.com/user')
    response2 = session.get('https://api.gihub.com/user/repos')
    

print(response.headers)
print(response.json())

# Getting first repo
print(response2.json()][0]['url'])