"""
Хеширование паролей с помощью алгоритма scrypt
"""
import hashlib
import os
import string
import time
import random


def random_password(length: int) -> bytes:
    """
    Создание случайного
    пароля из length
    символов
    :param length: int
    :return: bytes
    """
    ascii_lowercase = string.ascii_lowercase.encode()
    return b''.join(bytes(random.choice(ascii_lowercase)) for _ in range(length))


passwords = [random_password(10) for _ in range(10000)]


def hashing(password: bytes) -> str:
    """
    хэширование строки байтов
    :param password: bytes
    :return: hash
    """
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))


start = time.time()
for word in passwords:
    hashing(word)
print(time.time() - start)
