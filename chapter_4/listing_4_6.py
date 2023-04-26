"""
Конкурентное выполнение запросов с помощью gather
"""
import asyncio
from aiohttp import ClientSession
from chapter_4 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        statuses = await asyncio.gather(*requests)
        print(statuses)
        print(len(statuses))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
