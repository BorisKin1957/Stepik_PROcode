'''Шаг 1. Считайте словарь scores, где ключи --> уникальные идентификаторы участников,
значения --> набранные баллы.

Шаг 2. Сформируйте новый словарь, из которого удалены все пары, чьи значения равны
минимальному значению в scores.

Шаг 3. Выведите получившийся словарь.'''

# Этот код читает словарь из стандартного ввода, преобразует его в объект Python и сохраняет в переменную scores.
import ast
import sys

input_data = sys.stdin.read().strip()
scores = ast.literal_eval(input_data)

result = filter(lambda x: x[1] > min(scores.values()), scores.items())

print(dict(result))