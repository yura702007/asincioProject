"""
Обработка ошибки в транзакции
"""
import logging

import asyncpg
import asyncio


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')
    try:
        async with connection.transaction():
            insert_brand = "INSERT INTO brand VALUES(9999, 'big_brand')"
            await connection.execute(insert_brand)
            await connection.execute(insert_brand)
    except Exception:
        # Запротоколировать ошибку
        logging.exception('Ошибка при выполнениии транзакции')
    finally:
        query = """
            SELECT FROM brand
            WHERE brand_name LIKE 'big_%'
        """
        # Выбрать бренды и убедиться, что ничего не вставлено
        brands = await connection.fetch(query)
        print(f'Результаты запроса: {brands}')
        await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
