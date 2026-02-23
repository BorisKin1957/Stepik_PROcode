

ants = {}

for _ in range(5):
    ant, weight = input(), int(input())
    ants[ant] = weight

for ant in ants:
    print(f'{ant} - {ants[ant]} гр. сахара!')