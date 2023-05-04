"""
Два параллельных процесса
"""
from multiprocessing import Process
import time


def count(count_to: int) -> int:
    start = time.time()
    counter = 0
    while counter < count_to:
        counter += 1
    job_time = time.time() - start
    print(f'Подсчёт до {count_to} закончен за {job_time} секунд')
    return counter


if __name__ == '__main__':
    start_time = time.time()

    # Создать процесс для выполнения функции count
    to_one_hundred_million = Process(target=count, args=(10 ** 8,))
    to_two_hundred_million = Process(target=count, args=(10 ** 8 * 2,))

    # Запустить этот процесс. Этот метод возвращает управление немедленно
    to_one_hundred_million.start()
    to_two_hundred_million.start()

    # Ждать завершения процесса. Этот метод блокирует выполнение, пока процесс не завершится
    to_one_hundred_million.join()
    to_two_hundred_million.join()

    end_time = time.time() - start_time
    print(f'Полное время работы - {end_time} секунд')
