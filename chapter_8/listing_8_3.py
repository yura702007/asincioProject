"""
Оправка HTTP запроса с помощью потоковых писателей и читателей
"""
import asyncio
from asyncio import StreamReader
from typing import AsyncGenerator


async def read_until_empty(stream_reader: StreamReader) -> AsyncGenerator[str, None]:
    # Читать и декодировать стоку, пока не закончатся символы
    while response := await stream_reader.readline():
        yield response.decode()


async def main():
    host: str = 'www.example.com'
    request: str = f"GET / HTTP/1.1\r\n" \
                   f"Connection: close\r\n" \
                   f"Host: {host}\r\n\r\n"
    steam_reader, steam_writer = await asyncio.open_connection(host=host, port=80)
    try:
        # Записать http-запрос и опустошить буфер писателя
        steam_writer.write(request.encode())
        await steam_writer.drain()

        # Читать строки и сохранять их в списке
        responses = [response async for response in read_until_empty(steam_reader)]
        print(''.join(responses))
    finally:
        # Закрыть писатель и ждать завершения закрытия
        steam_writer.close()
        await steam_writer.wait_closed()


if __name__ == '__main__':
    asyncio.run(main())
