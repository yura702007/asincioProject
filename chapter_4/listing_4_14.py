"""
Обработка всех запросов по мере поступления
"""
import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        pending = [
            asyncio.create_task(fetch_status(session, url, 3)),
            asyncio.create_task(fetch_status(session, url, 3)),
            asyncio.create_task(fetch_status(session, url, 3))
        ]
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            print(f'Число завершившихся задач: {len(done)}')
            print(f'Число ожидающих задач: {len(pending)}')

            for done_task in done:
                print(await done_task)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
