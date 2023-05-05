"""
Исполнители пула процессов
"""
import time
from concurrent.futures import ProcessPoolExecutor
from listing_6_1 import count


if __name__ == '__main__':
    start = time.time()
    with ProcessPoolExecutor() as pool:
        numbers = [1, 3, 5, 22, 100000000]
        for result in pool.map(count, numbers):
            print(result)
    print(time.time() - start)