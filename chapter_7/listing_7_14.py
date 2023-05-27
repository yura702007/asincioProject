"""
Tkinter GUI
"""
from queue import Queue
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from typing import Optional
from chapter_7.listing_7_13 import StressTest


class LoadTester(Tk):

    def __init__(self, loop, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self._queue = Queue()
        self._refresh_ms = 25

        self._loop = loop
        self._load_test: Optional[StressTest] = None
        self.title("URL REQUESTS")

        self._url_label = Label(self, text="URL:")
        self._url_label.grid(column=0, row=0)

        self._url_field = Entry(self, width=30)
        self._url_field.grid(column=1, row=0)

        self._request_label = Label(self, text='Number of Request')
        self._request_label.grid(column=0, row=1)

        self._request_field = Entry(self, width=10)
        self._request_field.grid(column=1, row=1)

        self._submit = ttk.Button(self, text='SUBMIT', command=self._start)  # При нажатии на кнопку SUBMIT,
        self._submit.grid(column=2, row=1)  # вызывается метод _start

        self._pb_label = Label(self, text='PROGRESS')
        self._pb_label.grid(column=0, row=3)

        self._pb = ttk.Progressbar(self, orient='horizontal', length=200, mode='determinate')
        self._pb.grid(column=1, row=3, columnspan=2)

    def _update_bar(self, ptc: int):
        """
        Метод _update_bar устанавливает
        процент заполненности индикатора
        хода выполнения от 0 до 100.
        Его следует вызывать только
        из главного потока
        :param ptc: int
        :return: None
        """
        if ptc == 100:
            self._load_test = None
            self._submit['text'] = 'SUBMIT'
        else:
            self._pb['value'] = ptc
            self.after(self._refresh_ms, self._poll_queue)

    def _queue_update(self, completed_requests: int, total_requests: int):
        """
        Обратный вызов,
        который передаётся
        нагрузочному тесту;
        он добавляет обновление
        индикатора в очередь
        :param completed_requests: int
        :param total_requests: int
        :return: None
        """
        self._queue.put(int(completed_requests / total_requests * 100))

    def _poll_queue(self):
        """
        Извлечение обновления индикатора
        из очереди,
        усли получилось
        обновить индикатор
        :return: None
        """
        if not self._queue.empty():
            percent_complete = self._queue.get()
            self._update_bar(percent_complete)
        else:
            if self._load_test:
                self.after(self._refresh_ms, self._poll_queue)

    def _start(self):
        if self._load_test is None:
            self._submit['text'] = 'Cancel'
            test = StressTest(self._loop,
                              self._url_field.get(),
                              int(self._request_field.get()),
                              self._queue_update)
            self.after(self._refresh_ms, self._poll_queue)
            test.start()
            self._loop = test
        else:
            self._load_test.cancel()
            self._load_test = None
            self._submit['text'] = 'SUBMIT'
