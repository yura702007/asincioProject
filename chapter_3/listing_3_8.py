"""
Построение асинхронного эхо-сервера
"""
import asyncio
import socket
from asyncio import AbstractEventLoop
import logging


async def echo(connection: socket, loop: AbstractEventLoop) -> None:
    try:
        message = b''
        while data := await loop.sock_recv(connection, 1024):  # В бесконечном цикле ожидаем данные от клиента
            message += data
            if data == b'\r\n':
                if message == b'boom\r\n':
                    raise Exception('Неожиданная ошибка сети')
                await loop.sock_sendall(connection, message.upper())  # Получив данные отправляем их обратно клиенту
                message = b''
    except Exception as exp:
        logging.exception(exp)
    finally:
        connection.close()


async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
    while True:
        connection, client_address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от {client_address}')
        # После получения запроса на подключение создаём задачу echo, ожидающую данные от клиента
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8080)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()
    # Запускаем сопрограмму прослушивания порта на предмет подлючений
    await listen_for_connection(server_socket, asyncio.get_event_loop())


if __name__ == '__main__':
    asyncio.run(main())
