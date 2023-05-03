"""
Создание транзакции
"""
import asyncio
import asyncpg


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')

    # начать транзакцию базы данных
    async with connection.transaction():
        await connection.execute("INSERT INTO brand "
                                 "VALUES(DEFAULT, 'brand_1')")
        await connection.execute("INSERT INTO brand "
                                 "VALUES(DEFAULT, 'brand_2')")

    query = """
        SELECT brand_name FROM brand
        WHERE brand_name LIKE 'brand%'
    """
    # выбрать марки и убедиться, что транзакция зафиксирована
    brands = await connection.fetch(query)
    print(brands)

    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())