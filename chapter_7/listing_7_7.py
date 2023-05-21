"""
Использование сопрограммы to_thread
"""
import asyncio
from util import async_timed
from chapter_7 import URL, get_status_code


@async_timed()
async def main():
    urls = [URL for _ in range(1000)]
    tasks = [asyncio.to_thread(get_status_code, url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
