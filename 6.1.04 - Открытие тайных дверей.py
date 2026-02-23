

numbers = tuple(map(int, input().split()))

min_num, max_num = min(numbers), max(numbers)

result = [num for num in numbers if num != min_num and num != max_num]

print(min_num, max_num)
print(tuple(result))

