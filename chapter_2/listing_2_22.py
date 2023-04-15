"""
Получение доступа к циклу событий
"""
import asyncio
from util import delay


def call_later():
    print('Меня вызовут позже')


async def main():
    loop = asyncio.get_running_loop()  # Доступ к запущенному циклу событий
    loop.call_soon(call_later)  # Планирование вызова функции на следующей итерации ЦС
    await delay(3)


if __name__ == '__main__':
    asyncio.run(main())
