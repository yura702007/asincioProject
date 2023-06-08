"""
Асинхронный читатель стандартного ввода
"""
import sys
import asyncio
from concurrent.futures import Future
from asyncio import AbstractEventLoop
from threading import Thread
from util import delay, async_timed


def reader_stdin() -> int:
    return int(input('Введите количество секунд: '))


# async def create_std_reader():
#     stream_reader = asyncio.StreamReader()
#     protocol = asyncio.StreamReaderProtocol(stream_reader=stream_reader)
#     loop = asyncio.get_running_loop()
#     await loop.connect_read_pipe(lambda: protocol, sys.stdin)
#     return stream_reader


class ThreadedEventLoop(Thread):
    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True

    def run(self):
        self._loop.run_forever()


@async_timed()
async def main():
    tasks = []
    while True:
        try:
            tasks.append(asyncio.create_task(delay(reader_stdin())))
        except ValueError:
            break
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
