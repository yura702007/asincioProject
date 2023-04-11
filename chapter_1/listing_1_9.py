"""
Потоковые веб-запросы
"""
import time
import threading
import requests


def get_response() -> None:
    response = requests.get('https://example.com')
    print(response.status_code)


def threading_requests() -> None:
    request_1 = threading.Thread(target=get_response)
    request_2 = threading.Thread(target=get_response)

    request_1.start()
    request_2.start()

    print('Все потоки работают')

    request_1.join()
    request_2.join()


if __name__ == '__main__':
    start = time.time()

    threading_requests()

    end = time.time()
    print(f'Затрачено времени: {end - start}')
