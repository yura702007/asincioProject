"""
Распараллеливание операции reduce
"""
import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List
from chapter_6.listing_6_8 import partition, merge_dictionaries, map_frequencies


def partition_lists(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i: i + chunk_size]


async def reduce(loop, pool, counters, chunk_size) -> Dict[str, int]:
    # Разбить словари на допускающие распараллеливание порции
    chunks: List[List[Dict]] = list(partition_lists(counters, chunk_size))
    reducers = []
    while len(chunks[0]) > 1:
        for chunk in chunks:
            # Редуцировать каждую порцию в один словарь
            reducer = functools.partial(functools.reduce, merge_dictionaries, chunk)
            reducers.append(loop.run_in_executor(pool, reducer))
        # Ждать завершения всех операций редукции
        reducer_chunks = await asyncio.gather(*reducers)
        # Снова разбить результаты и выполнить ещё одну операцию цикла
        chunks = list(partition(reducer_chunks, chunk_size))
        reducers.clear()
    return chunks[0][0]


async def main(partition_size: int):
    with open('file', 'r', encoding='utf8') as f:
        loop = asyncio.get_running_loop()
        tasks = []
        with concurrent.futures.ProcessPoolExecutor() as pool:
            start = time.time()
            for chunk in partition(f, partition_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))
            intermediate_results = await asyncio.gather(*tasks)
            final_results = await reduce(loop, pool, intermediate_results, 500)
            print(f"Aardvark встречается {final_results['Aardvark']} раз")

            print(f'Время MapReduce {time.time() - start} секунд')


if __name__ == '__main__':
    asyncio.run(main(10 ** 7))
