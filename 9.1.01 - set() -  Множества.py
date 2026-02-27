


result = [float(number) for number in set(input().split())]

print(f'Сумма минимального и максимального числа: {round(min(result) + max(result), 2)}')
