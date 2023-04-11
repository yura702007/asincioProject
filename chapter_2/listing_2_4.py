"""
Использование await для ожидания результата сопрограммы
"""
import asyncio


async def add_one(number: int) -> int:
    return number + 1


async def main() -> None:
    one_add_one = await add_one(1)  # Приостановиться и ждать результата add_one(1)
    two_add_one = await add_one(2)  # Приостановиться и ждать результата add_one(2)

    print(one_add_one)
    print(two_add_one)


asyncio.run(main())
