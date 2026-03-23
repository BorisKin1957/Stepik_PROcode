'''Шаг 1. Объявите функцию determinant_3x3(matrix), которая принимает квадратную матрицу
3×3 (список из трёх списков по три числа).
Шаг 2. Если матрица не имеет форму 3×3, выбросьте исключение (например, ValueError) с
понятным сообщением.
Шаг 3. Вычислите определитель по формуле:

    Обозначим элементы как
    a b c
    d e f
    g h i

    Тогда
    det = a*(e*i − f*h) − b*(d*i − f*g) + c*(d*h − e*g)
    Шаг 4. Верните вычисленное значение.'''


def determinant_3x3(matrix):
    try:
        if len(matrix[0]) != 3 or len(matrix) != 3:
            raise ValueError
        a, b, c = matrix[0]
        d, e, f = matrix[1]
        g, h, i = matrix[2]

        result = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    except ValueError:
        print('На фиг! На фиг! Кричали пьяные пионеры')
    return result


matrix = [
    [6, 1, 1],
    [4, -2, 5],
    [2, 8, 7]
]
print(determinant_3x3(matrix))
