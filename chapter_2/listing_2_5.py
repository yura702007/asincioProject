"""
Первое применение asyncio.sleep()
"""
import asyncio


async def hello_world_message() -> str:
    await asyncio.sleep(1)  # Приостановить hello_world_message на одну секунду
    return 'Hello, World!!!'


async def main() -> None:
    message = await hello_world_message()
    print(message)


if __name__ == '__main__':
    asyncio.run(main())
