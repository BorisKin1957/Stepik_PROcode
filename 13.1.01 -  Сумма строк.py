'''
Шаг 1. Объяви функцию row_sums(matrix), где matrix --> список списков чисел.
Шаг 2. Для каждой строки матрицы вычисли сумму её элементов.
Шаг 3. Верни список сумм по строкам в том же порядке.
'''


def row_sums(matrix: list[list[int]]) -> list[int]:
    result = [sum(lst) for lst in matrix]
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(row_sums(matrix))