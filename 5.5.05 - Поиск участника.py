

# Заранее заданный кортеж из 50 чисел (числа от 0 до 9)
numbers = (
    3, 1, 4, 1, 5, 9, 2, 6, 5, 3,
    5, 8, 9, 7, 9, 3, 2, 3, 8, 4,
    6, 2, 6, 4, 3, 3, 8, 3, 2, 7,
    9, 5, 0, 2, 8, 8, 4, 1, 9, 7,
    1, 6, 9, 3, 9, 9, 3, 7, 5, 1
)

wanted, start, end = int(input()), int(input()), int(input())

if wanted in numbers[start:end]:
    print(f'Первое вхождение числа {wanted} в диапазоне от {start} до {end} '
          f'находится на индексе: {len(numbers[:start]) + numbers[start:end].index(wanted)}')
else:
    print(f'Число {wanted} не найдено в диапазоне от {start} до {end}.')

'''

НАДО БЫЛО по шаблону:

numbers.index(wanted, start, end)
'''