"""
Задание тайм-аутов в aiohttp
"""
import asyncio
from aiohttp import ClientSession, ClientTimeout


async def fetch_status(session: ClientSession, url: str) -> int:
    ten_millis = ClientTimeout(total=.58)
    async with session.get(url, timeout=ten_millis) as result:
        return result.status


async def main():
    session_timeout = ClientTimeout(total=1, connect=.1)
    async with ClientSession(timeout=session_timeout) as session:
        result = await fetch_status(session=session, url='https://example.com')
        print(result)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
