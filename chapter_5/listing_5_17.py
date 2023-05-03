"""
Получение заданного числа элементов с помощью асинхронного генератора
"""
import asyncpg
import asyncio


async def take(generator, to_take: int):
    item_count = 0
    async for item in generator:
        if item_count > to_take:
            return
        item_count += 1
        yield item


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')
    async with connection.transaction():
        query = 'SELECT brand_id, brand_name FROM brand'
        product_generator = connection.cursor(query)
        async for product in take(product_generator, 5):
            print(product)
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
