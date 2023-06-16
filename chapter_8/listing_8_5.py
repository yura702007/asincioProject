"""
Использование стандартного ввода в отдельном потоке
"""
import asyncio
from util import delay, async_timed


def input_number():
    number = input('Введите число: ')
    if number:
        return int(number)
    return


@async_timed()
async def main():
    coro = asyncio.to_thread(input_number)
    while True:
        task = asyncio.create_task(coro)
        timing = await task
        if timing:
            await delay(timing)
            coro = asyncio.to_thread(input_number)
        else:
            break


if __name__ == '__main__':
    asyncio.run(main())
