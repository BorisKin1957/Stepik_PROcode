

if not (num := int(input())) % 2:  # четное
    num //= 3
else:                               # нечетное
    num *= 3

print(f'Конечная позиция Счетчика: {num + 5}')
