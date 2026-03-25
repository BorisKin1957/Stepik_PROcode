
cities = tuple([city.strip() for city in input().split(',')])

print(cities)
print(f'Последний город тура: {cities[-1]}')