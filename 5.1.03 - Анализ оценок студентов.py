
n = int(input())

values = tuple(int(input()) for _ in range(n))
average = sum(values) / n

print(values)
print(f'{average:.2f}')

print(tuple((value for value in values if value >= average)))