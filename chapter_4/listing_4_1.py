"""
Асинхронный контекстный менеджер, ожидающий подключения клиента
"""
import asyncio
import socket
from types import TracebackType
from typing import Optional, Type

SERVER_ADDRESS = ('127.0.0.1', 8080)


class ConnectedSocket:

    def __init__(self, server_socket):
        self._connection = None
        self._server_socket = server_socket

    async def __aenter__(self):
        """
        Этот метод вызывается при входе в блок with.
        Он ждёт подключения клиента и
        возвращает это подключение
        :return: connection
        """
        print('Вход в контекстный менеджер, ожидание подключения')
        loop = asyncio.get_event_loop()
        connection, address = await loop.sock_accept(self._server_socket)
        self._connection = connection
        print('Подключение подтверждено')
        return self._connection

    async def __aexit__(self,
                        exc_type: Optional[Type[BaseException]],
                        exc_val: Optional[BaseException],
                        exc_tb: Optional[TracebackType]):
        """
        Этот метод вызывается при выходе из блока with.
        В нём производится очистка ресурса,
        в данном случае закрывается подключение
        :param exc_type: Optional[Type[BaseException]]
        :param exc_val: Optional[BaseException]
        :param exc_tb: Optional[TracebackType]
        :return: None
        """
        print('Выход из контекстного менеджера')
        self._connection.close()
        print('Подключение закрыто')


def create_server(address=SERVER_ADDRESS):
    """
    Создаёт сокет-сервер
    :param address: tuple
    :return: socket
    """
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    _socket.setblocking(False)
    _socket.bind(address)
    return _socket


async def main():
    loop = asyncio.get_event_loop()
    server = create_server()
    server.listen()

    async with ConnectedSocket(server_socket=server) as connection:
        data = await loop.sock_recv(connection, 1024)
        print(str(data))


if __name__ == '__main__':
    asyncio.run(main())

