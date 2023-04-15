"""
Создание неблокирующего сокета
"""
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8282))
server_socket.listen()
server_socket.setblocking(False)  # снятие блокировки
