"""
Выполнение HTTP запроса с помощью транспортного механизма и протокола
"""
from asyncio import Transport, Future, AbstractEventLoop, Protocol
from typing import Optional


class HTTPGetClientProtocol(Protocol):
    def __init__(self, host: str, loop: AbstractEventLoop):
        self._host: str = host
        self._future: Future = loop.create_future()
        self._transport: Optional[Transport] = None
        self._response_buffer: bytes = b''

    async def get_response(self):
        # Ждать внутренний будущий объект,
        # пока не будет получен ответ от сервера
        return await self._future

    def _get_request_bytes(self) -> bytes:
        # Создать PEE запрос
        request = f"GET / HTTP/1.1\r\n" \
                  f"Connection: close\r\n" \
                  f"Host: {self._host}\r\n\r\n"
        return request.encode()

    def connection_made(self, transport: Transport):
        # После того как подключение установленно
        # использовать транспорт для отправки запроса
        print(f'Создано подкючение к {self._host}')
        self._transport = transport
        self._transport.write(self._get_request_bytes())

    def data_received(self, data):
        # Получив данные сохранить их во внутреннем буфере
        print(f'Получены данные')
        self._response_buffer += data

    def eof_received(self) -> Optional[bool]:
        # После закрытия подключения
        # завершить будущий объект,
        # скопировав в него данные из буфера
        self._future.set_result(self._response_buffer.decode())
        return False

    def connection_lost(self, exc: Optional[Exception] | None) -> None:
        # Если подключение было закрыто без ошибок-
        # не делать ничего,
        # иначе завершить будущий объект исключением
        if exc:
            self._future.set_exception(exc)
        else:
            print(f'Подключение закрыто без ошибок')
