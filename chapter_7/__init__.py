import requests

URL = 'https://www.example.com'


def get_status_code(_url: str) -> int:
    response = requests.get(url=_url)
    return response.status_code
