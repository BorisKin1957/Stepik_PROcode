'''Шаг 1. Объяви функцию matrix_multiply(a, b), где a и b --> прямоугольные матрицы (списки списков).
Шаг 2. Проверь совместимость размеров: число столбцов a должно быть равно числу строк b.
— Если несовместимы, верни ровно строку: ❌ Матрицы несовместимы - нельзя перемножить.
Шаг 3. Иначе верни новую матрицу c размера len(a) × len(b[0]), где
c[i][j] = Σ a[i][k] * b[k][j] по всем k.'''


def matrix_multiply(a, b):
    # Проверяем совместимость: число столбцов a должно равняться числу строк b
    if len(a[0]) != len(b):
        return "❌ Матрицы несовместимы - нельзя перемножить"

    # Создаем результирующую матрицу c размером len(a) x len(b[0])
    rows_a = len(a)
    cols_b = len(b[0])
    cols_a = len(a[0])

    c = [[0] * cols_b for _ in range(rows_a)]

    # Выполняем умножение матриц
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                c[i][j] += a[i][k] * b[k][j]

    return c


a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [7, 8],
    [9, 10],
    [11, 12]
]
print(matrix_multiply(a, b))
a = [
    [1, 2],
    [3, 4]
]

b = [
    [5, 6],
    [7, 8]
]
print(matrix_multiply(a, b))
a = [
    [1, 2, 3]
]

b = [
    [4, 5]
]
print(matrix_multiply(a, b))
a = [
    [1, 0],
    [0, 1]
]

b = [
    [5, 6],
    [7, 8]
]
print(matrix_multiply(a, b))
a = [
    [2, 3, 4]
]

b = [
    [5],
    [6],
    [7]
]
print(matrix_multiply(a, b))
a = [
    [1, 2, 3],
    [4, 5, 6]
]

b = [
    [7, 8],
    [9, 10],
    [11, 12]
]
print(matrix_multiply(a, b))
a = [
    [1, 2]
]

b = [
    [3, 4, 5]
]
print(matrix_multiply(a, b))