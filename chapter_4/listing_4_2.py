"""
Отправка веб-запроса с помощью aiohttp
"""
import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_4 import fetch_status


# @async_timed()
# async def fetch_status(session: ClientSession, url: str) -> int:
#     async with session.get(url) as result:
#         return result.status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Состояние для {url} было равно {status}')


if __name__ == '__main__':
    asyncio.run(main())
