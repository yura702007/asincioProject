"""
Создание цикла событий в ручную
"""
import asyncio
from util import delay


async def main():
    task_1 = asyncio.create_task(delay(10))
    task_2 = asyncio.create_task(delay(5))

    await task_1
    await task_2


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # создание цикла событий
    try:
        loop.run_until_complete(main())  # запуск цикла событий
    finally:
        loop.close()  # закрытие цикла событий
