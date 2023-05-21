"""
Использование исполнителя пула потоков совместно с asyncio
"""
import asyncio
import functools
from concurrent.futures.thread import ThreadPoolExecutor
from util import async_timed
from chapter_7.listing_7_4 import URL, get_status_code


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(max_workers=100) as pool:
        urls = [URL for _ in range(1000)]
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)


if __name__ == '__main__':
    asyncio.run(main())
