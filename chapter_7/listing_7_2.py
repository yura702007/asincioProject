"""
Создание подкласса Thread для чистой остановки
"""
from threading import Thread
import socket


class ClientEchoThread(Thread):

    def __init__(self, client):
        super().__init__()
        self.client = client

    def run(self):
        try:
            while True:
                data = self.client.recv(2048)
                if not data:
                    # Если нет данных возбудить исключение,
                    # это бывает, если подключение было закрыто сервером или остановленно клиентом
                    raise BrokenPipeError
                print(f'Получено сообщение: {data}, отправляю!')
                self.client.sendall(data)
        except OSError as exc:  # В случае исключения выйти из метода run(), при этом поток завершается
            print(f'Поток прерван исключением {exc}, производится остановка!')

    def close(self):
        # Разомкнуть подключение, если поток активен.
        # Поток может быть не активен, если клиент закрыл подключение
        if self.is_alive():
            self.client.sendall(bytes('Останавливаюсь!', encoding='utf8'))
            self.client.shutdown(socket.SHUT_RDWR)  # Разомкнуть подключение клиента, остановив чтение и запись


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('127.0.0.1', 8080))
        server.listen()
        connection_threads = []
        try:
            while True:
                connection, addr = server.accept()
                thread = ClientEchoThread(connection)
                connection_threads.append(thread)
                thread.start()
        except KeyboardInterrupt:
            print('Останавливаюсь')
            # Вызвать метод close() созданных потоков, чтобы разомкнуть все клиентские подключения,
            # в случае прерывания с клавиатуры
            [thread.close() for thread in connection_threads]


if __name__ == '__main__':
    main()
