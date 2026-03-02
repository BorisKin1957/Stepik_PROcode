


names_1 = set([name.strip() for name in input().split(',')])
names_2 = set([name.strip() for name in input().split(',')])

result = ', '.join(sorted(names_1 - names_2))
print(f'1. Кто был на шоу, но не прошел первый тур: {result}')

result = ', '.join(sorted(names_1 & names_2))
print(f'2. Кто пришел на шоу и прошел первый тур: {result}')

result = ', '.join(sorted(names_1 | names_2))
print(f'3. Все, кто хотя бы один раз был на шоу: {result}')

result = ', '.join(sorted(names_1 ^ names_2))
print(f'4. Кто пришел на шоу, но не прошел тур, и наоборот: {result}')