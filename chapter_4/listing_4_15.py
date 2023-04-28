"""
Использование тайм-аута в wait
"""
import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        fetches = [
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url)),
            asyncio.create_task(fetch_status(session, url, 3))
        ]
        done, pending = await asyncio.wait(fetches, timeout=1)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for task in done:
            print(await task)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
