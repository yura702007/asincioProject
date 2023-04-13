"""
Выполнение кода, пока другие операции работают в фоне
"""
import asyncio
from util import delay


async def hello_every_second() -> None:
    for i in range(2):
        await asyncio.sleep(1)
        print('Пока я жду, исполняется другой код')


async def main() -> None:
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))

    await hello_every_second()
    await first_delay
    await second_delay


if __name__ == '__main__':
    asyncio.run(main())
