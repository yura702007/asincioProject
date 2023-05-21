"""
Выполнение запросов с помощью пула потоков
"""
import time
from concurrent.futures.thread import ThreadPoolExecutor
from chapter_7.listing_7_3 import get_status_code

URL = 'https://www.example.com'

if __name__ == '__main__':
    start = time.time()

    with ThreadPoolExecutor(max_workers=1000) as pool:
        urls = [URL for _ in range(1000)]
        results = pool.map(get_status_code, urls)
        for result in results:
            print(result)

    print(f'Выполнение 1000 запросов завершено за {time.time() - start}с.')
