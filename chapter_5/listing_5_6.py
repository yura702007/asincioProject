"""
Вставка случайных товаров и SKU
"""
import asyncpg
import asyncio
from typing import List, Tuple
from random import randint, sample
from chapter_5.listing_5_5 import load_brands


def gen_products(common_words: List[str],
                 brand_id_start: int,
                 brand_id_end: int,
                 products_to_create: int) -> List[Tuple[str, int]]:
    products = []
    for _ in range(products_to_create):
        description = [common_words[index].strip() for index in sample(range(len(common_words)), 10)]
        brand_id = randint(brand_id_start, brand_id_end)
        products.append((" ".join(description), brand_id))
    return products


def gen_skus(product_id_start: int,
             product_id_end: int,
             skus_to_create: int) -> List[Tuple[int, int, int]]:
    skus = []
    for _ in range(skus_to_create):
        product_id = randint(product_id_start, product_id_end)
        size_id = randint(1, 3)
        color_id = randint(1, 2)
        skus.append((product_id, size_id, color_id))
    return skus


async def main():
    common_products = load_brands(path='products.txt')
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='postgres',
                                       database='products',
                                       password='password')
    product_tuple = gen_products(common_words=common_products,
                                 brand_id_start=1,
                                 brand_id_end=100,
                                 products_to_create=1000)
    await connection.executemany("INSERT INTO product VALUES(DEFAULT, $1, $2)", product_tuple)
    sku_tuple = gen_skus(product_id_start=1,
                         product_id_end=1000,
                         skus_to_create=10000)
    await connection.executemany("INSERT INTO sku VALUES(DEFAULT, $1, $2, $3)", sku_tuple)
    await connection.close()


if __name__ == '__main__':
    asyncio.run(main())
