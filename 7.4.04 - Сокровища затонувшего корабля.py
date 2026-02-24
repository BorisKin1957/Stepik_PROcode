


numbers = map(int, input().split())

numbers_dict = {}

for num in numbers:
    numbers_dict[num] = numbers_dict.get(num, 0) + 1

print(*numbers_dict)