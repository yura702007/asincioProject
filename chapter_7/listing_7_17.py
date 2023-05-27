"""
Хеширование с применением многопоточности и asyncio
"""
import asyncio
import hashlib
import os
import random
import string
from functools import partial
from concurrent.futures.thread import ThreadPoolExecutor
from util import async_timed


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


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    tasks = []
    with ThreadPoolExecutor() as pool:
        for password in passwords:
            tasks.append(loop.run_in_executor(pool, partial(hashing, password)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())


