import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.session()

session.mount('https://api.gihub.com', github_adapter)

try:
    session.get('https://api.gihub.com')
except ConnectionError as ce:
    print(ce)