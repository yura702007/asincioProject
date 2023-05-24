"""
Взаимоблокировка
"""
from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a:  # Захватить блокировку a
        print('Захвачена блокировка а из метода а')
        time.sleep(1)  # Ждать одну секунду, это создаёт подходящие условия для взаимоблокировки
        with lock_b:  # Захватить блокировку b
            print('Захвачены обе блокировки из метода а')


def b():
    with lock_b:  # Захватить блокировку b
        print('Захвачена блокировка b из метода b')
        with lock_a:  # Захватить блокировку a
            print('Захвачены обе блокировки из метода b')


if __name__ == '__main__':
    thread_a = Thread(target=a)
    thread_b = Thread(target=b)
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
