"""
Задание тайм-аута для as_completed
"""
import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, 'https://example.com', 1),
            fetch_status(session, 'https://example.com', 10),
            fetch_status(session, 'https://example.com', 10)
        ]
        for task in asyncio.as_completed(fetchers, timeout=2):
            result = await task
            print(result)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())