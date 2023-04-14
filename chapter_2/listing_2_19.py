"""
Счётный код и длительная задача
"""
import asyncio
from util import async_timed, delay


@async_timed()
async def cpu_bond_work() -> int:
    counter = 0
    for _ in range(100000000):
        counter += 1
    return counter


@async_timed()
async def main():
    one_task = asyncio.create_task(cpu_bond_work())
    two_task = asyncio.create_task(cpu_bond_work())
    delay_task = asyncio.create_task(delay(4))
    await one_task
    await two_task
    await delay_task


if __name__ == '__main__':
    asyncio.run(main())
