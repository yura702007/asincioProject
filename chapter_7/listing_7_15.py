"""
Приложение для нагрузочного тестирования
"""
import asyncio
from asyncio import AbstractEventLoop
from threading import Thread
from chapter_7.listing_7_14 import LoadTester


class ThreadedEventLoop(Thread):
    """
    Класс потока,
    в котором будет происходить
    цикл событий asyncio
    """

    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True

    def run(self):
        self._loop.run_forever()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio_thread = ThreadedEventLoop(loop)
    # Запустить новый поток,
    # исполняющий цикл событий asyncio в фоновом режиме
    asyncio_thread.start()

    # Создать приложение Tkinter
    # и запустить его главный цикл событий
    app = LoadTester(loop)
    app.mainloop()
