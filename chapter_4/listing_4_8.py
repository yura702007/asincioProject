"""
Обработка исключений при использовании gather
"""
import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com', 'python://example.com']
        tasks = [fetch_status(session=session, url=url) for url in urls]
        status_codes = await asyncio.gather(*tasks, return_exceptions=True)
        print(status_codes)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
