"""
Многопоточный эхо-сервер
"""
from threading import Thread
import socket


def echo(client: socket):
    while True:
        data = client.recv(2048)
        print(f'Получено: {data}, отправляю!')
        client.sendall(data)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', 8080))
        server.listen()
        while True:
            connection, _ = server.accept()  # Блокируется в ожидании подключения клиентов
            # Как только клиент подключился - создать поток для выполнения функции echo
            thread = Thread(target=echo, args=(connection,))
            thread.start()  # Начать выполнение потока


if __name__ == '__main__':
    main()
