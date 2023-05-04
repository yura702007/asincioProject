"""
Создание пула процессов
"""
import time
from multiprocessing import Pool


def say_hello(name: str) -> str:
    start_fun = time.time()
    time.sleep(3)
    result = f'Hello, {name}!!!'
    end_fun = time.time() - start_fun
    print(f'Функция отработала за {end_fun} секунд')
    return result


if __name__ == '__main__':
    start = time.time()
    with Pool() as pool:  # Создать пул процессов
        # Выполнить say_hello с аргументом Jeff в отдельном процессе и получить результат
        hi_jeff = pool.apply(say_hello, args=('Jeff',))
        hi_john = pool.apply(say_hello, args=('John',))
        print(hi_jeff)
        print(hi_john)
    print(time.time() - start)