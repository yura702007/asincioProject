"""
Запуск сервера и прослушивание порта для подключения
"""
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создать TCP-сервер
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8080)  # Задать ip-адрес и номер порта сервера
server_socket.bind(server_address)  # активировать сервер
server_socket.listen()  # прослушивать сервер

connection, client_address = server_socket.accept()  # Дождаться подключения и выделить клиенту почтовый ящик
print(f'Получен запрос на подключение с {client_address}')
