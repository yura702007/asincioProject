"""
Попытка выполнение задач в фоновом режиме
"""
import asyncio
from util import delay


async def main():
    while True:
        delay_time = input('Введите время сна: ')
        if delay_time:
            await asyncio.create_task(delay(int(delay_time)))
        else:
            break


if __name__ == '__main__':
    asyncio.run(main())
