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
    connection, client_address = server_socket.accept()
    print(f'Получен запрос на подключение от {client_address}!')

    buffer = b''  # буфер обмена
    while buffer[-2:] != b'\r\n':
        data = connection.recv(2)  # чтение данных
        if not data:
            break
        else:
            print(f'Получены данные: {data}')
            buffer += data
    print(f'Все данные: {buffer}')
    connection.sendall(buffer)  # отправка данных клиенту
finally:
    server_socket.close()
