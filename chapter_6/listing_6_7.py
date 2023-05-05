"""
Подсчёт частоты слов начинающихся с буквы a
"""
import time


def get_text():
    with open('file', 'r', encoding='utf8') as file:
        for line in file:
            yield line.strip().split('\t')


def word_counter():
    words = get_text()
    words_dict = {}
    for word_lst in words:
        word = word_lst[0]
        count = word_lst[2]
        if word in words_dict:
            words_dict[word] += count
        else:
            words_dict[word] = count
        print(word)


def main():
    start = time.time()
    word_counter()
    print(time.time() - start)


if __name__ == '__main__':
    main()
