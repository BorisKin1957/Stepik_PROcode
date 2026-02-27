


from json import loads

data = loads(input())
codes = input().split()

result = [data.get(code, '?') for code in codes]

print(''.join(result))