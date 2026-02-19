

numbers = tuple(map(int, input().split()))
sum_positive = sum(filter(lambda x: x > 0, numbers))
sum_negative = sum(filter(lambda x: x < 0, numbers)) * 2

result = sum_positive + sum_negative

if result < 10:
    result *= 2

print(f'Сила камней: {result}')