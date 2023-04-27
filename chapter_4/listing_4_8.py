"""
Использование as_completed
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
            fetch_status(session, 'https://example.com', 1),
            fetch_status(session, 'https://example.com', 10)
        ]
        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
