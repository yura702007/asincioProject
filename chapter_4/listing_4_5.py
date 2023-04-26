"""
Использование спискового включения для конкурентного выполнения задач
"""
import asyncio
from util import delay, async_timed


@async_timed()
async def main():
    delay_times = [3, 3, 3]
    tasks = [asyncio.create_task(delay(second)) for second in delay_times]
    [await task for task in tasks]


if __name__ == '__main__':
    asyncio.run(main())
