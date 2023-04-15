"""
Чтение данных из сокета
"""
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8080)
server_socket.bind(server_address)
server_socket.listen()

print('Сервер запущен')
try:
    connections, client_address = server_socket.accept()
    print(f'Получен запрос на подключение от {client_address}!')

    buffer = b''  # буфер обмена
    while buffer[-2:] != b'\r\n':
        data = connections.recv(2)
        if not data:
            break
        else:
            print(f'Получены данные: {data}')
            buffer += data
    print(f'Все данные: {buffer}')
finally:
    server_socket.close()
