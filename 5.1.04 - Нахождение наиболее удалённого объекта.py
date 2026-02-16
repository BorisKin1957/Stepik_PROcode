'''Считайте:

    целое число N --> количество объектов;

    затем для каждого объекта по две строки: x и y (вещественные числа).

Для каждого объекта сформируйте кортеж (x, y). Найдите объект с максимальным расстоянием
до начала координат, где расстояние рассчитывается по формуле:
Выведите две строки:

    кортеж координат наиболее удалённого объекта (как в стандартном представлении Python,
    с числами типа float);

    расстояние до этого объекта, округлённое до двух знаков после запятой.
'''


from math import sqrt

def get_hypotenuse(a: float, b: float) -> float:
    '''гипотенуза прямоугольного треугольника'''
    return round(sqrt(a ** 2 + b ** 2), 2)


max_vector, gipotenuse, coordinates = 0.0, 0.0, (0.0, 0,0)

for _ in range(int(input())):
    x, y = float(input()), float(input())
    gipotenuse = get_hypotenuse(x, y)
    if gipotenuse > max_vector:
        max_vector = gipotenuse
        coordinates = x, y

print(coordinates)
print(f'{max_vector:.2f}')
