"""
Завершение допускающих ожидание задач не по порядку
"""
import asyncio
from util import delay, async_timed


@async_timed()
async def main():
    tasks = [delay(s) for s in range(9, 0, -1)]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == '__main__':
    asyncio.run(main())
