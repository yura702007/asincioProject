"""
Создание многопочного Python-приложения
"""
import threading


def hello_from_thread():
    print(f'Привет от потока {threading.current_thread()}')


def hello_to_world():
    print(f'Привет мир, в потоке {threading.current_thread()}')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

hello_world = threading.Thread(target=hello_to_world)
hello_world.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент Python исполняет {total_threads} потоков')
print(f'Имя текущего потока {thread_name}')
hello_thread.join()
hello_world.join()
