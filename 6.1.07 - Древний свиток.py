


string = input().replace(' ', '')

result = list(set(string))
result.sort()

print(len(string) - len(result))
print(tuple(result))