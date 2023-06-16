"""
Асинхронный читатель стандартного ввода
"""
import asyncio
from asyncio import StreamReader
import sys


async def create_std_reader() -> StreamReader:
    stream_reader = StreamReader()
    protocol = asyncio.StreamReaderProtocol(stream_reader=stream_reader)
    loop = asyncio.get_running_loop()
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    return stream_reader


if __name__ == '__main__':
    asyncio.run(create_std_reader())
