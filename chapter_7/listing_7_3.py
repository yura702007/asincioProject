"""
Базовое использование requests
"""
import requests


def get_status_code(_url: str) -> int:
    response = requests.get(url=_url)
    return response.status_code


if __name__ == '__main__':
    url = 'https://www.example.com'
    print(get_status_code(url))
    print(get_status_code(url))
