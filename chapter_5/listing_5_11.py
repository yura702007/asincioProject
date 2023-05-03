"""
Вложенная транзакция
"""
import asyncio
import logging
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')
    async with connection.transaction():
        await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'my_new_brand')")
        try:
            # попытка выполнить вложенную транзакцию
            async with connection.transaction():
                await connection.execute("INSERT INTO product_color VALUES(1, 'black')")
        except Exception as exc:
            logging.warning('Ошибка при вставке цвета товара игнорируется', exc_info=exc)
    # успешная внешняя транзакция записана в БД
    query = """
        SELECT FROM brand
        WHERE brand_name LIKE 'my_new%'
    """
    brand = await connection.fetch(query)
    print(brand)
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
