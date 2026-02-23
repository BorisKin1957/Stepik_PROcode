


numbers = tuple(map(int, input().split(',')))

weight = sum(numbers)

result = tuple([weight - num for num in numbers])

print(weight)
print(result)