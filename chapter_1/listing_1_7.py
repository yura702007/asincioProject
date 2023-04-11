"""
Мультипроцессорное вычисление чисел Фибоначчи
"""
import time
import multiprocessing


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    print(f'fib({number}) равно {fib(number)}')


def fibs_with_process():
    fortieth_process = multiprocessing.Process(target=print_fib, args=(40,))
    forty_first_process = multiprocessing.Process(target=print_fib, args=(41,))

    fortieth_process.start()
    forty_first_process.start()

    fortieth_process.join()
    forty_first_process.join()


if __name__ == '__main__':
    start = time.time()
    fibs_with_process()
    end = time.time()
    print(f'Время работы: {end - start}')

