"""
Исполнитель пула процессов в сочетании с asyncio
"""
import asyncio
import time
from asyncio.events import AbstractEventLoop
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from typing import List
from listing_6_1 import count


async def main():
    with ProcessPoolExecutor() as pool:
        # Создать частично применяемую функцию count с фиксированным аргументом
        loop: AbstractEventLoop = asyncio.get_running_loop()
        nums = [1, 3, 5, 22, 100000000]
        # Сформировать все обращения к пулу процессов, поместив их в список
        calls: List[partial[int]] = [partial(count, num) for num in nums]
        call_coros = []

        for call in calls:
            call_coros.append(loop.run_in_executor(pool, call))

        # Ждать результатов
        results = await asyncio.gather(*call_coros)

        for result in results:
            print(result)


if __name__ == '__main__':
    start = time.time()
    print('Start')
    asyncio.run(main())
    print('The End')
    print(time.time() - start)
