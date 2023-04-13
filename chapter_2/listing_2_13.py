"""
Защита задачи от снятия
"""


import asyncio
from util import delay


async def main() -> None:
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), timeout=5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Задача заняла более 5 секунд, скоро она закончится')
        result = await task
        print(result)


if __name__ == '__main__':
    asyncio.run(main())
