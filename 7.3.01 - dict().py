


result = {}

for symbol in input():
    result[symbol] = result.get(symbol, 0) + 1

print(result)