"""
Печать информации о состоянии отправки запросов
"""
import asyncio
from functools import partial
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Lock
from chapter_7 import URL, get_status_code
from util import async_timed

counter_lock = Lock()
counter: int = 0


def increment_counter(url: str) -> int:
    global counter
    status_code = get_status_code(url)
    with counter_lock:
        counter += 1
    return status_code


async def reporter(count: int):
    while counter < count:
        print(f'Завершено запросов: {counter}/{count}')
        await asyncio.sleep(.5)


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=200) as pool:
        request_count = 1200
        urls = [URL for _ in range(request_count)]
        reporter_task = asyncio.create_task(reporter(request_count))
        tasks = [loop.run_in_executor(pool, partial(increment_counter, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        await reporter_task
        print(results)


if __name__ == '__main__':
    asyncio.run(main())
