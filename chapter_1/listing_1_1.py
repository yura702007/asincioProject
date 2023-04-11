"""
Операции, ограниченные производительностью ввода-вывода и
быстродействием процессора
"""
import requests

# Веб-запрос ограничен производительностью ввода-вывода
response = requests.get('https://www.example.com')

items = response.headers.items()

# Обработка ответа ограничена быстродействием процессора
headers = [f'{key}: {header}' for key, header in items]

# Конкатенация строк ограничена быстродействием процессора
formatter_headers = '\n'.join(headers)

# Запись на ограничена производительностью ввода-вывода
with open('headers.txt', 'w', encoding='utf8') as file:
    file.write(formatter_headers)
