"""
Изучение поведения wait по умолчанию
"""
import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, 'https://example.com')),
            asyncio.create_task(fetch_status(session, 'https://example.com'))
        ]
        done, pending = await asyncio.wait(fetchers, return_when='ALL_COMPLETED')
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
