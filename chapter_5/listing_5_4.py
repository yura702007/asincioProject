"""
Вставка и выборка марок
"""
import asyncio
import asyncpg
from asyncpg import Record
from typing import List


async def main():
    # Подключение к БД
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password'
    )

    # Внесение данных в таблицу brand
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    # Запрос для получения данных из таблицы
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    # Получение данных из таблицы и сохранение результатов
    results: List[Record] = await connection.fetch(brand_query)

    for brand in results:
        print(f'id: {brand["brand_id"]}, name: {brand["brand_name"]}')

    # Отключение от БД
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
