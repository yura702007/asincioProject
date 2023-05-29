"""
Асинхронный читатель стандартного ввода
"""
import asyncio
from asyncio import StreamReader
from util import delay
import sys


async def create_std_reader() -> StreamReader:
    stream_reader = StreamReader()
    protocol = asyncio.StreamReaderProtocol(stream_reader=stream_reader)
    loop = asyncio.get_running_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    return stream_reader


async def main():
    stdin_reader = await create_std_reader()
    while True:
        delay_time: str = await stdin_reader.readline()
        if delay_time:
            await asyncio.create_task(delay(int(delay_time)))
        else:
            print('EXIT')
            break


if __name__ == '__main__':
    asyncio.run(main())
