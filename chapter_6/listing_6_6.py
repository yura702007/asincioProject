"""
Однопоточная модель MapReduce
"""
import functools
from typing import Dict


def map_frequency(text: str) -> Dict[str, int]:
    words = text.split(' ')
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


def merge_dictionaries(first: Dict[str, int], second: Dict[str, int]) -> Dict[str, int]:
    for key in second:
        if key in first:
            first[key] += second[key]
        else:
            first[key] = second[key]
    return first


lines = [
    "I know what I know",
    "I know that I know",
    "I don't know much",
    "They don't know much"
]


def main():
    mapped_result = [map_frequency(line) for line in lines]

    for result in mapped_result:
        print(result)

    print(functools.reduce(merge_dictionaries, mapped_result))


if __name__ == '__main__':
    main()
