"""
Выполнение счётного кода в отладочном режиме
"""
import asyncio
from util import async_timed


@async_timed()
async def cpu_bond_work() -> int:
    counter = 0
    for _ in range(100000000):
        counter += 1
    return counter


@async_timed()
async def main():
    task = asyncio.create_task(cpu_bond_work())
    result = await task
    print(result)


if __name__ == '__main__':
    asyncio.run(main(), debug=True)
