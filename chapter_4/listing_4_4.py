"""
Неправильное использование спискового включения для создания и ожидания задач
"""
import asyncio
from util import delay, async_timed


@async_timed()
async def main():
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(second)) for second in delay_times]


if __name__ == '__main__':
    asyncio.run(main())
