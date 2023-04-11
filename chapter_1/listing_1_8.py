"""
Синхронные веб-запросы
"""
import time
import requests


def get_response():
    response = requests.get('https://example.com')
    print(response.status_code)


if __name__ == '__main__':
    start = time.time()

    get_response()
    get_response()

    end = time.time()
    print(f'Затрачено времени: {end - start}')
