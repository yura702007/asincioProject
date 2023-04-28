"""
Обработка ислючений при использовании wait
"""
import asyncio
import logging

from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        good_request = fetch_status(session, 'http://www.example.com')
        bad_request = fetch_status(session, 'python://bad')

        fetchers = [
            asyncio.create_task(good_request),
            asyncio.create_task(bad_request)
        ]

        done, pending = await asyncio.wait(fetchers)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            if done_task.exception():
                logging.error('При выполнении запроса возникло исключение', exc_info=done_task.exception())
            else:
                print(done_task.result())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
