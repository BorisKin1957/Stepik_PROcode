'''Проверить равенство главной и побочной диагоналей'''

def is_double_diagonal_equal(matrix):
    # Проверяем, является ли матрица квадратной (число строк равно числу столбцов)
    if len(matrix) != len(matrix[0]):
        return 'Матрица не квадратная'

    # Списки для хранения элементов главной и побочной диагоналей
    main_diag, aux_diag = [], []

    # Размер матрицы (количество строк/столбцов)
    vol = len(matrix)

    # Проходим по каждой строке матрицы
    for i in range(vol):
        # Добавляем элемент с главной диагонали: индексы [i][i]
        main_diag.append(matrix[i][i])

        # Добавляем элемент с побочной диагонали: индексы [i][vol - 1 - i]
        aux_diag.append(matrix[i][vol - 1 - i])

    # Сравниваем списки элементов главной и побочной диагоналей
    # Если они одинаковы — возвращаем True, иначе False
    return main_diag == aux_diag


# Тестовые примеры:


matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
print(is_double_diagonal_equal(matrix))  # Ожидается: True


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(is_double_diagonal_equal(matrix))  # Ожидается: False


matrix = [
    [1, 2],
    [2, 1]
]
print(
    is_double_diagonal_equal(matrix))