
data = []

for item in input().split(', '):
    kind, force = item.split()
    data.append((kind, force))

while True:
    kind = data[0][0]
    force = int(data[0][1])
    if len(data) > 1 and kind in sum(data[1:], ()):
        for k, v in data[1:]:
            if k == kind:
                force += int(v)
                data.remove((kind, v))
        data.remove(data[0])
    else:
        print(f'Общая сила {kind} камень: {force}')
        break

    print(f'Общая сила {kind } камень: {force}')