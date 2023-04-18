"""
Использование селектора для построения неблокирующего сокета
"""
import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple


selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8080)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)  # Создать селектор с тайм-аутом 1 с.
    if len(events) == 0:  # Если ничего не произошло, сообщить об этом.
        print('Событий нет, подожду ещё')
    for event, _ in events:
        event_socket = event.fileobj  # Получить сокет, для которого произошло событие
        if event_socket == server_socket:

            # Если событие произошло с серверным сокетом, значит была попытка подключения
            connection, client_address = server_socket.accept()
            connection.setblocking(False)
            print(f'Получен запрос на подключение от {client_address}')

            # Зарегистрировать клиент, подкючившийся к сокету
            selector.register(connection, selectors.EVENT_READ)
        else:
            # Если событие произошло не с серверным сокетом,
            # получить данные от клиента и отправить их обратно
            data = event_socket.recv(1024)
            print(f'Получены данные: {data}')
            event_socket.send(data)
