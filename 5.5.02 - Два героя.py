

numbers = tuple(input().split())
num = input()

print(f'Число {num} встречается {numbers.count(num)} раз(а) в кортеже.')

if num in numbers:
    print(f'Первое вхождение числа {num} находится на индексе {numbers.index(num)}.')
else:
    print(f'Число {num} не найдено в кортеже.')