"""
Наблюдение за ходом отображения
"""
from concurrent.futures import ProcessPoolExecutor
import functools
import asyncio
from multiprocessing import Value
from typing import List, Dict
from chapter_6.listing_6_8 import partition, merge_dictionaries
map_progress: Value


def init(progress: Value):
    global map_progress
    map_progress = progress


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] += int(count)
        else:
            counter[word] = int(count)

    with map_progress.get_lock():
        map_progress.value += 1
    progress_reporter()

    return counter


def progress_reporter():
    print(f'Завершено операций отображения: {map_progress.value}')


async def main(partition_size: int):
    global map_progress

    with open('file', 'r', encoding='utf8') as f:
        loop = asyncio.get_running_loop()
        tasks = []
        map_progress = Value('i', 0)

        with ProcessPoolExecutor(initializer=init, initargs=(map_progress,)) as pool:

            for chunk in partition(f, partition_size):
                tasks.append(loop.run_in_executor(pool, functools.partial(map_frequencies, chunk)))
            counters = await asyncio.gather(*tasks)
            final_result = functools.reduce(merge_dictionaries, counters)
            print(f"Aardvark встречается {final_result['Aardvark']} раз")


if __name__ == '__main__':
    asyncio.run(main(10 ** 7))
