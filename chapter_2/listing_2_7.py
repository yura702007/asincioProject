"""
Выполнение двух сопрограмм
"""
import asyncio
from util import delay


async def add_one(number: int) -> int:
    return number + 1


async def hello_world_message() -> str:
    await delay(1)
    return 'Hello, World!!!'


async def main() -> None:
    message = await hello_world_message()  # Приостановить main() до возврата из hello_world_message()
    one_add_one = await add_one(1)  # Приостановить main() до возврата из add_one()
    print(message)
    print(one_add_one)


if __name__ == '__main__':
    asyncio.run(main())
