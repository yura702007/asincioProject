"""
Использование сопрограммы execute для выполнения команды create
"""
import asyncio
import asyncpg
from listing_5_2 import *


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password'
    )
    statements = [
        CREATE_BRAND_TABLE,
        CREATE_PRODUCT_TABLE,
        CREATE_PRODUCT_COLOR_TABLE,
        CREATE_PRODUCT_SIZE_TABLE,
        CREATE_SKU_TABLE,
        SIZE_INSERT,
        COLOR_INSERT
    ]

    print('Создаётся база данных product')
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('База данных product создана')
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
