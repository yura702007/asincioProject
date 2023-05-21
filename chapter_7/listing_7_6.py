"""
Использование исполнителя по умолчанию
"""
import asyncio
from functools import partial
from util import async_timed
from chapter_7 import URL, get_status_code


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    urls = [URL for _ in range(1000)]
    tasks = [loop.run_in_executor(None, partial(get_status_code, url)) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
