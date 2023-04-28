"""
Отмена работающих запросов при возникновении исключения
"""
import logging
import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        fetches = [
            asyncio.create_task(fetch_status(session, 'python://bad')),
            asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3)),
            asyncio.create_task(fetch_status(session, 'https://www.example.com', delay=3))
        ]
        done, pending = await asyncio.wait(fetches, return_when=asyncio.FIRST_EXCEPTION)
        print(f'Число завершившихся задач: {len(done)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for done_task in done:
            if done_task.exception():
                logging.error('При выполнении запроса возникло исключение', exc_info=done_task.exception())
            else:
                print(done_task.result())

        for pending_task in pending:
            pending_task.cancel()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
