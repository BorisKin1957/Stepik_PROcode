
result = {}
count = int(input())

for _ in range(3):
    island, cash = input().split(': ')
    result[island] = int(cash) // count


for island in result:
    print(f'{island}: {result[island]}')