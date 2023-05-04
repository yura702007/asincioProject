"""
Асинхронное получение результатов от пула процессов
"""
import time
from multiprocessing import Pool
from listing_6_2 import say_hello


if __name__ == '__main__':
    print('Start')
    start = time.time()
    with Pool() as pool:
        hi_jeff = pool.apply_async(say_hello, args=('Jeff',))
        hi_john = pool.apply_async(say_hello, args=('John',))
        print(hi_jeff.get())
        print(hi_john.get())
    print(time.time() - start)
    print('The End')
