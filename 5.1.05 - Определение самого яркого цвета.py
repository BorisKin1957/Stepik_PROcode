'''Считай:

    целое число N --> количество цветов;

    затем для каждого цвета три целых числа: R, G, B (каждое с новой строки).

Для каждого цвета сформируй кортеж (R, G, B), вычисли его яркость как R + G + B и найди
цвет с максимальной яркостью.

Выведи две строки:

    кортеж самого яркого цвета;

    его яркость (сумму R + G + B).
'''

max_light, rgb = 0, (0, 0, 0)

for _ in range(int(input())):
    r, g, b = int(input()), int(input()), int(input())
    light = r + g + b
    if light > max_light:
        max_light = light
        rgb = r, g, b

print(rgb)
print(max_light)
