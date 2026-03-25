

import json

data = json.loads(input())  # Преобразуем строку JSON обратно в словарь

for key, value in data.items():
    print(f'Модуль: {key}, количество: {value}')
print(f'Всего модулей: {sum(data.values())}')