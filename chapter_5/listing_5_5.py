"""
Вставка случайных брендов
"""
import asyncpg
import asyncio
from typing import List, Tuple, Union
from random import sample


def load_brands(path='brands.txt') -> List[str]:
    with open(path, 'r', encoding='utf8') as file:
        return file.readlines()


def generate_brand_names(brands: List[str]) -> List[Tuple[Union[str, ]]]:
    return [(brands[index].strip(),) for index in sample(range(4000), 100)]


async def insert_brands(brands_lst, connection) -> int:
    brands = generate_brand_names(brands_lst)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)


async def main():
    common_brands = load_brands()
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password'
    )
    await insert_brands(common_brands, connection)


if __name__ == '__main__':
    asyncio.run(main())
