"""
Распараллеливание с помощью пула процессов и MapReduce
"""
import asyncio
import concurrent.futures
import functools
import time
from typing import Dict, List


def partition(file, size: int) -> List:
    """
    Вернуть файл по частям в виде списков
    :param file: объект файла
    :param size: размер части файла
    :return: часть файла в виде списка
    """
    data = True
    while data:
        data = file.readlines(size)
        if data:
            yield data


def map_frequencies(chunk: List[str]) -> Dict[str, int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] += int(count)
        else:
            counter[word] = int(count)
    return counter


def merge_dictionaries(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    for key in second:
        if key in first:
            first[key] += second[key]
        else:
            first[key] = second[key]
    return first


async def main(partition_size: int):
    with open('file', 'r', encoding='utf8') as f:
        loop = asyncio.get_running_loop()
        tasks = []
        start = time.time()
        with concurrent.futures.ProcessPoolExecutor() as pool:
            for chunk in partition(f, partition_size):
                tasks.append(loop.run_in_executor(
                    pool,
                    functools.partial(map_frequencies, chunk)
                ))  # Для каждой порции выполнить операцию отображения в отдельном процессе
            intermediate_results = await asyncio.gather(*tasks)  # Ждать завершения всех операций отображения

            # Редуцировать промежуточные результаты в окончательный
            final_results = functools.reduce(merge_dictionaries, intermediate_results)
            print(f"Aardvark встречается {final_results['Aardvark']} раз")

            print(f'Время MapReduce {time.time() - start} секунд')


if __name__ == '__main__':
    asyncio.run(main(10**7))
